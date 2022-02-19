import os
import pathlib

import pytest

from tests.generate import RESOURCE_DIR


@pytest.fixture(autouse=True)
def reset_db():
    db_path = pathlib.Path(f"sqlite://{RESOURCE_DIR}/orion.db")
    os.environ["PREFECT_ORION_DATABASE_CONNECTION_URL"] = str(db_path)
    if db_path.exists():
        db_path.unlink()
