CREATE TABLE dim_fund (
    amfi_code BIGINT PRIMARY KEY,
    fund_house VARCHAR(100),
    scheme_name VARCHAR(255),
    category VARCHAR(50),
    sub_category VARCHAR(100),
    plan VARCHAR(50),
    launch_date DATE,
    benchmark VARCHAR(150),
    expense_ratio_pct NUMERIC(6,2),
    exit_load_pct NUMERIC(6,2),
    min_sip_amount NUMERIC(12,2),
    min_lumpsum_amount NUMERIC(12,2),
    fund_manager VARCHAR(100),
    risk_category VARCHAR(50),
    sebi_category_code VARCHAR(20)
);

CREATE TABLE fact_nav (
    id BIGSERIAL PRIMARY KEY,
    amfi_code BIGINT REFERENCES dim_fund(amfi_code),
    nav_date DATE,
    nav NUMERIC(12,4)
);

CREATE TABLE fact_aum (
    id BIGSERIAL PRIMARY KEY,
    report_date DATE,
    fund_house VARCHAR(100),
    aum_lakh_crore NUMERIC(18,2),
    aum_crore NUMERIC(18,2),
    num_schemes INTEGER
);

CREATE TABLE fact_sip_industry (
    id BIGSERIAL PRIMARY KEY,
    month VARCHAR(10),
    sip_inflow_crore NUMERIC(18,2),
    active_sip_accounts_crore NUMERIC(18,2),
    new_sip_accounts_lakh NUMERIC(18,2),
    sip_aum_lakh_crore NUMERIC(18,2),
    yoy_growth_pct NUMERIC(10,2)
);

CREATE TABLE fact_performance (
    id BIGSERIAL PRIMARY KEY,
    amfi_code BIGINT REFERENCES dim_fund(amfi_code),
    return_1yr_pct NUMERIC(10,2),
    return_3yr_pct NUMERIC(10,2),
    return_5yr_pct NUMERIC(10,2),
    benchmark_3yr_pct NUMERIC(10,2),
    alpha NUMERIC(10,4),
    beta NUMERIC(10,4),
    sharpe_ratio NUMERIC(10,4),
    sortino_ratio NUMERIC(10,4),
    std_dev_ann_pct NUMERIC(10,2),
    max_drawdown_pct NUMERIC(10,2),
    aum_crore NUMERIC(18,2),
    expense_ratio_pct NUMERIC(10,2),
    morningstar_rating INTEGER,
    risk_grade VARCHAR(20)
);

CREATE TABLE fact_transactions (
    id BIGSERIAL PRIMARY KEY,
    investor_id VARCHAR(30),
    transaction_date DATE,
    amfi_code BIGINT REFERENCES dim_fund(amfi_code),
    transaction_type VARCHAR(50),
    amount_inr NUMERIC(18,2),
    state VARCHAR(100),
    city VARCHAR(100),
    city_tier VARCHAR(20),
    age_group VARCHAR(20),
    gender VARCHAR(20),
    annual_income_lakh NUMERIC(10,2),
    payment_mode VARCHAR(50),
    kyc_status VARCHAR(50)
);

CREATE TABLE fact_portfolio (
    id BIGSERIAL PRIMARY KEY,
    amfi_code BIGINT REFERENCES dim_fund(amfi_code),
    stock_symbol VARCHAR(50),
    stock_name VARCHAR(200),
    sector VARCHAR(100),
    weight_pct NUMERIC(10,4),
    market_value_cr NUMERIC(18,2),
    current_price_inr NUMERIC(18,2),
    portfolio_date DATE
);