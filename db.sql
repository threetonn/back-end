--
-- PostgreSQL database dump
--

-- Dumped from database version 14.3
-- Dumped by pg_dump version 14.6

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
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO root;

--
-- Name: features; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.features (
    id integer NOT NULL,
    name character varying(45) NOT NULL
);


ALTER TABLE public.features OWNER TO root;

--
-- Name: features_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.features_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.features_id_seq OWNER TO root;

--
-- Name: features_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.features_id_seq OWNED BY public.features.id;


--
-- Name: gender; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.gender (
    id integer NOT NULL,
    name character varying(45) NOT NULL
);


ALTER TABLE public.gender OWNER TO root;

--
-- Name: gender_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.gender_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.gender_id_seq OWNER TO root;

--
-- Name: gender_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.gender_id_seq OWNED BY public.gender.id;


--
-- Name: gym; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.gym (
    id integer NOT NULL,
    name character varying(45) NOT NULL,
    address character varying(45) NOT NULL
);


ALTER TABLE public.gym OWNER TO root;

--
-- Name: gym_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.gym_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.gym_id_seq OWNER TO root;

--
-- Name: gym_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.gym_id_seq OWNED BY public.gym.id;


--
-- Name: role; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.role (
    id integer NOT NULL,
    name character varying(45) NOT NULL
);


ALTER TABLE public.role OWNER TO root;

--
-- Name: role_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.role_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.role_id_seq OWNER TO root;

--
-- Name: role_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.role_id_seq OWNED BY public.role.id;


--
-- Name: route; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.route (
    id integer NOT NULL,
    route character varying(45) NOT NULL,
    name character varying(45)
);


ALTER TABLE public.route OWNER TO root;

--
-- Name: route_has_role; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.route_has_role (
    "Route_id" integer NOT NULL,
    "Role_id" integer NOT NULL
);


ALTER TABLE public.route_has_role OWNER TO root;

--
-- Name: route_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.route_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.route_id_seq OWNER TO root;

--
-- Name: route_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.route_id_seq OWNED BY public.route.id;


--
-- Name: subscription; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.subscription (
    id integer NOT NULL,
    description text,
    is_active boolean DEFAULT true NOT NULL,
    "SubscriptionDuration_id" integer NOT NULL,
    "SubscriptionType_id" integer NOT NULL
);


ALTER TABLE public.subscription OWNER TO root;

--
-- Name: subscription_has_features; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.subscription_has_features (
    "Subscription_id" integer NOT NULL,
    "Features_id" integer NOT NULL
);


ALTER TABLE public.subscription_has_features OWNER TO root;

--
-- Name: subscription_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.subscription_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.subscription_id_seq OWNER TO root;

--
-- Name: subscription_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.subscription_id_seq OWNED BY public.subscription.id;


--
-- Name: subscriptionduration; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.subscriptionduration (
    id integer NOT NULL,
    price double precision NOT NULL,
    discount double precision NOT NULL
);


ALTER TABLE public.subscriptionduration OWNER TO root;

--
-- Name: subscriptionduration_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.subscriptionduration_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.subscriptionduration_id_seq OWNER TO root;

--
-- Name: subscriptionduration_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.subscriptionduration_id_seq OWNED BY public.subscriptionduration.id;


--
-- Name: subscriptiontype; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.subscriptiontype (
    id integer NOT NULL,
    name character varying(45) NOT NULL,
    type character varying(45) NOT NULL
);


ALTER TABLE public.subscriptiontype OWNER TO root;

--
-- Name: subscriptiontype_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.subscriptiontype_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.subscriptiontype_id_seq OWNER TO root;

--
-- Name: subscriptiontype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.subscriptiontype_id_seq OWNED BY public.subscriptiontype.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    name character varying(45) NOT NULL,
    surname character varying(45) NOT NULL,
    patronymic character varying(45),
    birthday timestamp without time zone NOT NULL,
    email character varying(45) NOT NULL,
    phone character varying(45) NOT NULL,
    password character varying(256) NOT NULL,
    "Gender_id" integer NOT NULL,
    "Role_id" integer NOT NULL,
    image character varying,
    bio text
);


ALTER TABLE public."user" OWNER TO root;

