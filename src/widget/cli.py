import uvicorn


def main() -> None:
    uvicorn.run("widget.app:app", host="127.0.0.1", port=8080, reload=False)
