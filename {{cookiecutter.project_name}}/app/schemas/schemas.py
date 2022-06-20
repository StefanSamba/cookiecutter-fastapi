from typing import List

from pydantic import BaseModel


class Request(BaseModel):
    utterances: List[dict] = [
        {"text": "Hi, this is just an example string"},
        {"text": "This is a second example string"},
    ]
