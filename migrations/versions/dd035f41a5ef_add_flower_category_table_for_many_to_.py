"""Add flower_category table for many-to-many relation

Revision ID: dd035f41a5ef
Revises: 4ab775b7bd99
Create Date: 2025-02-05 19:12:23.182815

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd035f41a5ef'
down_revision: Union[str, None] = '4ab775b7bd99'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Batch Mode를 사용하여 테이블을 복사하면서 'category_id' 컬럼과 외래 키 삭제
    with op.batch_alter_table('flowers') as batch_op:
        batch_op.drop_constraint('fk_flowers_categories', type_='foreignkey')
        batch_op.drop_column('category_id')


def downgrade() -> None:
    # Batch Mode를 사용하여 테이블을 복사하면서 'category_id' 컬럼과 외래 키 다시 추가
    with op.batch_alter_table('flowers') as batch_op:
        batch_op.add_column(sa.Column('category_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_flowers_categories', 'categories', ['category_id'], ['id'])
