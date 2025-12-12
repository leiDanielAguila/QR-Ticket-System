from fastapi import FastAPI
from app.utils.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
from app.api.events.router import router as events_router
from app.api.guests.router import router as guests_router
from app.api.auth.router import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(events_router)
app.include_router(guests_router)
app.include_router(auth_router)

@app.get("/")
async def greet():
    return {"Welcome": "Ticketing system"}

    