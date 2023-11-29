from uuid import uuid4
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from models import User, Season, Team, Player, \
    Match, MatchScore, PlayerMatchInfo
import random


def create_user(db: Session, user_id: str, username: str) -> User:
    user = User(uuid=user_id,
                username=username)
    db.add(user)
    return user


def create_season(db: Session, name: str, user_id) -> Season:
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    start_day = datetime(current_year, current_month, 1)
    end_day = start_day + timedelta(days=30)

    season = Season(
        uuid=uuid4(),
        season_name=name,
        start_day=start_day,
        end_day=end_day,
        game_format='Game Format Example',
        code=f'S{current_year}_{current_month:02}_001',
        user_id=user_id
    )
    db.add(season)
    return season


def create_team(db: Session, name: str, code: str, user_id, season_id) -> Team:
    team = Team(
        uuid=uuid4(),
        name=name,
        code=code,
        director=f'Director {code}',
        coach=f'Coach {code}',
        trainer=f'Trainer {code}',
        doctor=f'Doctor {code}',
        user_id=user_id,
        season_id=season_id
    )
    db.add(team)
    return team


def create_player(db: Session, name: str, player_number: int, code: str, postion: str, weight: int, height: int, user_id, team_id, season_id):
    player = Player(
        uuid=uuid4(),
        name=name,
        player_number=player_number,
        code=code,
        postion=postion,
        weight=weight,
        height=height,
        user_id=user_id,
        team_id=team_id,
        season_id=season_id
    )
    db.add(player)
    return player


def create_match_score(db: Session, home_team_score: int, away_team_score: int) -> MatchScore:
    match_score = MatchScore(
        uuid=uuid4(),
        home_team_score=home_team_score,
        away_team_score=away_team_score
    )
    db.add(match_score)
    return match_score


def create_match(db: Session, home_team_id, away_team_id, season_id, match_score_id) -> Match:
    match = Match(
        uuid=uuid4(),
        home_team_id=home_team_id,
        away_team_id=away_team_id,
        season_id=season_id,
        match_score_id=match_score_id,
    )
    db.add(match)
    return match


def create_player_match_info(db: Session, player_id, match_id, onCourt, zone_code, libero) -> PlayerMatchInfo:
    player_match_info = PlayerMatchInfo(
        uuid=uuid4(),
        player_id=player_id,
        match_id=match_id,
        onCourt=onCourt,
        zone_code=zone_code,
        libero=libero,
    )
    db.add(player_match_info)
    return player_match_info


def insert_seed_data():
    db = Session()
    user_id = '1963f7eff71e4a0c944d62628a5bb070'
    user = create_user(db, user_id, 'username')
    season = create_season(db, 'Season 2022', user.uuid)
    team1 = create_team(db, 'Team 1', 'T1', user.uuid, season.uuid)
    team2 = create_team(db, 'Team 2', 'T2', user.uuid, season.uuid)
    position = [
        'Middle Blocker',
        'Wing Spiker',
        'Setter',
        'Opposite',
        'Libero',
        'Wing Spiker',
    ]

    player1 = []
    player2 = []
    for i in range(1, 11):
        player1.append(create_player(db,
                                     f'Player {i}',
                                     i,
                                     f'P{i}',
                                     position[random.randint(0, 5)],
                                     random.randint(50, 100),
                                     random.randint(150, 200),
                                     user.uuid,
                                     team1.uuid,
                                     season.uuid))
        player2.append(create_player(db,
                                     f'Player {i}',
                                     i,
                                     f'P{i}', 'Position',
                                     position[random.randint(0, 5)],
                                     random.randint(50, 100),
                                     random.randint(150, 200),
                                     user.uuid,
                                     team2.uuid,
                                     season.uuid))
    match_score = create_match_score(db, '1', 25, 20)
    match = create_match(db,
                         home_team_id=team1.uuid,
                         away_team_id=team2.uuid,
                         season_id=season.uuid,
                         match_score_id=match_score.uuid,
                         )
    zone = ['Z1', 'Z2', 'Z3', 'Z4', 'Z5', 'Z6']

    for i in range(1, 11):
        create_player_match_info(db,
                                 player_id=player1[i].uuid,
                                 match_id=match.uuid,
                                 onCourt=True,
                                 zone_code=zone[random.randint(0, 5)],
                                 libero=False,
                                 )
        create_player_match_info(db,
                                 player_id=player2[i].uuid,
                                 match_id=match.uuid,
                                 onCourt=True,
                                 zone_code=zone[random.randint(0, 5)],
                                 libero=False,
                                 )
    db.commit()


if __name__ == "__main__":
    insert_seed_data()
