from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.orchestration.run_salesforce_to_google_ads_pipeline import router as pipeline_router

load_dotenv()

app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(pipeline_router)

# Main function to run the FastAPI app
def main() -> None:
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()

from app.models.Opportunity import Opportunity
from app.orchestration.run_salesforce_to_google_ads_pipeline import router
app.include_router(router)
