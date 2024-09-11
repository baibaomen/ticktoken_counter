from fastapi import FastAPI, HTTPException
import tiktoken

app = FastAPI()

@app.post("/")
async def get_token_count(model: str, message: str):
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        raise HTTPException(status_code=400, detail="Unsupported model name")

    tokens = encoding.encode(message)
    token_count = len(tokens)

    return {"token_count": token_count}
