from tests.constants import SEASON_ID, USER_ID, TEAM_TWO_ID, NOT_EXIST_USER_ID # noqa: F401

SEASON_DATA_JSON = [
  {
    'start_day': '2022-07-01T00:00:00',
    'end_day': '2022-07-31T23:59:59',
    'season_name': 'Summer 2022',
    'game_format': 'Game Format Example',
    'code': 'S2022_001',
    'user_id': USER_ID,
    'uuid': SEASON_ID
    }
]

SEASON_DATA_JSON_NOT_EXIST_USER = [
  {
    'start_day': '2022-07-01T00:00:00',
    'end_day': '2022-07-31T23:59:59',
    'season_name': 'Summer 2022',
    'game_format': 'Game Format Example',
    'code': 'S2022_001',
    'user_id': NOT_EXIST_USER_ID,
    'uuid': SEASON_ID
  }
]

SEASON_CREATE_DATA_JSON = {
    "start_day": "2022-08-01T00:00:00",
    "end_day": "2022-08-31T23:59:59",
    "season_name": "Summer 2023",
    "game_format": "Game Format Example2",
    "code": "S2023_001",
    "user_id": USER_ID
}

