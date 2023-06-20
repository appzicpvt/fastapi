from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine

from apps.contact_messages import router as contact_messages_router
from apps.converter import router as converter_router

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# Create Tables
Base.metadata.create_all(bind=engine)

# Application
app = FastAPI()

# add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(contact_messages_router.router)
app.include_router(converter_router.router)


@app.get("/")
def root():
    return {"detail": "loaded"}
