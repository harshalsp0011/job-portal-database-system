import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL Database Credentials
db_username = "postgres"
db_password = "121201"
db_host = "localhost"
db_port = "5432"
db_name = "job_db"

#  connection to PostgreSQL
engine = create_engine(f"postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}")

# Load Excel file
file_path = "generated_data.xlsx"
xls = pd.ExcelFile(file_path)


df_applicants = pd.read_excel(xls, sheet_name="applicant")
df_companies = pd.read_excel(xls, sheet_name="company")
df_skills = pd.read_excel(xls, sheet_name="skill")
df_categories = pd.read_excel(xls, sheet_name="category")
df_jobs = pd.read_excel(xls, sheet_name="job")
df_applications = pd.read_excel(xls, sheet_name="application")
df_job_skills = pd.read_excel(xls, sheet_name="job_skill")
df_job_categories = pd.read_excel(xls, sheet_name="job_category")
df_applicant_skills = pd.read_excel(xls, sheet_name="applicant_skill")  

# Insert data into PostgreSQL tables
df_applicants.to_sql("applicant", con=engine, if_exists="append", index=False)
df_companies.to_sql("company", con=engine, if_exists="append", index=False)
df_skills.to_sql("skill", con=engine, if_exists="append", index=False)
df_categories.to_sql("category", con=engine, if_exists="append", index=False)
df_jobs.to_sql("job", con=engine, if_exists="append", index=False)
df_applications.to_sql("application", con=engine, if_exists="append", index=False)
df_job_skills.to_sql("job_skill", con=engine, if_exists="append", index=False)
df_job_categories.to_sql("job_category", con=engine, if_exists="append", index=False)
df_applicant_skills.to_sql("applicant_skill", con=engine, if_exists="append", index=False)  

