import pandas as pd

from src.reports import spending_by_category


def test_spending_by_category(sample_df, df_by_category) -> None:
    pd.testing.assert_frame_equal(spending_by_category(sample_df, "Переводы", date="31.10.2024"), df_by_category)
