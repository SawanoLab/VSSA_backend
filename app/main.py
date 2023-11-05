from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware
from routers.season import season_router
from routers.team import team_router


router = APIRouter()
router.include_router(
    season_router,
    prefix='/seasons',
    tags=['seasons']
)

router.include_router(
    team_router,
    prefix='/teams',
    tags=['teams']
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router)
