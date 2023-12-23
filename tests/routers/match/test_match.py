from tests.conftest import test_db  # noqa: F401
from tests.constants import SEASON_ID, USER_ID, TEAM_ONE_ID, TEAM_TWO_ID, NOT_EXIST_USER_ID  # noqa: F401
from tests.constants.team import TEAM_DATA_JSON, TEAM_CREATE_DATA_JSON


def test_get_match(client):
    res = client.get(f'/matches/?user_id={USER_ID}')
    data = res.json()
    print(data)
    assert res.status_code == 200
