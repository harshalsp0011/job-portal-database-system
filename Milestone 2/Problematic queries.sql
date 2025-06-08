
--. Multi-Skill Filter
-- Find applicants with Python AND SQL skills
SELECT a.name, a.email
FROM applicant a
WHERE EXISTS (
    SELECT 1 FROM applicant_skill aps 
    JOIN skill s ON aps.skill_id = s.skill_id
    WHERE aps.applicant_id = a.applicant_id 
    AND s.skill_name = 'Python'
)
AND EXISTS (
    SELECT 1 FROM applicant_skill aps 
    JOIN skill s ON aps.skill_id = s.skill_id
    WHERE aps.applicant_id = a.applicant_id 
    AND s.skill_name = 'SQL'
);


-- Solution :

CREATE INDEX idx_applicant_skills ON applicant_skill(applicant_id, skill_id);

SELECT a.name, a.email
FROM applicant a
JOIN (
    SELECT applicant_id, array_agg(s.skill_name) AS skills
    FROM applicant_skill aps
    JOIN skill s ON aps.skill_id = s.skill_id
    GROUP BY applicant_id
) AS applicant_skills ON a.applicant_id = applicant_skills.applicant_id
WHERE applicant_skills.skills @> ARRAY['Python', 'SQL']::character varying[];



-- Full scan 
-- Count unique skills per company (expensive aggregation)
SELECT c.name, COUNT(DISTINCT js.skill_id) AS unique_skills
FROM company c
JOIN job j ON c.company_id = j.company_id
JOIN job_skill js ON j.job_id = js.job_id
GROUP BY c.company_id
ORDER BY unique_skills DESC;



-- Solution 

-- Pre-aggregate with a materialized view
CREATE MATERIALIZED VIEW mv_company_skills AS
SELECT c.company_id, COUNT(DISTINCT js.skill_id) AS unique_skills
FROM company c
JOIN job j ON c.company_id = j.company_id
JOIN job_skill js ON j.job_id = js.job_id
GROUP BY c.company_id;

-- 
SELECT c.name, m.unique_skills
FROM company c
JOIN mv_company_skills m ON c.company_id = m.company_id
ORDER BY m.unique_skills DESC;



-- -- Count pending applications per job
SELECT j.job_id, j.title, COUNT(a.status) AS pending_count
FROM job j
LEFT JOIN application a ON j.job_id = a.job_id
WHERE a.status = 'Pending'
GROUP BY j.job_id;


-- solution 

CREATE INDEX idx_pending_apps ON application(job_id)
WHERE status = 'Pending';

SELECT j.job_id, j.title, COUNT(a.status) AS pending_count
FROM job j
LEFT JOIN application a ON j.job_id = a.job_id
WHERE a.status = 'Pending'
GROUP BY j.job_id;
