from pydantic import BaseModel


class Job(BaseModel):
    company: str
    position: str
    status: str

jobs = []

