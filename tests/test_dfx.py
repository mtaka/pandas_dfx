import pytest
from pkg import *
import sys

def test_df():
    str = """cls,gen,math,eng,jap
    A,F,40,60,70
    A,F,50,70,60
    A,M,60,80,50
    A,M,70,90,90
    B,F,80,90,70
    B,F,65,80,60
    B,M,75,70,80
    B,M,95,60,50
    """

    df = df_from_text(str,sep=',')
    assert type(df), "DataFrame"
    assert len(df), 8
    assert list(df.columns), 'cls gen math eng jap'.split()

