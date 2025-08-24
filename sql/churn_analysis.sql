-- 1. Total number of customers
SELECT COUNT(DISTINCT customerID) AS total_customers
FROM telco_churn;

-- 2. Overall churn rate
SELECT 
    ROUND(AVG(Churn) * 100, 2) AS churn_percentage
FROM telco_churn;

-- 3. Churn rate by contract type
SELECT 
    Contract,
    ROUND(AVG(Churn) * 100, 2) AS churn_percentage
FROM telco_churn
GROUP BY Contract
ORDER BY churn_percentage DESC;

-- 4. Average monthly charges for churned vs non-churned customers
SELECT 
    Churn,
    ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charges
FROM telco_churn
GROUP BY Churn;
