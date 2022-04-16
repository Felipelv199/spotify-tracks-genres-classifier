import pandas as pd
from pathlib import Path


class PandasUtils():
    def save_df_as_csv(df: pd.DataFrame, path: str):
        filepath = Path(path)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(filepath, index=False)
