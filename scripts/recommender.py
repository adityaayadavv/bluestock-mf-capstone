import pandas as pd

perf = pd.read_csv(
    "clean_performance.csv"
)

def recommend_funds(risk_level):

    risk_map = {
        'Low': ['Liquid','Short Duration','Gilt'],

        'Moderate': [
            'Large Cap',
            'Flexi Cap',
            'Value',
            'Index',
            'Index/ETF',
            'Large & Mid Cap'
        ],

        'High': [
            'Mid Cap',
            'Small Cap',
            'ELSS'
        ]
    }

    filtered = perf[
        perf['category'].isin(
            risk_map[risk_level]
        )
    ]

    return (
        filtered
        .sort_values(
            'sharpe_ratio',
            ascending=False
        )
        [
            [
                'scheme_name',
                'category',
                'sharpe_ratio'
            ]
        ]
        .head(3)
    )