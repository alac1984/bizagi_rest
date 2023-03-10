"""First revision

Revision ID: 2d87f34b9ea2
Revises: 
Create Date: 2022-12-27 16:33:51.473127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2d87f34b9ea2"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "tb_forn",
        sa.Column("forn_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("rating", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("forn_id"),
    )
    op.create_table(
        "tb_compra",
        sa.Column("com_id", sa.Integer(), nullable=False),
        sa.Column("forn_id", sa.Integer(), nullable=True),
        sa.Column("date", sa.DateTime(), nullable=True),
        sa.Column("item", sa.String(), nullable=False),
        sa.Column("value", sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(
            ["forn_id"],
            ["tb_forn.forn_id"],
        ),
        sa.PrimaryKeyConstraint("com_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("tb_compra")
    op.drop_table("tb_forn")
    # ### end Alembic commands ###
