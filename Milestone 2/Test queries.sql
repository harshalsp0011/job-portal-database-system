--Complex JOIN with GROUP BY 
-- Count applications per job category
SELECT c.category_name, COUNT(a.application_id) AS application_count
FROM category c
JOIN job_category jc ON c.category_id = jc.category_id
JOIN job j ON jc.job_id = j.job_id
LEFT JOIN application a ON j.job_id = a.job_id
GROUP BY c.category_name
ORDER BY application_count DESC;


--	Subquery (High-Paying Jobs)
-- Jobs paying above average salary
SELECT j.title, c.name AS company, j.salary
FROM job j
JOIN company c ON j.company_id = c.company_id
WHERE j.salary::numeric > (
    SELECT AVG(salary::numeric) FROM job
)
ORDER BY j.salary::numeric DESC;


--Rank applicants by number of skills
SELECT a.name, a.email, 
       COUNT(ak.skill_id) AS skill_count,
       RANK() OVER (ORDER BY COUNT(ak.skill_id) DESC) AS applicant_rank
FROM applicant a
LEFT JOIN applicant_skill ak ON a.applicant_id = ak.applicant_id
GROUP BY a.applicant_id
LIMIT 100;

--Insert 

--New Job Posting
-- Add new job with associated skills
WITH new_job AS (
  INSERT INTO job(title, description, location, salary, posted_date, company_id)
  VALUES ('Data Scientist', 'Analyze large datasets...', 'Remote', '120000', CURRENT_DATE, 15)
  RETURNING job_id
)
INSERT INTO job_skill(job_id, skill_id)
SELECT nj.job_id, s.skill_id 
FROM new_job nj, skill s
WHERE s.skill_name IN ('Python', 'Machine Learning', 'SQL');

--Add New Company
INSERT INTO company(name, industry, location, website)
VALUES ('Tech Innovations', 'IT', 'San Francisco', 'techinnov.com')
RETURNING company_id;



--UPDATE Operations

-- Batch update application statuses
UPDATE application
SET status = 'Rejected'
WHERE job_id IN (
  SELECT job_id FROM job 
  WHERE posted_date < CURRENT_DATE - INTERVAL '90 days'
)
AND status = 'Pending';


--Salary Adjustment
UPDATE job
SET salary = salary::numeric * 1.05  -- 5% raise
WHERE company_id = 15
AND posted_date > CURRENT_DATE - INTERVAL '1 year';


-- DELETE Operations


--First delete related skills for those applicants   (combine run )
DELETE FROM applicant_skill
WHERE applicant_id IN (
  SELECT a.applicant_id
  FROM applicant a
  LEFT JOIN application ap ON a.applicant_id = ap.applicant_id
  GROUP BY a.applicant_id
  HAVING MAX(ap.application_date) < CURRENT_DATE - INTERVAL '2 years'
     OR MAX(ap.application_date) IS NULL
);

-- Then delete those applicants
DELETE FROM applicant
WHERE applicant_id IN (
  SELECT a.applicant_id
  FROM applicant a
  LEFT JOIN application ap ON a.applicant_id = ap.applicant_id
  GROUP BY a.applicant_id
  HAVING MAX(ap.application_date) < CURRENT_DATE - INTERVAL '2 years'
     OR MAX(ap.application_date) IS NULL
);


