import pandas as pd
from faker import Faker
import random
from tqdm import tqdm

fake = Faker()

# Generate applicant data
def generate_applicants(num=50000):
    applicants = []
    for i in tqdm(range(1, num + 1), desc="Generating applicants"):
        applicants.append({
            "applicant_id": i,
            "name": fake.name(),
            "email": fake.unique.email(),
            "phone": fake.phone_number()[:15],
            "resume": fake.text(max_nb_chars=200),
            "location": f"{fake.city()}"
        })
    return pd.DataFrame(applicants)

# Generate company data
def generate_companies(num=100):
    industries = ["Technology", "Finance", "Health", "Education", "Retail", "AI", "Consulting", "Logistics",
                  "Construction", "Real Estate", "Manufacturing", "Biotech", "Gaming", "Entertainment", "Legal"]
    companies = []
    for i in tqdm(range(1, num + 1), desc="Generating companies"):
        companies.append({
            "company_id": i,
            "name": fake.company(),
            "industry": random.choice(industries),
            "location": f"{fake.city()}",
            "website": fake.url()
        })
    return pd.DataFrame(companies)

# Generate skill data
def generate_skills():
    skill_names = [
        "Python", "Java", "C++", "JavaScript", "React", "Node.js", "Angular", "Vue.js", "Django", "Flask",
        "SQL", "NoSQL", "MongoDB", "PostgreSQL", "MySQL", "AWS", "Azure", "GCP", "Docker", "Kubernetes",
        "Git", "CI/CD", "Terraform", "Linux", "HTML", "CSS", "SASS", "Swift", "Kotlin", "Flutter",
        "TensorFlow", "PyTorch", "Scikit-learn", "Pandas", "NumPy", "Agile", "Scrum", "JIRA", "Figma", "Photoshop",
        "Tableau", "Power BI", "Excel", "Business Analysis", "Cybersecurity", "Blockchain", "Data Engineering", "Spark", "Hadoop", "Airflow"
    ]
    return pd.DataFrame([{"skill_id": i + 1, "skill_name": name} for i, name in enumerate(skill_names)])

# Generate category data
def generate_categories(num=50):
    base = ["IT", "Finance", "Tech", "Data Science", "Cloud", "AI", "DevOps", "Design", "Marketing", "Sales", "Healthcare", "Legal", "Construction", "Real Estate", "Education"]
    categories = list(set(base + [fake.word().capitalize() for _ in range(num)]))
    return pd.DataFrame([{"category_id": i + 1, "category_name": name} for i, name in enumerate(categories[:num])])

# Generate job data
def generate_jobs(num=50000, max_company_id=100):
    jobs = []
    for i in tqdm(range(1, num + 1), desc="Generating jobs"):
        jobs.append({
            "job_id": i,
            "title": fake.job(),
            "description": fake.text(max_nb_chars=200),
            "location": f"{fake.city()}, {fake.state_abbr()}",
            "salary": str(random.randint(50000, 150000)),
            "posted_date": fake.date_this_year().isoformat(),
            "company_id": random.randint(1, max_company_id)
        })
    return pd.DataFrame(jobs)

# Generate application data
def generate_applications(num=50000, max_applicant=50000, max_job=50000):
    statuses = ["Pending", "Accepted", "Rejected"]
    applications = []
    for i in tqdm(range(1, num + 1), desc="Generating applications"):
        applications.append({
            "application_id": i,
            "applicant_id": random.randint(1, max_applicant),
            "job_id": random.randint(1, max_job),
            "application_date": fake.date_this_year().isoformat(),
            "status": random.choice(statuses)
        })
    return pd.DataFrame(applications)

# Generate job_skill data
def generate_job_skills(num=100000, max_job=50000, max_skill=50):
    job_skills = set()
    while len(job_skills) < num:
        job_skills.add((random.randint(1, max_job), random.randint(1, max_skill)))
    return pd.DataFrame(list(job_skills), columns=["job_id", "skill_id"])

# Generate job_category data
def generate_job_categories(num=100000, max_job=50000, max_category=50):
    job_categories = set()
    while len(job_categories) < num:
        job_categories.add((random.randint(1, max_job), random.randint(1, max_category)))
    return pd.DataFrame(list(job_categories), columns=["job_id", "category_id"])

# Generate applicant_skill data
def generate_applicant_skills(num=100000, max_applicant=50000, max_skill=50):
    applicant_skills = set()
    while len(applicant_skills) < num:
        applicant_skills.add((random.randint(1, max_applicant), random.randint(1, max_skill)))
    return pd.DataFrame(list(applicant_skills), columns=["applicant_id", "skill_id"])


applicants_df = generate_applicants()
companies_df = generate_companies()
skills_df = generate_skills()
categories_df = generate_categories()
jobs_df = generate_jobs(max_company_id=companies_df["company_id"].max())
applications_df = generate_applications()
job_skills_df = generate_job_skills()
job_categories_df = generate_job_categories(max_category=categories_df["category_id"].max())
applicant_skills_df = generate_applicant_skills()


with pd.ExcelWriter("generated_data_updated.xlsx") as writer:
    applicants_df.to_excel(writer, sheet_name="applicant", index=False)
    companies_df.to_excel(writer, sheet_name="company", index=False)
    skills_df.to_excel(writer, sheet_name="skill", index=False)
    categories_df.to_excel(writer, sheet_name="category", index=False)
    jobs_df.to_excel(writer, sheet_name="job", index=False)
    applications_df.to_excel(writer, sheet_name="application", index=False)
    job_skills_df.to_excel(writer, sheet_name="job_skill", index=False)
    job_categories_df.to_excel(writer, sheet_name="job_category", index=False)
    applicant_skills_df.to_excel(writer, sheet_name="applicant_skill", index=False)


