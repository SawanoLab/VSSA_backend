import uuid

from tests.constants import SEASON_ID, USER_ID, TEAM_ONE_ID, TEAM_TWO_ID, NOT_EXIST_USER_ID


def to_uuid(uuid_string):
    return str(uuid.UUID(uuid_string))


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


PLAYER_DATA_JSON = [
    {
        "uuid": to_uuid("18ef9a7adae2456f891c831b04901b8f"),
        "name": "Player 10",
        "player_number": 10,
        "code": "PL10",
        "postion": "Setter",
        "weight": 72,
        "height": 176,
        "user_id": USER_ID,
        "team_id": TEAM_ONE_ID,
        "season_id": SEASON_ID
    },
    {
        "uuid": to_uuid("28ef9a7adae2456f891c831b04901b8f"),
        "name": "Player 11",
        "player_number": 11,
        "code": "PL11",
        "postion": "Wing Spiker",
        "weight": 74,
        "height": 178,
        "user_id": USER_ID,
        "team_id": TEAM_TWO_ID,
        "season_id": SEASON_ID
    },
    {
        "uuid": to_uuid("38ef9a7adae2456f891c831b04901b8f"),
        "name": "Player 12",
        "player_number": 12,
        "code": "PL12",
        "postion": "Middle Blocker",
        "weight": 82,
        "height": 186,
        "user_id": USER_ID,
        "team_id": TEAM_TWO_ID,
        "season_id": SEASON_ID
    },
    {
        "uuid": to_uuid("48ef9a7adae2456f891c831b04901b8f"),
        "name": "Player 13",
        "player_number": 13,
        "code": "PL13",
        "postion": "Opposite",
        "weight": 75,
        "height": 180,
        "user_id": USER_ID,
        "team_id": TEAM_TWO_ID,
        "season_id": SEASON_ID
    },
    {
        "uuid": to_uuid("58ef9a7adae2456f891c831b04901b8f"),
        "name": "Player 14",
        "player_number": 14,
        "code": "PL14",
        "postion": "Libero",
        "weight": 69,
        "height": 171,
        "user_id": USER_ID,
        "team_id": TEAM_TWO_ID,
        "season_id": SEASON_ID
    },
    {
        "uuid": to_uuid("61ef9a7adae2456f891c831b04901b8f"),
        "name": "Player 19",
        "player_number": 19,
        "code": "PL19",
        "postion": "Middle Blocker",
        "weight": 80,
        "height": 185,
        "user_id": USER_ID,
        "team_id": TEAM_TWO_ID,
        "season_id": SEASON_ID
    },
    {
        "uuid": to_uuid("62ef9a7adae2456f891c831b04901b8f"),
        "name": "Player 20",
        "player_number": 20,
        "code": "PL20",
        "postion": "Opposite",
        "weight": 78,
        "height": 182,
        "user_id": USER_ID,
        "team_id": TEAM_TWO_ID,
        "season_id": SEASON_ID
    },
    {
        "uuid": to_uuid("68ef9a7adae2456f891c831b04901b1f"),
        "name": "Player 3",
        "player_number": 3,
        "code": "PL3",
        "postion": "Setter",
        "weight": 70,
        "height": 175,
        "user_id": USER_ID,
        "team_id": TEAM_ONE_ID,
        "season_id": SEASON_ID
    },
    {
        "uuid": to_uuid("68ef9a7adae2456f891c831b04901b2f"),
        "name": "Player 4",
        "player_number": 4,
        "code": "PL4",
        "postion": "Wing Spiker",
        "weight": 78,
        "height": 182,
        "user_id": USER_ID,
        "team_id": TEAM_ONE_ID,
        "season_id": SEASON_ID
    },
    {
        "uuid": to_uuid("68ef9a7adae2456f891c831b04901b3f"),
        "name": "Player 5",
        "player_number": 5,
        "code": "PL5",
        "postion": "Middle Blocker",
        "weight": 81,
        "height": 186,
        "user_id": USER_ID,
        "team_id": TEAM_ONE_ID,
        "season_id": SEASON_ID
    },
    {
        "uuid": to_uuid("68ef9a7adae2456f891c831b04901b4f"),
        "name": "Player 6",
        "player_number": 6,
        "code": "PL6",
        "postion": "Opposite",
        "weight": 77,
        "height": 181,
        "user_id": USER_ID,
        "team_id": TEAM_ONE_ID,
        "season_id": SEASON_ID
    },
    {
        "uuid": to_uuid("68ef9a7adae2456f891c831b04901b5f"),
        "name": "Player 7",
        "player_number": 7,
        "code": "PL7",
        "postion": "Libero",
        "weight": 67,
        "height": 172,
        "user_id": USER_ID,
        "team_id": TEAM_ONE_ID,
        "season_id": SEASON_ID
    },
    {
        "uuid": to_uuid("68ef9a7adae2456f891c831b04901b6f"),
        "name": "Player 8",
        "player_number": 8,
        "code": "PL8",
        "postion": "Wing Spiker",
        "weight": 76,
        "height": 179,
        "user_id": USER_ID,
        "team_id": TEAM_ONE_ID,
        "season_id": SEASON_ID
    },
    {
        "uuid": to_uuid("68ef9a7adae2456f891c831b04901b7f"),
        "name": "Player 9",
        "player_number": 9,
        "code": "PL9",
        "postion": "Middle Blocker",
        "weight": 80,
        "height": 184,
        "user_id": USER_ID,
        "team_id": TEAM_ONE_ID,
        "season_id": SEASON_ID
    },
    {
        "uuid": to_uuid("68ef9a7adae2456f891c831b04901b8f"),
        "name": "Player 1",
        "player_number": 1,
        "code": "PL1",
        "postion": "Wing Spiker",
        "weight": 75,
        "height": 180,
        "user_id": USER_ID,
        "team_id": TEAM_ONE_ID,
        "season_id": SEASON_ID
    },
    {
        "uuid": to_uuid("68ef9a7adae2456f891c831b04901b9f"),
        "name": "Player 2",
        "player_number": 2,
        "code": "PL2",
        "postion": "Middle Blocker",
        "weight": 80,
        "height": 185,
        "user_id": USER_ID,
        "team_id": TEAM_ONE_ID,
        "season_id": SEASON_ID
    },
    {
        "uuid": to_uuid("68ef9a7adae2456f891c831b14901b8f"),
        "name": "Player 15",
        "player_number": 15,
        "code": "PL15",
        "postion": "Wing Spiker",
        "weight": 73,
        "height": 177,
        "user_id": USER_ID,
        "team_id": TEAM_TWO_ID,
        "season_id": SEASON_ID
    },
    {
        "uuid": to_uuid("78ef9a7adae2456f891c831b04901b8f"),
        "name": "Player 16",
        "player_number": 16,
        "code": "PL16",
        "postion": "Middle Blocker",
        "weight": 79,
        "height": 183,
        "user_id": USER_ID,
        "team_id": TEAM_TWO_ID,
        "season_id": SEASON_ID
    },
    {
        "uuid": to_uuid("88ef9a7adae2456f891c831b04901b8f"),
        "name": "Player 17",
        "player_number": 17,
        "code": "PL17",
        "postion": "Setter",
        "weight": 72,
        "height": 174,
        "user_id": USER_ID,
        "team_id": TEAM_TWO_ID,
        "season_id": SEASON_ID
    },
    {
        "uuid": to_uuid("98ef9a7adae2456f891c831b04901b8f"),
        "name": "Player 18",
        "player_number": 18,
        "code": "PL18",
        "postion": "Wing Spiker",
        "weight": 74,
        "height": 177,
        "user_id": USER_ID,
        "team_id": TEAM_TWO_ID,
        "season_id": SEASON_ID
    }
]

PLAYER_CREATE_DATA_JSON = {
    "name": "Player 21",
    "player_number": 21,
    "code": "PL21",
    "postion": "Wing Spiker",
    "weight": 78,
    "height": 182,
    "user_id": USER_ID,
    "team_id": TEAM_ONE_ID,
    "season_id": SEASON_ID
}

PLAYER_UPDATE_DATA_JSON = {
    "name": "Player 21",
    "player_number": 21,
    "code": "PL21",
    "postion": "Wing Spiker",
    "weight": 78,
    "height": 182,
    "user_id": USER_ID,
    "team_id": TEAM_ONE_ID,
    "season_id": SEASON_ID,
}

PLAYER_NOT_RERATION_DATA_JSON = {
    "uuid": "7dbbaab0-13c2-49e4-b7d9-f066b45c2003",
    "name": "Player 21",
    "player_number": 21,
    "code": "PL21",
    "postion": "Wing Spiker",
    "weight": 78,
    "height": 182,
    "user_id": USER_ID,
    "team_id": TEAM_ONE_ID,
    "season_id": SEASON_ID,
}
