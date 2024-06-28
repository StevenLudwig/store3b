--
-- PostgreSQL database dump
--
--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: sl
--

--COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
--1	pbkdf2_sha256$720000$RyCUO0xFAEZMhakLeO4lMf$aCRTU7igjOu0TAsm5cW9tIxYyPX5JXRJ6HsHQ28jSJU=    2024-06-26 20:22:01+00  t	sl	Steve	Beltran	steve@mail.com  t	2024-06-26 20:10:21+00
--\.

--
-- Data for Name: catalog_product; Type: TABLE DATA; Schema: public; Owner: sl
--

COPY public.catalog_product (id, name, sku, price, is_active, created_at, updated_at) FROM stdin;
1	colchon	LU1001	8000.00	t	2024-06-26 22:02:42.452407+00	2024-06-26 22:02:42.45243+00
2	colchon king	LU1004	18000.00	t	2024-06-27 05:06:18.328321+00	2024-06-27 05:06:18.328353+00
3	colchon california	LU1005	20000.00	t	2024-06-27 16:05:51.188295+00	2024-06-27 20:07:43.382401+00
\.

--
-- Data for Name: django_celery_beat_intervalschedule; Type: TABLE DATA; Schema: public; Owner: sl
--

COPY public.django_celery_beat_intervalschedule (id, every, period) FROM stdin;
1	1	minutes
\.


--
-- Data for Name: django_celery_beat_periodictask; Type: TABLE DATA; Schema: public; Owner: sl
--

COPY public.django_celery_beat_periodictask (id, name, task, args, kwargs, queue, exchange, routing_key, expires, enabled, last_run_at, total_run_count, date_changed, description, crontab_id, interval_id, solar_id, one_off, start_time, priority, headers, clocked_id, expire_seconds) FROM stdin;
2	Check stock	apps.inventory.tasks.check_stock	[]	{}	\N	\N	\N	\N	t	2024-06-27 20:13:43.389942+00	55	2024-06-27 20:14:43.400584+00	Check stock status for products	\N	1	\N	f	2024-06-27 19:20:14+00	\N	{}	\N	\N
\.

--
-- Data for Name: inventory_stock; Type: TABLE DATA; Schema: public; Owner: sl
--

COPY public.inventory_stock (id, quantity, created_at, updated_at, product_id) FROM stdin;
3	100	2024-06-27 16:05:51.19471+00	2024-06-27 16:05:51.194728+00	3
1	100	2024-06-26 23:43:54.353344+00	2024-06-27 16:53:11.411707+00	1
2	10	2024-06-27 05:06:18.336048+00	2024-06-27 19:52:50.783748+00	2
\.

--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sl
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sl
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sl
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 76, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sl
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sl
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sl
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: catalog_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sl
--

SELECT pg_catalog.setval('public.catalog_product_id_seq', 3, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sl
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 19, true);


--
-- Name: django_celery_beat_clockedschedule_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sl
--

SELECT pg_catalog.setval('public.django_celery_beat_clockedschedule_id_seq', 1, false);


--
-- Name: django_celery_beat_crontabschedule_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sl
--

SELECT pg_catalog.setval('public.django_celery_beat_crontabschedule_id_seq', 1, true);


--
-- Name: django_celery_beat_intervalschedule_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sl
--

SELECT pg_catalog.setval('public.django_celery_beat_intervalschedule_id_seq', 1, true);


--
-- Name: django_celery_beat_periodictask_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sl
--

SELECT pg_catalog.setval('public.django_celery_beat_periodictask_id_seq', 2, true);


--
-- Name: django_celery_beat_solarschedule_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sl
--

SELECT pg_catalog.setval('public.django_celery_beat_solarschedule_id_seq', 1, false);


--
-- Name: django_celery_results_chordcounter_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sl
--

SELECT pg_catalog.setval('public.django_celery_results_chordcounter_id_seq', 1, false);


--
-- Name: django_celery_results_groupresult_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sl
--

SELECT pg_catalog.setval('public.django_celery_results_groupresult_id_seq', 1, false);


--
-- Name: django_celery_results_taskresult_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sl
--

SELECT pg_catalog.setval('public.django_celery_results_taskresult_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sl
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 19, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sl
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 54, true);


--
-- Name: inventory_stock_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sl
--

SELECT pg_catalog.setval('public.inventory_stock_id_seq', 3, true);


--
-- Name: order_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sl
--

SELECT pg_catalog.setval('public.order_order_id_seq', 13, true);


--
-- Name: order_orderitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sl
--

SELECT pg_catalog.setval('public.order_orderitem_id_seq', 9, true);

--
-- PostgreSQL database dump complete
--
