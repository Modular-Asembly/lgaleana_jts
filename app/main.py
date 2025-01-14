from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


load_dotenv()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers

from app.orchestration.run_salesforce_to_google_ads_pipeline import router
app.include_router(router)

from app.orchestration.run_salesforce_to_google_ads_pipeline import router
app.include_router(router)
