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

#----------------------------------------------------------------------------
def dfs_cols(df, scols, sep=' '):
    """リストの代わりに文字列で指定した列を取り出す。デフォルトの区切り文字は空白

    Args:
        df (DataFrame): 対象
        scols (str): 列を指定する文字列
        sep (str, optional): 区切り文字. Defaults to ' '.

    Returns:
        DataFrame: 文字列で指定したサブセット
    """

    return df[scols.split(sep)]

DataFrame.s_cols = dfs_cols

#----------------------------------------------------------------------------
def dfm_colsas(df, repmap):
    """指定した辞書で列名を置き換え。rename(columns={})の短縮

    Args:
        df (DataFrame): 置き換え対象
        repmap (dictionary): 列名のマップ

    Returns:
        DataFrame: 列名置き換え結果
    """
    return df.rename(columns=repmap)

DataFrame.m_colsas = dfm_colsas

#----------------------------------------------------------------------------
def dfs_colsas(df, scols, sep=' '):
    """DataFrameの列名をリストの代わりに文字列で指定して置き換え。デフォルトの区切り文字は空白

    Args:
        df (DataFrame): 対象
        scols (str): [description]
        sep (str, optional): 区切り文字. Defaults to ' '.

    Returns:
        DataFrame: 列名置き換え結果
    """
    df.columns = scols.split(sep)
    return df

DataFrame.s_colsas = dfs_colsas