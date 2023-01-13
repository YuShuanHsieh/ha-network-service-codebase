
from fastapi import FastAPI
import uvicorn
from app.settings import Settings, get_settings
from app import endpoints

settings: Settings = get_settings()


def build_app() -> FastAPI:

    api = FastAPI(docs_url=None)
    api.mount("/api", endpoints.app)

    return api


app = build_app()

if __name__ == "__main__":
    uvicorn.run(
        app=settings.WEB_APP,
        host=settings.WEB_HOST,
        port=settings.WEB_PORT,
        reload=True,
        log_config="logging.yaml"
    )
