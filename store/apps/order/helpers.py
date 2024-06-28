import secrets
import time


def generate_order_number() -> str:
    return f"{time.strftime('%y%m%d')}{str(secrets.randbits(32))[:10]}"
