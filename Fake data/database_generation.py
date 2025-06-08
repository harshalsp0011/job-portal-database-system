import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Function to generate applicant data
def generate_applicants(num=10):
    applicants = []
    for i in range(1, num + 1):
        applicant = {
            "applicant_id": i,
            "name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number()[:15],
            "resume": fake.text(max_nb_chars=200),
            "location": fake.city() + ", " + fake.state_abbr()
        }
        applicants.append(applicant)
    return pd.DataFrame(applicants)

# Function to generate company data
def generate_companies(num=10):
    companies = []
    industries = ["Technology", "Data Science", "Web Development", "Cloud Computing", "Artificial Intelligence", 
                 "UI/UX Design", "DevOps", "Mobile Development", "Product Management", "Finance"]
    for i in range(1, num + 1):
        company = {
            "company_id": i,
            "name": fake.company(),
            "industry": random.choice(industries),
            "location": fake.city() + ", " + fake.state_abbr(),
            "website": fake.url()
        }
        companies.append(company)
    return pd.DataFrame(companies)

# Function to generate skill data
def generate_skills(num=10):
    skills = []
    skill_names = ["Python", "SQL", "React", "Node.js", "AWS", "Docker", "Flutter", "Azure", "Agile", "Machine Learning"]
    for i in range(1, num + 1):
        skill = {
            "skill_id": i,
            "skill_name": skill_names[i - 1]
        }
        skills.append(skill)
    return pd.DataFrame(skills)

# Function to generate category data
def generate_categories(num=10):
    categories = []
    category_names = ["IT", "Finance", "Tech", "Data Science", "Web Development", "Cloud Computing", 
                      "Artificial Intelligence", "UI/UX Design", "DevOps", "Mobile Development"]
    for i in range(1, num + 1):
        category = {
            "category_id": i,
            "category_name": category_names[i - 1]
        }
        categories.append(category)
    return pd.DataFrame(categories)

# Function to generate job data
def generate_jobs(num=10):
    jobs = []
    for i in range(1, num + 1):
        job = {
            "job_id": i,
            "title": fake.job(),
            "description": fake.text(max_nb_chars=200),
            "location": fake.city() + ", " + fake.state_abbr(),
            "salary": f"${random.randint(50000, 150000)}",
            "posted_date": fake.date_this_year().isoformat(),
            "company_id": random.randint(1, 10)
        }
        jobs.append(job)
    return pd.DataFrame(jobs)

# Function to generate application data
def generate_applications(num=10):
    applications = []
    statuses = ["Pending", "Accepted", "Rejected"]
    for i in range(1, num + 1):
        application = {
            "application_id": i,
            "applicant_id": random.randint(1, 10),
            "job_id": random.randint(1, 10),
            "application_date": fake.date_this_year().isoformat(),
            "status": random.choice(statuses)
        }
        applications.append(application)
    return pd.DataFrame(applications)

# Function to generate job_skill data
def generate_job_skills(num=10):
    job_skills = []
    for i in range(1, num + 1):
        job_skill = {
            "job_id": i,
            "skill_id": random.randint(1, 10)
        }
        job_skills.append(job_skill)
    return pd.DataFrame(job_skills)

# Function to generate job_category data
def generate_job_categories(num=10):
    job_categories = []
    for i in range(1, num + 1):
        job_category = {
            "job_id": i,
            "category_id": random.randint(1, 10)
        }
        job_categories.append(job_category)
    return pd.DataFrame(job_categories)

# Generate all datasets
applicants_df = generate_applicants()
companies_df = generate_companies()
skills_df = generate_skills()
categories_df = generate_categories()
jobs_df = generate_jobs()
applications_df = generate_applications()
job_skills_df = generate_job_skills()
job_categories_df = generate_job_categories()

# Save datasets to Excel files
with pd.ExcelWriter("generated_data.xlsx") as writer:
    applicants_df.to_excel(writer, sheet_name="applicants", index=False)
    companies_df.to_excel(writer, sheet_name="companies", index=False)
    skills_df.to_excel(writer, sheet_name="skills", index=False)
    categories_df.to_excel(writer, sheet_name="categories", index=False)
    jobs_df.to_excel(writer, sheet_name="jobs", index=False)
    applications_df.to_excel(writer, sheet_name="applications", index=False)
    job_skills_df.to_excel(writer, sheet_name="job_skills", index=False)
    job_categories_df.to_excel(writer, sheet_name="job_categories", index=False)

print("Data generation complete! Excel file saved as 'generated_data.xlsx'.")