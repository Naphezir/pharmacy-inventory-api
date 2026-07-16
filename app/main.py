from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
            "message": "Pharmacy Inventory API",
            "status": "running"
            }

# to run use: uvicorn name-of-main-file:name-of-app --reload (reloads after change in file)
# e.g. here:  uvicorn app.main:app --reload
# TODO: what was 'uv run' for