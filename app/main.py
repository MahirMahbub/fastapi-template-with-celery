from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.routes import test
from db.database import SessionLocal

app = FastAPI()

# API Doc
# app = FastAPI(
#     title="Wiki-Movie",
#     description="Wikipedia Persing Tools",
#     version="1.0.0",
# )


# Error
@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    # print(f"OMG! An HTTP error!: {repr(exc)}")
    # Add error logger here loguru
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"},
    )


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()

# API routes
app.include_router(
    router=test.router,
    tags=["example"]
)

db = SessionLocal()



@app.on_event("startup")
async def startup_event():
    pass

# if __name__ == '__main__':
#     uvicorn.run(app='app:app', reload=True, port="7003", host="0.0.0.0")