--
-- Name: user_has_workouttype; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.user_has_workouttype (
    "User_id" integer NOT NULL,
    "WorkoutType_id" integer NOT NULL
);


ALTER TABLE public.user_has_workouttype OWNER TO root;

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_id_seq OWNER TO root;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- Name: usersubscription; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.usersubscription (
    id integer NOT NULL,
    date_of_purchase timestamp without time zone NOT NULL,
    start_date timestamp without time zone NOT NULL,
    end_date timestamp without time zone NOT NULL,
    "User_id" integer NOT NULL,
    "Subscription_id" integer NOT NULL,
    day_count integer NOT NULL
);


ALTER TABLE public.usersubscription OWNER TO root;

--
-- Name: usersubscription_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.usersubscription_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.usersubscription_id_seq OWNER TO root;

--
-- Name: usersubscription_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.usersubscription_id_seq OWNED BY public.usersubscription.id;


--
-- Name: workout; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.workout (
    id integer NOT NULL,
    name character varying(45) NOT NULL,
    "WorkoutType_id" integer NOT NULL,
    "Trainer" integer NOT NULL,
    start_date timestamp without time zone NOT NULL,
    end_date timestamp without time zone NOT NULL,
    "Gym_id" integer NOT NULL
);


ALTER TABLE public.workout OWNER TO root;

--
-- Name: workout_has_user; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.workout_has_user (
    "Workout_id" integer NOT NULL,
    "User_id" integer NOT NULL
);


ALTER TABLE public.workout_has_user OWNER TO root;

--
-- Name: workout_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.workout_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.workout_id_seq OWNER TO root;

--
-- Name: workout_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.workout_id_seq OWNED BY public.workout.id;


--
-- Name: workouttype; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.workouttype (
    id integer NOT NULL,
    name character varying(45) NOT NULL,
    description text NOT NULL,
    image character varying
);


ALTER TABLE public.workouttype OWNER TO root;

--
-- Name: workouttype_has_subscription; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.workouttype_has_subscription (
    "WorkoutType_id" integer NOT NULL,
    "Subscription_id" integer NOT NULL
);


ALTER TABLE public.workouttype_has_subscription OWNER TO root;

--
-- Name: workouttype_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.workouttype_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.workouttype_id_seq OWNER TO root;

--
-- Name: workouttype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.workouttype_id_seq OWNED BY public.workouttype.id;


--
-- Name: features id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.features ALTER COLUMN id SET DEFAULT nextval('public.features_id_seq'::regclass);


--
-- Name: gender id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.gender ALTER COLUMN id SET DEFAULT nextval('public.gender_id_seq'::regclass);


--
-- Name: gym id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.gym ALTER COLUMN id SET DEFAULT nextval('public.gym_id_seq'::regclass);


--
-- Name: role id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.role ALTER COLUMN id SET DEFAULT nextval('public.role_id_seq'::regclass);


--
-- Name: route id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.route ALTER COLUMN id SET DEFAULT nextval('public.route_id_seq'::regclass);


--
-- Name: subscription id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.subscription ALTER COLUMN id SET DEFAULT nextval('public.subscription_id_seq'::regclass);


--
-- Name: subscriptionduration id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.subscriptionduration ALTER COLUMN id SET DEFAULT nextval('public.subscriptionduration_id_seq'::regclass);


