"""Changed Compra date (datetime) to date

Revision ID: 9c34f4235482
Revises: 2d87f34b9ea2
Create Date: 2022-12-27 23:55:41.330180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9c34f4235482"
down_revision = "2d87f34b9ea2"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("tb_compra", "date", type_=sa.Date)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("tb_compra", "date", type_=sa.DateTime)
    # ### end Alembic commands ###
