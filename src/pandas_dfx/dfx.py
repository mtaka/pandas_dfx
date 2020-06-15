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


#----------------------------------------------------------------------------
def dfs_gb(df, scols, sep=' '):
    """DataFrameを指定した文字列でグループ化。区切り文字の既定値は空白

    Args:
        df (DataFrame): グループ化する対象
        scols (str): グループ化する列名を文字列でして
        sep (str, optional): 区切り文字. Defaults to ' '.

    Returns:
        Groupby: グループ化オブジェクト
    """
    return df.groupby(scols.split())
DataFrame.s_gb = dfs_gb


#----------------------------------------------------------------------------
def dfs_gagg(df, gstr, vstr, f='sum'):
    """グループ化する項目と、集計項目を文字列で渡すグループ化関数

    Args:
        df (DataFrame): 対象DataFrame
        gstr (str): グループ化する項目のリストを文字列で指定
        vstr (str): 集計項目のリストを文字列で指定
        f (function/str, optional): グループ化集計関数名. Defaults to 'sum'.

    Returns:
        DataFrame: 集計結果
    """
    #return df.groupby(gstr.split())[vstr.split()].agg(f)
    return df.s_gb(gstr)[vstr.split()].agg(f)
DataFrame.s_gagg = dfs_gagg

# def dfs_gapp(df, gstr, vstr, fapp):
#     return df.groupby(gstr.split())[vstr.split()].app(fapp)
# DataFrame.x_sgapp = dfs_gapp