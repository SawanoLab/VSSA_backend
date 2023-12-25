from tests.constants import USER_ID, MATCH_ID, ATTACK_ID  # noqa: F401
from tests.constants.attack import ATTACK_CREATE_DATA_JSON, ATTACK_DATA_JSON


def test_get_attacks(client):
    res = client.get(f'/attacks/?user_id={USER_ID}&match_id={MATCH_ID}')
    data = res.json()
    assert res.status_code == 200
    assert data == ATTACK_DATA_JSON


def test_create_attack(client, test_db):  # noqa: F811
    res = client.post('/attacks/', json=ATTACK_CREATE_DATA_JSON)
    data = res.json()
    assert res.status_code == 200
    assert data == ATTACK_DATA_JSON


def test_delete_attack(client, test_db):  # noqa: F811
    res = client.delete(f'/attacks/{ATTACK_ID}?user_id={USER_ID}')
    assert res.status_code == 200
