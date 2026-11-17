from fastapi import FastAPI
from app.schemas import ParsedRequest, ParsedResponse


app = FastAPI()

@app.get("/health")
def health_check():
    return {"status":"active"}


@app.post("/parse", response_model=ParsedResponse)
def parse_order(payload: ParsedRequest) -> ParsedResponse:
    return ParsedResponse(
        customer_name="Rameshbhai",
        amount=100,
        intent="payment_recieved",
        confidence=0.95
    )

