-- Drop and recreate public schema
DROP SCHEMA IF EXISTS public CASCADE;
CREATE SCHEMA public AUTHORIZATION pg_database_owner;
COMMENT ON SCHEMA public IS 'standard public schema';

-- Sequences
CREATE SEQUENCE public.orderdetails_order_detail_id_seq MINVALUE 0 NO MAXVALUE START 0 NO CYCLE;
CREATE SEQUENCE public.orders_order_id_seq MINVALUE 0 NO MAXVALUE START 0 NO CYCLE;
CREATE SEQUENCE public.persons_person_id_seq MINVALUE 0 NO MAXVALUE START 0 NO CYCLE;
CREATE SEQUENCE public.products_product_id_seq MINVALUE 0 NO MAXVALUE START 0 NO CYCLE;
CREATE SEQUENCE public.users_user_id_seq MINVALUE 0 NO MAXVALUE START 0 NO CYCLE;

-- Table: applicant
CREATE TABLE public.applicant (
	applicant_id serial PRIMARY KEY,
	"name" varchar(100) NOT NULL,
	email varchar(100) NOT NULL UNIQUE,
	phone varchar(15),
	resume text,
	"location" varchar(100)
);
COMMENT ON COLUMN public.applicant."name" IS 'Full Name';
COMMENT ON COLUMN public.applicant.email IS 'Email address';
COMMENT ON COLUMN public.applicant.phone IS 'Mobile No';
COMMENT ON COLUMN public.applicant.resume IS 'summary of the applicant';
COMMENT ON COLUMN public.applicant."location" IS 'Location of the applicant';

-- Table: company
CREATE TABLE public.company (
	company_id serial PRIMARY KEY,
	"name" varchar(100) NOT NULL,
	industry varchar(100),
	"location" varchar(100),
	website varchar(100)
);
COMMENT ON COLUMN public.company.company_id IS 'Unique pk  for each company';
COMMENT ON COLUMN public.company."name" IS 'Name of the company';
COMMENT ON COLUMN public.company.industry IS 'Type of industry';
COMMENT ON COLUMN public.company."location" IS 'Location of the company';
COMMENT ON COLUMN public.company.website IS 'Website';

-- Table: skill
CREATE TABLE public.skill (
	skill_id serial PRIMARY KEY,
	skill_name varchar(100) NOT NULL
);
COMMENT ON COLUMN public.skill.skill_id IS 'Unique ID for skill';
COMMENT ON COLUMN public.skill.skill_name IS 'Name of the skills (Python, SQL)';

-- Table: category
CREATE TABLE public.category (
	category_id serial PRIMARY KEY,
	category_name varchar(100) NOT NULL
);
COMMENT ON TABLE public.category IS 'categories for jobs';
COMMENT ON COLUMN public.category.category_id IS 'Unique ID for each category/type of company';
COMMENT ON COLUMN public.category.category_name IS 'Name of the category ( IT, Finance, Tech etc )';

-- Table: job
CREATE TABLE public.job (
	job_id serial PRIMARY KEY,
	title varchar(100) NOT NULL,
	description text,
	"location" varchar(100),
	salary varchar(100),
	posted_date date,
	company_id int,
	FOREIGN KEY (company_id) REFERENCES public.company(company_id)
);
COMMENT ON COLUMN public.job.job_id IS 'job pk for each job post';
COMMENT ON COLUMN public.job.title IS 'Title of the job posting';
COMMENT ON COLUMN public.job.description IS 'Description of job';
COMMENT ON COLUMN public.job."location" IS 'Location of the job';
COMMENT ON COLUMN public.job.salary IS 'Salary offered';
COMMENT ON COLUMN public.job.posted_date IS 'Date the job was posted';

-- Table: application
CREATE TABLE public.application (
	application_id serial PRIMARY KEY,
	applicant_id int,
	job_id int,
	application_date date,
	status varchar(20),
	FOREIGN KEY (applicant_id) REFERENCES public.applicant(applicant_id),
	FOREIGN KEY (job_id) REFERENCES public.job(job_id)
);
COMMENT ON COLUMN public.application.application_id IS 'Unique ID for each application done';
COMMENT ON COLUMN public.application.applicant_id IS 'ID of the applicant';
COMMENT ON COLUMN public.application.job_id IS 'ID of the job applied';
COMMENT ON COLUMN public.application.application_date IS 'Date the application';
COMMENT ON COLUMN public.application.status IS 'Status of the application : Pending, Accepted, Rejected';

-- Table: job_skill
CREATE TABLE public.job_skill (
	job_id int,
	skill_id int,
	FOREIGN KEY (job_id) REFERENCES public.job(job_id),
	FOREIGN KEY (skill_id) REFERENCES public.skill(skill_id)
);
COMMENT ON COLUMN public.job_skill.job_id IS 'ID of the job';
COMMENT ON COLUMN public.job_skill.skill_id IS 'ID of the skill required';

-- Table: job_category
CREATE TABLE public.job_category (
	job_id int,
	category_id int,
	FOREIGN KEY (job_id) REFERENCES public.job(job_id),
	FOREIGN KEY (category_id) REFERENCES public.category(category_id)
);
COMMENT ON TABLE public.job_category IS 'posted job and its category';
COMMENT ON COLUMN public.job_category.job_id IS 'Id of job';
COMMENT ON COLUMN public.job_category.category_id IS 'ID of the category';

-- Table: applicant_skill
CREATE TABLE public.applicant_skill (
	applicant_id INT NOT NULL,
	skill_id INT NOT NULL,
	PRIMARY KEY (applicant_id, skill_id),
	FOREIGN KEY (applicant_id) REFERENCES public.applicant(applicant_id),
	FOREIGN KEY (skill_id) REFERENCES public.skill(skill_id)
);
COMMENT ON TABLE public.applicant_skill IS 'Linking applicants to their acquired skills';
COMMENT ON COLUMN public.applicant_skill.applicant_id IS 'A foreign key referencing Applicant table';
COMMENT ON COLUMN public.applicant_skill.skill_id IS 'A foreign key referencing Skill table';