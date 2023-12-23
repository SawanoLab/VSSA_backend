
from tests.constants import ATTACK_ID, USER_ID, TEAM_ONE_ID, PLAYER_ID, MATCH_ID  # noqa: F401
from app.enums.attack import AttackBallType, AttackSkill, AttackEvaluationType

ATTACK_DATA_JSON = [
    {
        "uuid": ATTACK_ID,
        "home_team_score": 1,
        "away_team_score": 0,
        "home_team_set_score": 1,
        "away_team_set_score": 0,
        "attack_start_zone": 3,
        "attack_end_zone": 4,
        "attack_ball_type": AttackBallType.high,
        "attack_skill": AttackSkill.headSpike,
        "attack_evaluation": AttackEvaluationType.kill,
        "user_id": USER_ID,
        "match_id": MATCH_ID,
        "team_id": TEAM_ONE_ID,
        "player_id": PLAYER_ID,
    }
]

ATTACK_CREATE_DATA_JSON = {
    "home_team_score": 0,
    "away_team_score": 0,

    "home_team_set_score": 0,
    "away_team_set_score": 0,

    "attack_start_zone": 0,
    "attack_end_zone": 0,

    "attack_ball_type": AttackBallType.high,  # Must match enum value
    "attack_skill": AttackSkill.headSpike,  # Must match enum value
    "attack_evaluation": AttackEvaluationType.kill,  # Must match enum value

    "user_id": USER_ID,
    "match_id": MATCH_ID,
    "team_id": TEAM_ONE_ID,
    "player_id": PLAYER_ID,
}
