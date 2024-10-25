from typing import Optional

import uvicorn
from fastapi import FastAPI, HTTPException

from main import get_airports

app = FastAPI()


@app.get("/airports")
def fetch_airports(code: str = None, name: str = None) -> Optional[dict]:
    if code is None or name is None:
        raise HTTPException(status_code=400, detail="code or name is invalid")
    result = get_airports(code, name)
    return result


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
