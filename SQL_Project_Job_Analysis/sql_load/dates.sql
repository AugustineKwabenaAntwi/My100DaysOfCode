SELECT
    sum(salary_year_avg) as year_avg,
    sum(salary_hour_avg) as hour_avg,
    job_title_short
FROM job_postings_fact
HAVING job_posted_date > '2023-06-01'
GROUP BY job_title_short

LIMIT 5