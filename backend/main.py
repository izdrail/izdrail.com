import asyncio

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


from api.endpoints import socialgenerator
from api.endpoints import feeds
from api.endpoints import google
from api.endpoints import seo
from api.endpoints import videos
from api.endpoints import testing
from api.endpoints import scrapper
from api.endpoints import jobs
from api.endpoints import nlp as nlp_endpoint
from api.endpoints import security

app = FastAPI(
    title="Backend for izdrail.com",
    description="This is a collection of endpoints that powers izdrail.com",
    version="0.4.9",
    terms_of_service="https://izdrail.com/",

    contact={
        "name": "Stefan",
        "url": "https://izdrail.com/",
        "email": "stefan@izdrail.com",
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Endpoints
app.include_router(nlp_endpoint.router)

app.include_router(google.router)
app.include_router(feeds.router)

app.include_router(seo.router)

app.include_router(videos.router)
app.include_router(testing.router)
app.include_router(socialgenerator.router)
app.include_router(jobs.router)
app.include_router(scrapper.router)
app.include_router(security.router)


@app.get("/")
async def root():
    return {"data": "You can try the latest API endpoint here -> https://backend.izdrail.com/docs"}

# This line is removed as it was causing the issue
# loop = asyncio.get_event_loop()
# loop.run_until_complete()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003, reload=True)