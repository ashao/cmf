from typing import Sequence

import pandas as pd
from pydantic import BaseModel, HttpUrl


class ExecutionDataFrame(BaseModel):
    context_id: str
    context_type: str
    execution: str
