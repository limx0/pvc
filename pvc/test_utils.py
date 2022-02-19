import pandas as pd
from prefect import flow
from prefect import task

from tests.generate import RESOURCE_DIR


@task
def raw(folder, name):
    return pd.read_csv(RESOURCE_DIR / folder / name)


@task
def process(df: pd.DataFrame, n: int):
    return df * n


@task
def join(dfs):
    return pd.concat(dfs)


# @flow
# def flow1():
#     r = raw()


@flow
def flow1(n: int = 2, folder="source1"):
    results = []
    for i in range(1, 3):
        r = raw(folder=folder, name=f"raw{i}.csv")
        p = process(r, n=n)
        results.append(p)
    return join(results)
