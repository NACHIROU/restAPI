from pydantic import BaseModel
class Item :
    def __init__(self, name:str, descrition:str) -> None:
        self.name = name
        self.description = descrition
