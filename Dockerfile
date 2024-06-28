FROM python:3.12.2-bookworm AS base


RUN <<EOT
    set -eux
    DEBIAN_FRONTEND=noninteractive
    apt update -y
    apt upgrade -y
    apt clean
EOT


FROM base AS builder

RUN <<EOT
    set -eux
    apt install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        python3-dev \
        python3-venv \
        manpages-dev
    apt clean
EOT

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN --mount=type=bind,source=requirements,target=/tmp/requirements <<EOT
    set -eux
    python3 -m venv --upgrade-deps /venv
    /venv/bin/python -m pip install -r /tmp/requirements/development.txt
EOT


FROM base

COPY --from=builder /venv /venv
COPY . /app

ENV PATH="/venv/bin:${PATH}"

# Set desired user and group IDs (replace with actual IDs)
ENV USER_ID=1000
ENV GROUP_ID=1000
# Create a group and a user with the specified IDs
RUN addgroup --gid $GROUP_ID user && adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user
# Set the user to use when running the container
USER user

WORKDIR /app