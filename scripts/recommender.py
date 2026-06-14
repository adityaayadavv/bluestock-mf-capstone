"""
Fund Recommendation Engine

Author: Aditya Yadav
Project: Bluestock Mutual Fund Analytics Platform

Description:
Implements a rule-based mutual fund recommendation
system using fund category, risk profile, and
risk-adjusted performance metrics.
"""

import pandas as pd

PERF = pd.read_csv(
    "clean_performance.csv"
)


def recommend_funds(risk_level):
    """
    Recommends the top 3 mutual funds based on
    risk profile and Sharpe Ratio.

    Args:
        risk_level (str):
            One of ['Low', 'Moderate', 'High']

    Returns:
        pandas.DataFrame:
            Top 3 recommended funds.
    """

    risk_map = {
        "Low": [
            "Liquid",
            "Short Duration",
            "Gilt",
        ],
        "Moderate": [
            "Large Cap",
            "Flexi Cap",
            "Value",
            "Index",
            "Index/ETF",
            "Large & Mid Cap",
        ],
        "High": [
            "Mid Cap",
            "Small Cap",
            "ELSS",
        ],
    }

    if risk_level not in risk_map:
        raise ValueError(
            "Risk level must be one of: "
            "Low, Moderate, High"
        )

    filtered = PERF[
        PERF["category"].isin(
            risk_map[risk_level]
        )
    ]

    recommendations = (
        filtered
        .sort_values(
            "sharpe_ratio",
            ascending=False
        )
        [
            [
                "scheme_name",
                "category",
                "sharpe_ratio",
            ]
        ]
        .head(3)
    )

    return recommendations