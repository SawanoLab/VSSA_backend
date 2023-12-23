from tests.conftest import test_db  # noqa: F401
from tests.constants import SEASON_ID, USER_ID, TEAM_ONE_ID, TEAM_TWO_ID, NOT_EXIST_USER_ID # noqa: F401
from tests.constants.team import TEAM_DATA_JSON, TEAM_CREATE_DATA_JSON


def test_get_team(client):
    res = client.get(f'/teams/?user_id={USER_ID}')
    print("USER_ID: ", USER_ID)
    data = res.json()
    assert res.status_code == 200
    assert data == TEAM_DATA_JSON


def test_get_team_error(client):
    res = client.get(f'/teams/?user_id={NOT_EXIST_USER_ID}')
    data = res.json()
    assert res.status_code == 200
    assert data == []


def test_post_team(client, test_db):  # noqa: F811
    res = client.post('/teams/', json=TEAM_CREATE_DATA_JSON)
    data = res.json()
    assert res.status_code == 200
    assert data == TEAM_CREATE_DATA_JSON
