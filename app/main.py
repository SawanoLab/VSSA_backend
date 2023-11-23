import os
from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware
from routers.season import season_router
from routers.team import team_router
from routers.player import player_router
from routers.match import match_router

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

router.include_router(
    match_router,
    prefix='/matches',
    tags=['matches']
)

app = FastAPI()

origins = [os.environ.get('ALLOW_ORIGIN')]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(router)
