from tests.conftest import test_db  # noqa: F401
from tests.constants.player import (PLAYER_DATA_JSON,
                                    PLAYER_CREATE_DATA_JSON,
                                    PLAYER_UPDATE_DATA_JSON,
                                    USER_ID,
                                    NOT_EXIST_USER_ID)


def test_get_player(client):
    res = client.get(f'/players/?user_id={USER_ID}')
    data = res.json()
    assert res.status_code == 200
    assert data == PLAYER_DATA_JSON


def test_get_player_error(client):
    res = client.get(f'/players/?user_id={NOT_EXIST_USER_ID}')
    data = res.json()
    assert res.status_code == 200
    assert data == []


def test_update_player(client, test_db):    # noqa: F811
    res = client.put(
        f'/players/{PLAYER_DATA_JSON[0]["uuid"]}?user_id={USER_ID}',
        json=PLAYER_UPDATE_DATA_JSON
        )
    data = res.json()
    PLAYER_UPDATE_DATA_JSON['uuid'] = PLAYER_DATA_JSON[0]["uuid"]
    assert res.status_code == 200
    assert data == PLAYER_UPDATE_DATA_JSON


def test_create_player(client, test_db):    # noqa: F811
    res = client.post('/players/', json=PLAYER_CREATE_DATA_JSON)
    data = res.json()
    PLAYER_CREATE_DATA_JSON['uuid'] = data.get('uuid')
    assert res.status_code == 200
    assert data == PLAYER_CREATE_DATA_JSON
