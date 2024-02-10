"""create tables

Revision ID: e32ec177e9d3
Revises: 
Create Date: 2023-12-26 02:10:52.256443

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
import sqlalchemy_utils
import uuid

# revision identifiers, used by Alembic.
revision = 'e32ec177e9d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text(
                        'current_timestamp'), nullable=False),
                    sa.Column('updated_at', mysql.TIMESTAMP(), server_default=sa.text(
                        'current_timestamp on update current_timestamp'), nullable=False),
                    sa.Column('uuid', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.Column('username', sa.String(
                        length=128), nullable=False),
                    sa.PrimaryKeyConstraint('uuid', name=op.f('pk_users'))
                    )
    op.create_table('seasons',
                    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text(
                        'current_timestamp'), nullable=False),
                    sa.Column('updated_at', mysql.TIMESTAMP(), server_default=sa.text(
                        'current_timestamp on update current_timestamp'), nullable=False),
                    sa.Column('uuid', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.Column('start_day', sa.DATETIME(), nullable=False),
                    sa.Column('end_day', sa.DATETIME(), nullable=False),
                    sa.Column('season_name', sa.String(
                        length=128), nullable=False),
                    sa.Column('game_format', sa.String(
                        length=128), nullable=False),
                    sa.Column('code', sa.String(length=128), nullable=False),
                    sa.Column('user_id', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.ForeignKeyConstraint(
                        ['user_id'], ['users.uuid'], name=op.f('fk_seasons_user_id_users')),
                    sa.PrimaryKeyConstraint('uuid', name=op.f('pk_seasons'))
                    )
    op.create_table('teams',
                    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text(
                        'current_timestamp'), nullable=False),
                    sa.Column('updated_at', mysql.TIMESTAMP(), server_default=sa.text(
                        'current_timestamp on update current_timestamp'), nullable=False),
                    sa.Column('uuid', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.Column('name', sa.String(length=128), nullable=False),
                    sa.Column('code', sa.String(length=128), nullable=False),
                    sa.Column('director', sa.String(
                        length=128), nullable=True),
                    sa.Column('coach', sa.String(length=128), nullable=True),
                    sa.Column('trainer', sa.String(length=128), nullable=True),
                    sa.Column('doctor', sa.String(length=128), nullable=True),
                    sa.Column('season_id', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.Column('user_id', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.ForeignKeyConstraint(['season_id'], ['seasons.uuid'], name=op.f(
                        'fk_teams_season_id_seasons')),
                    sa.ForeignKeyConstraint(
                        ['user_id'], ['users.uuid'], name=op.f('fk_teams_user_id_users')),
                    sa.PrimaryKeyConstraint('uuid', name=op.f('pk_teams'))
                    )
    op.create_table('matchs',
                    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text(
                        'current_timestamp'), nullable=False),
                    sa.Column('updated_at', mysql.TIMESTAMP(), server_default=sa.text(
                        'current_timestamp on update current_timestamp'), nullable=False),
                    sa.Column('uuid', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.Column('home_team_id', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.Column('away_team_id', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.Column('season_id', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.Column('user_id', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.Column('youtube_url', sa.String(
                        length=128), nullable=False),
                    sa.ForeignKeyConstraint(['away_team_id'], ['teams.uuid'], name=op.f(
                        'fk_matchs_away_team_id_teams')),
                    sa.ForeignKeyConstraint(['home_team_id'], ['teams.uuid'], name=op.f(
                        'fk_matchs_home_team_id_teams')),
                    sa.ForeignKeyConstraint(['season_id'], ['seasons.uuid'], name=op.f(
                        'fk_matchs_season_id_seasons')),
                    sa.ForeignKeyConstraint(
                        ['user_id'], ['users.uuid'], name=op.f('fk_matchs_user_id_users')),
                    sa.PrimaryKeyConstraint('uuid', name=op.f('pk_matchs'))
                    )
    op.create_table('players',
                    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text(
                        'current_timestamp'), nullable=False),
                    sa.Column('updated_at', mysql.TIMESTAMP(), server_default=sa.text(
                        'current_timestamp on update current_timestamp'), nullable=False),
                    sa.Column('uuid', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.Column('name', sa.String(length=128), nullable=False),
                    sa.Column('player_number', sa.Integer(), nullable=False),
                    sa.Column('code', sa.String(length=128), nullable=False),
                    sa.Column('postion', sa.String(
                        length=128), nullable=False),
                    sa.Column('weight', sa.Integer(), nullable=True),
                    sa.Column('height', sa.Integer(), nullable=True),
                    sa.Column('user_id', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.Column('team_id', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.Column('season_id', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.ForeignKeyConstraint(['season_id'], ['seasons.uuid'], name=op.f(
                        'fk_players_season_id_seasons')),
                    sa.ForeignKeyConstraint(
                        ['team_id'], ['teams.uuid'], name=op.f('fk_players_team_id_teams')),
                    sa.ForeignKeyConstraint(
                        ['user_id'], ['users.uuid'], name=op.f('fk_players_user_id_users')),
                    sa.PrimaryKeyConstraint('uuid', name=op.f('pk_players'))
                    )
    op.create_table('attacks',
                    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text(
                        'current_timestamp'), nullable=False),
                    sa.Column('updated_at', mysql.TIMESTAMP(), server_default=sa.text(
                        'current_timestamp on update current_timestamp'), nullable=False),
                    sa.Column('uuid', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.Column('home_team_score', sa.Integer(), nullable=False),
                    sa.Column('home_team_set_score',
                              sa.Integer(), nullable=False),
                    sa.Column('away_team_score', sa.Integer(), nullable=False),
                    sa.Column('away_team_set_score',
                              sa.Integer(), nullable=False),
                    sa.Column('attack_start_zone',
                              sa.Integer(), nullable=False),
                    sa.Column('attack_end_zone', sa.Integer(), nullable=False),
                    sa.Column('attack_ball_type', sa.Enum('high', 'medium',
                                                          'quick', 'other', name='attackballtype'), nullable=False),
                    sa.Column('attack_skill', sa.Enum('headSpike', 'softSpike',
                                                      'dink', name='attackskill'), nullable=False),
                    sa.Column('attack_evaluation', sa.Enum('kill', 'overPass', 'possibleCover',
                                                           'blocked', 'inPlay', 'error', name='attackevaluationtype'), nullable=False),
                    sa.Column('user_id', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.Column('match_id', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.Column('team_id', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.Column('player_id', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.ForeignKeyConstraint(['match_id'], ['matchs.uuid'], name=op.f(
                        'fk_attacks_match_id_matchs')),
                    sa.ForeignKeyConstraint(['player_id'], ['players.uuid'], name=op.f(
                        'fk_attacks_player_id_players')),
                    sa.ForeignKeyConstraint(
                        ['team_id'], ['teams.uuid'], name=op.f('fk_attacks_team_id_teams')),
                    sa.ForeignKeyConstraint(
                        ['user_id'], ['users.uuid'], name=op.f('fk_attacks_user_id_users')),
                    sa.PrimaryKeyConstraint('uuid', name=op.f('pk_attacks'))
                    )
    op.create_table('match_set_score',
                    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text(
                        'current_timestamp'), nullable=False),
                    sa.Column('updated_at', mysql.TIMESTAMP(), server_default=sa.text(
                        'current_timestamp on update current_timestamp'), nullable=False),
                    sa.Column('uuid', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.Column('match_id', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.Column('set_number', sa.Integer(), nullable=False),
                    sa.Column('score_team_home', sa.Integer(), nullable=False),
                    sa.Column('score_team_away', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['match_id'], ['matchs.uuid'], name=op.f(
                        'fk_match_set_score_match_id_matchs')),
                    sa.PrimaryKeyConstraint(
                        'uuid', name=op.f('pk_match_set_score'))
                    )
    op.create_table('playerMatchInfo',
                    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text(
                        'current_timestamp'), nullable=False),
                    sa.Column('updated_at', mysql.TIMESTAMP(), server_default=sa.text(
                        'current_timestamp on update current_timestamp'), nullable=False),
                    sa.Column('uuid', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.Column('player_id', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.Column('match_id', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.Column('on_court', sa.Boolean(), nullable=False),
                    sa.Column('zone_code', sa.String(
                        length=255), nullable=False),
                    sa.Column('libero', sa.Boolean(), nullable=False),
                    sa.ForeignKeyConstraint(['match_id'], ['matchs.uuid'], name=op.f(
                        'fk_playerMatchInfo_match_id_matchs')),
                    sa.ForeignKeyConstraint(['player_id'], ['players.uuid'], name=op.f(
                        'fk_playerMatchInfo_player_id_players')),
                    sa.PrimaryKeyConstraint(
                        'uuid', name=op.f('pk_playerMatchInfo'))
                    )
    op.create_table('match_scores',
                    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text(
                        'current_timestamp'), nullable=False),
                    sa.Column('updated_at', mysql.TIMESTAMP(), server_default=sa.text(
                        'current_timestamp on update current_timestamp'), nullable=False),
                    sa.Column('uuid', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.Column('match_set_score_id', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.Column('score_team_id', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.Column('home_team_score', sa.Integer(), nullable=False),
                    sa.Column('away_team_score', sa.Integer(), nullable=False),
                    sa.Column('sequence_number', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['match_set_score_id'], ['match_set_score.uuid'], name=op.f(
                        'fk_match_scores_match_set_score_id_match_set_score')),
                    sa.ForeignKeyConstraint(['score_team_id'], ['teams.uuid'], name=op.f(
                        'fk_match_scores_score_team_id_teams')),
                    sa.PrimaryKeyConstraint(
                        'uuid', name=op.f('pk_match_scores'))
                    )
    op.create_table('event_times',
                    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text(
                        'current_timestamp'), nullable=False),
                    sa.Column('updated_at', mysql.TIMESTAMP(), server_default=sa.text(
                        'current_timestamp on update current_timestamp'), nullable=False),
                    sa.Column('uuid', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.Column('start_time', sa.Integer(), nullable=False),
                    sa.Column('match_id', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), default=uuid.uuid4, nullable=False),
                    sa.Column('sumnail_url', sa.String(
                        length=128), nullable=False),
                    sa.Column('event_name', sa.String(
                        length=128), nullable=False),
                    sa.ForeignKeyConstraint(['match_id'], ['matchs.uuid'], name=op.f(
                        'fk_event_times_match_id_matchs')),
                    sa.PrimaryKeyConstraint(
                        'uuid', name=op.f('pk_event_times'))
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('attack_events')
    op.drop_table('match_scores')
    op.drop_table('playerMatchInfo')
    op.drop_table('match_set_score')
    op.drop_table('attacks')
    op.drop_table('players')
    op.drop_table('matchs')
    op.drop_table('teams')
    op.drop_table('seasons')
    op.drop_table('users')
    # ### end Alembic commands ###
