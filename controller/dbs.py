import os
from pathlib import Path

db_path = Path(
    os.path.abspath(
        os.getenv(
            "CYPHAL_DBS_PATH",
            f'{os.getenv("PROJECT_ROOT", __file__ + "/../../")}/var',
        )
    )
)
