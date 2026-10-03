from pydantic import BaseModel
class Postcreate(BaseModel):
    text:str
    content:str


class Postresponds(BaseModel):
    text:str
    content:str