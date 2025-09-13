from pydantic import BaseModel


class Diff(BaseModel):
    before: str
    after: str
    tag: str  # "insert", "delete" or "replace"
