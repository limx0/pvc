import pathlib
import string

import numpy as np
import pandas as pd


RESOURCE_DIR = pathlib.Path(__file__).parent.joinpath("resources").resolve()


def generate_test_data(folder, name, shape=(3, 3)):
    df = pd.DataFrame(
        data=np.random.random(shape),
        columns=list(string.ascii_uppercase[: shape[1]]),
    )
    RESOURCE_DIR.joinpath(folder).mkdir(exist_ok=True)
    with open(f"{RESOURCE_DIR}/{folder}/{name}.csv", "wb") as f:
        df.to_csv(f)


if __name__ == "__main__":
    for i in range(1, 4):
        generate_test_data("source1", f"raw{i}", (3, 3))
