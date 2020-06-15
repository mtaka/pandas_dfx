import pandas as pd
from pandas import DataFrame, Series

#----------------------------------------------------------------------------
def df_from_text(src, **kwargs):
    """テキストからDataFrameを生成。pd.read_tableの省略形
    Args:
        src (str): タブ区切りのデータ
    Returns:
        DataFrame: パーズ結果のDataFrameを生成
    """
    import io
    return pd.read_table(io.StringIO(src), **kwargs)
