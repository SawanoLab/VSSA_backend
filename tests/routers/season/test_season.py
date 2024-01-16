from tests.conftest import test_db  # noqa: F401
from tests.constants import SEASON_ID, USER_ID, TEAM_ONE_ID, TEAM_TWO_ID, NOT_EXIST_USER_ID  # noqa: F401
from tests.constants.season import SEASON_DATA_JSON, SEASON_CREATE_DATA_JSON  # noqa: F401


def test_get_season(client):
    res = client.get(f'/seasons/?user_id={USER_ID}')
    data = res.json()
    assert res.status_code == 200
    assert data == SEASON_DATA_JSON


def test_get_season_not_exist_user(client):
    res = client.get(f'/seasons/?user_id={NOT_EXIST_USER_ID}')
    data = res.json()
    assert res.status_code == 200
    assert data == []


def test_post_season(client, test_db): # noqa: F811
    res = client.post('/seasons/', json=SEASON_CREATE_DATA_JSON)
    data = res.json()
    SEASON_CREATE_DATA_JSON['uuid'] = data.get('uuid')
    assert res.status_code == 200
    assert data == SEASON_CREATE_DATA_JSON
