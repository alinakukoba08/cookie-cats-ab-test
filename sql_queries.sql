-- Check data balance
SELECT version, COUNT(*) 
FROM cookie_cats
GROUP BY version;

-- Retention rates
SELECT 
    version,
    AVG(retention_1) AS day1_retention,
    AVG(retention_7) AS day7_retention
FROM cookie_cats
GROUP BY version;

-- Engagement
SELECT 
    version,
    AVG(sum_gamerounds) AS avg_rounds
FROM cookie_cats
GROUP BY version;
