from pydantic import BaseModel, PositiveFloat, Field
from typing import Literal

class ParsedRequest(BaseModel):
    input_text : str

class ParsedResponse(BaseModel):
    customer_name : str
    amount : PositiveFloat
    intent : Literal['payment_given', 'payment_recieved', 'check_balance']
    confidence : float = Field(ge=0.0, le=1.0)

