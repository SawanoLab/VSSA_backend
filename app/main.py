from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware
from routers.season import season_router
from routers.team import team_router
from routers.player import player_router

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

router.include_router(
    player_router,
    prefix='/players',
    tags=['players']
)

app = FastAPI()

origins = ['http://localhost:3001']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(router)