--
-- Name: subscriptiontype id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.subscriptiontype ALTER COLUMN id SET DEFAULT nextval('public.subscriptiontype_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Name: usersubscription id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.usersubscription ALTER COLUMN id SET DEFAULT nextval('public.usersubscription_id_seq'::regclass);


--
-- Name: workout id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.workout ALTER COLUMN id SET DEFAULT nextval('public.workout_id_seq'::regclass);


--
-- Name: workouttype id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.workouttype ALTER COLUMN id SET DEFAULT nextval('public.workouttype_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.alembic_version (version_num) FROM stdin;
08d7c8274058
\.


--
-- Data for Name: features; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.features (id, name) FROM stdin;
\.


--
-- Data for Name: gender; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.gender (id, name) FROM stdin;
1	male
2	female
\.


--
-- Data for Name: gym; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.gym (id, name, address) FROM stdin;
\.


--
-- Data for Name: role; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.role (id, name) FROM stdin;
1	client
2	trainer
3	manager
4	admin
\.


--
-- Data for Name: route; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.route (id, route, name) FROM stdin;
\.


--
-- Data for Name: route_has_role; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.route_has_role ("Route_id", "Role_id") FROM stdin;
\.


--
-- Data for Name: subscription; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.subscription (id, description, is_active, "SubscriptionDuration_id", "SubscriptionType_id") FROM stdin;
\.


--
-- Data for Name: subscription_has_features; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.subscription_has_features ("Subscription_id", "Features_id") FROM stdin;
\.


--
-- Data for Name: subscriptionduration; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.subscriptionduration (id, price, discount) FROM stdin;
\.


--
-- Data for Name: subscriptiontype; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.subscriptiontype (id, name, type) FROM stdin;
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public."user" (id, name, surname, patronymic, birthday, email, phone, password, "Gender_id", "Role_id", image, bio) FROM stdin;
\.


--
-- Data for Name: user_has_workouttype; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.user_has_workouttype ("User_id", "WorkoutType_id") FROM stdin;
\.


--
-- Data for Name: usersubscription; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.usersubscription (id, date_of_purchase, start_date, end_date, "User_id", "Subscription_id", day_count) FROM stdin;
\.


--
-- Data for Name: workout; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.workout (id, name, "WorkoutType_id", "Trainer", start_date, end_date, "Gym_id") FROM stdin;
\.


--
-- Data for Name: workout_has_user; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.workout_has_user ("Workout_id", "User_id") FROM stdin;
\.


--
-- Data for Name: workouttype; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.workouttype (id, name, description, image) FROM stdin;
1	personal	Персональная	\N
\.


--
-- Data for Name: workouttype_has_subscription; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.workouttype_has_subscription ("WorkoutType_id", "Subscription_id") FROM stdin;
\.


--
-- Name: features_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.features_id_seq', 1, false);


--
-- Name: gender_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.gender_id_seq', 2, true);


--
-- Name: gym_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.gym_id_seq', 1, false);


--
-- Name: role_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.role_id_seq', 4, true);


--
-- Name: route_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.route_id_seq', 1, false);


--
-- Name: subscription_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.subscription_id_seq', 1, false);


--
-- Name: subscriptionduration_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.subscriptionduration_id_seq', 1, false);


--
-- Name: subscriptiontype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.subscriptiontype_id_seq', 1, false);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.user_id_seq', 1, true);


--
-- Name: usersubscription_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.usersubscription_id_seq', 1, false);


--
-- Name: workout_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.workout_id_seq', 1, false);


--
-- Name: workouttype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.workouttype_id_seq', 1, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: features features_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.features
    ADD CONSTRAINT features_pkey PRIMARY KEY (id);


--
-- Name: gender gender_name_key; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.gender
    ADD CONSTRAINT gender_name_key UNIQUE (name);


--
-- Name: gender gender_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.gender
    ADD CONSTRAINT gender_pkey PRIMARY KEY (id);


--
-- Name: gym gym_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.gym
    ADD CONSTRAINT gym_pkey PRIMARY KEY (id);


--
-- Name: role role_name_key; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.role
    ADD CONSTRAINT role_name_key UNIQUE (name);


--
-- Name: role role_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.role
    ADD CONSTRAINT role_pkey PRIMARY KEY (id);


--
-- Name: route_has_role route_has_role_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.route_has_role
    ADD CONSTRAINT route_has_role_pkey PRIMARY KEY ("Route_id", "Role_id");


--
-- Name: route route_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.route
    ADD CONSTRAINT route_pkey PRIMARY KEY (id);


--
-- Name: subscription_has_features subscription_has_features_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.subscription_has_features
    ADD CONSTRAINT subscription_has_features_pkey PRIMARY KEY ("Subscription_id", "Features_id");


--
-- Name: subscription subscription_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.subscription
    ADD CONSTRAINT subscription_pkey PRIMARY KEY (id);


--
-- Name: subscriptionduration subscriptionduration_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.subscriptionduration
    ADD CONSTRAINT subscriptionduration_pkey PRIMARY KEY (id);


--
-- Name: subscriptiontype subscriptiontype_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.subscriptiontype
    ADD CONSTRAINT subscriptiontype_pkey PRIMARY KEY (id);


--
-- Name: user user_email_key; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_email_key UNIQUE (email);


--
-- Name: user_has_workouttype user_has_workouttype_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.user_has_workouttype
    ADD CONSTRAINT user_has_workouttype_pkey PRIMARY KEY ("User_id", "WorkoutType_id");


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: usersubscription usersubscription_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.usersubscription
    ADD CONSTRAINT usersubscription_pkey PRIMARY KEY (id);


--
-- Name: workout_has_user workout_has_user_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.workout_has_user
    ADD CONSTRAINT workout_has_user_pkey PRIMARY KEY ("Workout_id", "User_id");


--
-- Name: workout workout_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.workout
    ADD CONSTRAINT workout_pkey PRIMARY KEY (id);


--
-- Name: workouttype_has_subscription workouttype_has_subscription_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.workouttype_has_subscription
    ADD CONSTRAINT workouttype_has_subscription_pkey PRIMARY KEY ("WorkoutType_id", "Subscription_id");


--
-- Name: workouttype workouttype_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.workouttype
    ADD CONSTRAINT workouttype_pkey PRIMARY KEY (id);


--
-- Name: ix_route_has_role_Role_id; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX "ix_route_has_role_Role_id" ON public.route_has_role USING btree ("Role_id");


--
-- Name: ix_route_has_role_Route_id; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX "ix_route_has_role_Route_id" ON public.route_has_role USING btree ("Route_id");


--
-- Name: ix_subscription_SubscriptionDuration_id; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX "ix_subscription_SubscriptionDuration_id" ON public.subscription USING btree ("SubscriptionDuration_id");


--
-- Name: ix_subscription_SubscriptionType_id; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX "ix_subscription_SubscriptionType_id" ON public.subscription USING btree ("SubscriptionType_id");


--
-- Name: ix_subscription_has_features_Features_id; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX "ix_subscription_has_features_Features_id" ON public.subscription_has_features USING btree ("Features_id");


--
-- Name: ix_subscription_has_features_Subscription_id; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX "ix_subscription_has_features_Subscription_id" ON public.subscription_has_features USING btree ("Subscription_id");


--
-- Name: ix_user_Gender_id; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX "ix_user_Gender_id" ON public."user" USING btree ("Gender_id");


--
-- Name: ix_user_Role_id; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX "ix_user_Role_id" ON public."user" USING btree ("Role_id");


--
-- Name: ix_user_has_workouttype_User_id; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX "ix_user_has_workouttype_User_id" ON public.user_has_workouttype USING btree ("User_id");


--
-- Name: ix_user_has_workouttype_WorkoutType_id; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX "ix_user_has_workouttype_WorkoutType_id" ON public.user_has_workouttype USING btree ("WorkoutType_id");


--
-- Name: ix_usersubscription_Subscription_id; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX "ix_usersubscription_Subscription_id" ON public.usersubscription USING btree ("Subscription_id");


--
-- Name: ix_usersubscription_User_id; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX "ix_usersubscription_User_id" ON public.usersubscription USING btree ("User_id");


--
-- Name: ix_workout_Gym_id; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX "ix_workout_Gym_id" ON public.workout USING btree ("Gym_id");


--
-- Name: ix_workout_Trainer; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX "ix_workout_Trainer" ON public.workout USING btree ("Trainer");


--
-- Name: ix_workout_WorkoutType_id; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX "ix_workout_WorkoutType_id" ON public.workout USING btree ("WorkoutType_id");


--
-- Name: ix_workout_has_user_User_id; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX "ix_workout_has_user_User_id" ON public.workout_has_user USING btree ("User_id");


--
-- Name: ix_workout_has_user_Workout_id; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX "ix_workout_has_user_Workout_id" ON public.workout_has_user USING btree ("Workout_id");


--
-- Name: ix_workouttype_has_subscription_Subscription_id; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX "ix_workouttype_has_subscription_Subscription_id" ON public.workouttype_has_subscription USING btree ("Subscription_id");


--
-- Name: ix_workouttype_has_subscription_WorkoutType_id; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX "ix_workouttype_has_subscription_WorkoutType_id" ON public.workouttype_has_subscription USING btree ("WorkoutType_id");


--
-- Name: route_has_role route_has_role_Role_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.route_has_role
    ADD CONSTRAINT "route_has_role_Role_id_fkey" FOREIGN KEY ("Role_id") REFERENCES public.role(id);


--
-- Name: route_has_role route_has_role_Route_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.route_has_role
    ADD CONSTRAINT "route_has_role_Route_id_fkey" FOREIGN KEY ("Route_id") REFERENCES public.route(id);


--
-- Name: subscription subscription_SubscriptionDuration_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.subscription
    ADD CONSTRAINT "subscription_SubscriptionDuration_id_fkey" FOREIGN KEY ("SubscriptionDuration_id") REFERENCES public.subscriptionduration(id);


--
-- Name: subscription subscription_SubscriptionType_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.subscription
    ADD CONSTRAINT "subscription_SubscriptionType_id_fkey" FOREIGN KEY ("SubscriptionType_id") REFERENCES public.subscriptiontype(id);


--
-- Name: subscription_has_features subscription_has_features_Features_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.subscription_has_features
    ADD CONSTRAINT "subscription_has_features_Features_id_fkey" FOREIGN KEY ("Features_id") REFERENCES public.features(id);


--
-- Name: subscription_has_features subscription_has_features_Subscription_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.subscription_has_features
    ADD CONSTRAINT "subscription_has_features_Subscription_id_fkey" FOREIGN KEY ("Subscription_id") REFERENCES public.subscription(id);


--
-- Name: user user_Gender_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT "user_Gender_id_fkey" FOREIGN KEY ("Gender_id") REFERENCES public.gender(id);


--
-- Name: user user_Role_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT "user_Role_id_fkey" FOREIGN KEY ("Role_id") REFERENCES public.role(id);


--
-- Name: user_has_workouttype user_has_workouttype_User_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.user_has_workouttype
    ADD CONSTRAINT "user_has_workouttype_User_id_fkey" FOREIGN KEY ("User_id") REFERENCES public."user"(id);


--
-- Name: user_has_workouttype user_has_workouttype_WorkoutType_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.user_has_workouttype
    ADD CONSTRAINT "user_has_workouttype_WorkoutType_id_fkey" FOREIGN KEY ("WorkoutType_id") REFERENCES public.workouttype(id);


--
-- Name: usersubscription usersubscription_Subscription_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.usersubscription
    ADD CONSTRAINT "usersubscription_Subscription_id_fkey" FOREIGN KEY ("Subscription_id") REFERENCES public.subscription(id);


--
-- Name: usersubscription usersubscription_User_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.usersubscription
    ADD CONSTRAINT "usersubscription_User_id_fkey" FOREIGN KEY ("User_id") REFERENCES public."user"(id);


--
-- Name: workout workout_Gym_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.workout
    ADD CONSTRAINT "workout_Gym_id_fkey" FOREIGN KEY ("Gym_id") REFERENCES public.gym(id);


--
-- Name: workout workout_Trainer_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.workout
    ADD CONSTRAINT "workout_Trainer_fkey" FOREIGN KEY ("Trainer") REFERENCES public."user"(id);


--
-- Name: workout workout_WorkoutType_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.workout
    ADD CONSTRAINT "workout_WorkoutType_id_fkey" FOREIGN KEY ("WorkoutType_id") REFERENCES public.workouttype(id);


--
-- Name: workout_has_user workout_has_user_User_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.workout_has_user
    ADD CONSTRAINT "workout_has_user_User_id_fkey" FOREIGN KEY ("User_id") REFERENCES public."user"(id);


--
-- Name: workout_has_user workout_has_user_Workout_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.workout_has_user
    ADD CONSTRAINT "workout_has_user_Workout_id_fkey" FOREIGN KEY ("Workout_id") REFERENCES public.workout(id);


--
-- Name: workouttype_has_subscription workouttype_has_subscription_Subscription_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.workouttype_has_subscription
    ADD CONSTRAINT "workouttype_has_subscription_Subscription_id_fkey" FOREIGN KEY ("Subscription_id") REFERENCES public.subscription(id);


--
-- Name: workouttype_has_subscription workouttype_has_subscription_WorkoutType_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.workouttype_has_subscription
    ADD CONSTRAINT "workouttype_has_subscription_WorkoutType_id_fkey" FOREIGN KEY ("WorkoutType_id") REFERENCES public.workouttype(id);


--
-- PostgreSQL database dump complete
--

