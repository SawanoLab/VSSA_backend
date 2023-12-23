"""add youtube_url column

Revision ID: d21746fdffe9
Revises: 3bf113fdd508
Create Date: 2023-12-21 14:52:38.091147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd21746fdffe9'
down_revision = '3bf113fdd508'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('matchs', sa.Column(
        'youtube_url', sa.String(length=255), nullable=False))


def downgrade():
    op.drop_column('matchs', 'youtube_url')
