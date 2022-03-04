from fastapi import FastAPI

app = FastAPI(title="B.L.O.S.",
              description="Basic List Organizer Server (B.L.O.S.), The backend for the Basic List Organizer (B.L.O.) set of apps.")


async def index():
    return "Hello World!"

app.add_api_route("/", index, methods=["GET"])
