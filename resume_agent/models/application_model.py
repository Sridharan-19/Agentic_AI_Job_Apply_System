from dataclasses import dataclass
from datetime import datetime

@dataclass
class Application:

    job_id: int

    status: str

    applied_at: datetime