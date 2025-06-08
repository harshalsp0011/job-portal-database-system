Job Portal Database System - Team 17

SETUP INSTRUCTIONS

1. Database Initialization:
   Run this command to create all tables, indexes and constraints:
   psql -U [your_username] -h [host] -d [database_name] -f create.sql

   Alternatively, you can copy these essential schema queries:

2. Data Generation & Loading:
   python generate.py  (creates fake data CSV files)
   python load.py     (imports data to PostgreSQL)


3. Web Interface:
   pip install streamlit
   streamlit run app.py
   Access at http://localhost:8501

REQUIREMENTS:
- PostgreSQL 14+
- Python 3.8+ with:
  pip install psycopg2-binary pandas faker sqlalchemy streamlit

FILES:
- create.sql  : Schema with tables, indexes, constraints
- generate.py : Creates fake applicant/job data using Faker
- load.py     : Loads CSV data into PostgreSQL (edit DB config)
- app.py      : Streamlit web interface

DATA SOURCES:
- All data is programmatically generated using Python Faker
- No external datasets were used
- Includes realistic distributions for:
  * Applicant profiles (200+ records)
  * Job postings (100+ listings)
  * Skills mapping (50+ unique skills)

CONFIGURATION:
Edit load.py with your credentials:
DB_CONFIG = {
    'host': 'localhost',
    'database': 'job_portal',
    'user': 'postgres',
    'password': 'your_password'
}

KEY FEATURES:
- Optimized indexes for fast searches
- BCNF-normalized schema
- Scalable fake data generation

WEB INTERFACE FEATURES:
- Interactive query builder
- Visualizations of job/applicant data
- Real-time application tracking
- Skill matching dashboard

TEAM:
- Harshal Sanjiv Patil (hpatil2)
- Prathamesh Kishor Gadgil (pgadgil)