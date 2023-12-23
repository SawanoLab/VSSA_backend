from tests.constants import SEASON_ID, USER_ID, TEAM_ONE_ID, TEAM_TWO_ID

TEAM_DATA_JSON = [
    {
        "name": "Team 2",
        "code": "T2",
        "director": "Director 2",
        "coach": "Coach 2",
        "trainer": "Trainer 2",
        "doctor": "Doctor 2",
        "season_id": SEASON_ID,
        "user_id": USER_ID,
        "uuid": TEAM_TWO_ID
    },
    {
        "name": "Team 1",
        "code": "T1",
        "director": "Director 1",
        "coach": "Coach 1",
        "trainer": "Trainer 1",
        "doctor": "Doctor 1",
        "season_id": SEASON_ID,
        "user_id": USER_ID,
        "uuid": TEAM_ONE_ID
    }
]

TEAM_CREATE_DATA_JSON = {
    "name": "Team 3",
    "code": "T3",
    "director": "Director 3",
    "coach": "Coach 3",
    "trainer": "Trainer 3",
    "doctor": "Doctor 3",
    "season_id": SEASON_ID,
    "user_id": USER_ID
}
