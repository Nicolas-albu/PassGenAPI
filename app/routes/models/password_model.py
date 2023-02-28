from pydantic import BaseModel

class Password(BaseModel):
    password_length: int
    types_of_characters: list[str] | None = ["uppercase", "lowercase", "digits"]