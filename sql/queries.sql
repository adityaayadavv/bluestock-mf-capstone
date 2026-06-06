-- 1. Top 10 Funds by 5-Year Return

SELECT
    amfi_code,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;


-- 2. Top 10 Funds by Sharpe Ratio

SELECT
    amfi_code,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;


-- 3. Funds with Highest AUM

SELECT
    amfi_code,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 10;


-- 4. Average Returns by Risk Grade

SELECT
    risk_grade,
    AVG(return_3yr_pct) AS avg_return
FROM fact_performance
GROUP BY risk_grade
ORDER BY avg_return DESC;


-- 5. Monthly SIP Trend

SELECT
    month,
    sip_inflow_crore
FROM fact_sip_industry
ORDER BY month;


-- 6. Top Fund Houses by AUM

SELECT
    fund_house,
    MAX(aum_crore) AS max_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY max_aum DESC;


-- 7. Transaction Volume by State

SELECT
    state,
    COUNT(*) AS transactions
FROM fact_transactions
GROUP BY state
ORDER BY transactions DESC;


-- 8. Investment Amount by Transaction Type

SELECT
    transaction_type,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;


-- 9. Top Portfolio Sectors

SELECT
    sector,
    SUM(weight_pct) AS total_weight
FROM fact_portfolio
GROUP BY sector
ORDER BY total_weight DESC;


-- 10. Average NAV by Fund

SELECT
    amfi_code,
    AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY avg_nav DESC;