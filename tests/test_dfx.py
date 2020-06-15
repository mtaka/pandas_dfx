import pytest
from pkg import *
import sys

@pytest.fixture
def text1():
    return """cls,gen,math,eng,jap
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
def df1(text1):
    return df_from_text(text1, sep=',')

def test_from_text(text1):
    df = df_from_text(text1, sep=',')
    assert type(df), "DataFrame"
    assert len(df), 8
    assert list(df.columns), 'cls gen math eng jap'.split()

def test_df_1(df1):
    assert len(df1), 8
    assert list(df1.columns), 'cls gen math eng jap'.split()

def test_dfs_cols(df1):
    df11 = dfs_cols(df1, 'gen eng jap')
    assert list(df11.columns), 'gen eng jap'.split()
    df12 = dfs_cols(df1, 'cls;jap;math', sep=';')
    assert list(df12.columns), 'cls jap math'.split()
    df13 = df1.s_cols('cls gen jap')
    assert list(df13.columns), 'cls gen jap'.split()

def test_dfm_colsas(df1):
    df11 = dfm_colsas(df1, {'cls': 'CLS', 'eng': 'E', 'math': 'M', 'jap': 'J'})
    assert list(df11.columns), 'CLS gen E M J'.split()
    df12 = df1.m_colsas({'jap': 'JAP', 'gen': 'Gen'})
    assert list(df11.columns), 'cls Gen eng math JAP'.split()

def test_dfs_colsas(df1):
    df11 = dfs_colsas(df1, 'C G M E J')
    assert list(df11.columns), 'C G M E J'.split()
    df12 = df1.s_colsas('C;G;M;E;J', sep=';')
    assert list(df12.columns), 'C G M E J'.split()
