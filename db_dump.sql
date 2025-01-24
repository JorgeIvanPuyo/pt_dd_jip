--
-- PostgreSQL database dump
--

-- Dumped from database version 15.8 (Debian 15.8-1.pgdg120+1)
-- Dumped by pg_dump version 15.8 (Debian 15.8-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: conductores; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.conductores (
    id integer NOT NULL,
    nombre character varying(255) NOT NULL
);


ALTER TABLE public.conductores OWNER TO "user";

--
-- Name: conductores_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.conductores_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.conductores_id_seq OWNER TO "user";

--
-- Name: conductores_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.conductores_id_seq OWNED BY public.conductores.id;


--
-- Name: ordenes; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.ordenes (
    id integer NOT NULL,
    ruta_id integer NOT NULL,
    prioridad boolean,
    valor double precision NOT NULL
);


ALTER TABLE public.ordenes OWNER TO "user";

--
-- Name: ordenes_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.ordenes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ordenes_id_seq OWNER TO "user";

--
-- Name: ordenes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.ordenes_id_seq OWNED BY public.ordenes.id;


--
-- Name: rutas; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.rutas (
    id integer NOT NULL,
    notas character varying(500),
    fecha_programada date NOT NULL,
    conductor_id integer NOT NULL
);


ALTER TABLE public.rutas OWNER TO "user";

--
-- Name: rutas_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.rutas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.rutas_id_seq OWNER TO "user";

--
-- Name: rutas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.rutas_id_seq OWNED BY public.rutas.id;


--
-- Name: conductores id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.conductores ALTER COLUMN id SET DEFAULT nextval('public.conductores_id_seq'::regclass);


--
-- Name: ordenes id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.ordenes ALTER COLUMN id SET DEFAULT nextval('public.ordenes_id_seq'::regclass);


--
-- Name: rutas id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.rutas ALTER COLUMN id SET DEFAULT nextval('public.rutas_id_seq'::regclass);


--
-- Data for Name: conductores; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.conductores (id, nombre) FROM stdin;
9	Eduardo B.
10	José N.
11	Mauricio J.
12	Miguel T.
13	Álvaro T.
14	Juan D.
15	Ariel F.
16	Carlos M.
17	Roberto R.
18	Basilio M.
19	Jorge G.
20	Felipe V.
\.


--
-- Data for Name: ordenes; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.ordenes (id, ruta_id, prioridad, valor) FROM stdin;
2002	1002	t	71
2003	1003	f	81.5
2004	1004	t	92
2005	1005	f	102.5
2006	1006	t	113
2007	1007	f	123.5
2008	1008	t	134
2009	1009	f	144.5
2001	1001	t	60.5
\.


--
-- Data for Name: rutas; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.rutas (id, notas, fecha_programada, conductor_id) FROM stdin;
1002	Ruta de ejemplo 3	2025-01-25	11
1003	Ruta de ejemplo 4	2025-01-26	12
1004	Ruta de ejemplo 5	2025-01-27	13
1005	Ruta de ejemplo 6	2025-01-28	14
1006	Ruta de ejemplo 7	2025-01-29	15
1007	Ruta de ejemplo 8	2025-01-30	16
1008	Ruta de ejemplo 9	2025-01-31	17
1009	Ruta de ejemplo 10	2025-02-01	18
1001	Ruta de ejemplo 2	2025-01-24	10
\.


--
-- Name: conductores_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.conductores_id_seq', 1, false);


--
-- Name: ordenes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.ordenes_id_seq', 1, false);


--
-- Name: rutas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.rutas_id_seq', 1, false);


--
-- Name: conductores conductores_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.conductores
    ADD CONSTRAINT conductores_pkey PRIMARY KEY (id);


--
-- Name: ordenes ordenes_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.ordenes
    ADD CONSTRAINT ordenes_pkey PRIMARY KEY (id);


--
-- Name: rutas rutas_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.rutas
    ADD CONSTRAINT rutas_pkey PRIMARY KEY (id);


--
-- Name: ordenes ordenes_ruta_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.ordenes
    ADD CONSTRAINT ordenes_ruta_id_fkey FOREIGN KEY (ruta_id) REFERENCES public.rutas(id);


--
-- Name: rutas rutas_conductor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.rutas
    ADD CONSTRAINT rutas_conductor_id_fkey FOREIGN KEY (conductor_id) REFERENCES public.conductores(id);


--
-- PostgreSQL database dump complete
--

