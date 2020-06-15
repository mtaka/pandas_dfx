import pytest
from pkg import *
import sys

@pytest.fixture
def text1(scope='module'):
    return """cls,gen,math,en,jp
A,F,40,60,70
A,F,50,70,60
A,M,60,80,50
A,M,70,90,90
B,F,80,90,70
B,F,65,80,60
B,M,75,70,80
B,M,95,60,50
    """
@pytest.fixture
def df1(text1, scope='module'):
    return df_from_text(text1, sep=',')

def test_from_text(text1):
    df = df_from_text(text1, sep=',')
    assert type(df), "DataFrame"
    assert len(df), 8
    assert list(df.columns), 'cls gen math en jp'.split()

def test_df_1(df1):
    assert len(df1), 8
    assert list(df1.columns), 'cls gen math en jp'.split()

def test_dfs_cols(df1):
    df11 = dfs_cols(df1, 'gen en jp')
    assert list(df11.columns), 'gen en jp'.split()
    df12 = dfs_cols(df1, 'cls;jp;math', sep=';')
    assert list(df12.columns), 'cls jp math'.split()
    df13 = df1.s_cols('cls gen jp')
    assert list(df13.columns), 'cls gen jp'.split()

def test_dfm_colsas(df1):
    df11 = dfm_colsas(df1, {'cls': 'CLS', 'en': 'E', 'math': 'M', 'jp': 'J'})
    assert list(df11.columns), 'CLS gen E M J'.split()
    df12 = df1.m_colsas({'jp': 'JAP', 'gen': 'Gen'})
    assert list(df11.columns), 'cls Gen en math JAP'.split()

def test_dfs_colsas(df1):
    df11 = dfs_colsas(df1, 'C G M E J')
    assert list(df11.columns), 'C G M E J'.split()
    df12 = df1.s_colsas('C;G;M;E;J', sep=';')
    assert list(df12.columns), 'C G M E J'.split()


def test_dfs_gb(df1):
    gb = dfs_gb(df1, 'cls gen')
    assert str(gb), 'DataFrameGroupBy'
    df11 = gb['math'].sum()
    assert len(df11), 4
    df12 = df1.s_gb('cls')['en'].mean()
    assert len(df12), 2

def test_dfs_gagg(df1):
    df11 = dfs_gagg(df1, 'cls gen', 'math en jp')
    assert list(df11.columns), 'math en jp'.split()
    assert list(df11.index), [('A','F'), ('A','M'),('B','F'),('B',M)]

    df12 = df1.s_gagg('cls gen', 'math en jp', 'mean')
    df13 = df1.groupby(['cls', 'gen'])['en', 'jp'].mean()
    assert list(df12['en']), list(df3['en'])


