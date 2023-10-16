"""creating the tables

Revision ID: 339aa5937e15
Revises: 
Create Date: 2023-10-16 08:42:00.715723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '339aa5937e15'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agegroups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('group_name', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('club_roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role_name', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('members',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=255), nullable=False),
    sa.Column('gender', sa.String(length=255), nullable=False),
    sa.Column('next_of_kin', sa.String(length=255), nullable=True),
    sa.Column('date_of_birth', sa.DateTime(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('sub_county', sa.String(length=255), nullable=True),
    sa.Column('learning_institution', sa.String(length=255), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('heigth', sa.Integer(), nullable=True),
    sa.Column('special_needs', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patrons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('patron_name', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sports',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sport_name', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('store_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.String(length=255), nullable=False),
    sa.Column('item_price', sa.Float(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('facilitation_fees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fee_amount', sa.Float(), nullable=False),
    sa.Column('facilitation_date', sa.DateTime(), nullable=True),
    sa.Column('sport_id', sa.Integer(), nullable=True),
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['member_id'], ['members.id'], ),
    sa.ForeignKeyConstraint(['sport_id'], ['sports.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('game_captains',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('captain_name', sa.String(length=255), nullable=False),
    sa.Column('sport_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['sport_id'], ['sports.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('membership_fees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('registration_date', sa.DateTime(), nullable=False),
    sa.Column('individual_fee', sa.Integer(), nullable=False),
    sa.Column('group_fee', sa.Integer(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['member_id'], ['members.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sportspreferences',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.Column('sport_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['member_id'], ['members.id'], ),
    sa.ForeignKeyConstraint(['sport_id'], ['sports.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('store_records ',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sale_date', sa.DateTime(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('total_price', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['store_items.id'], ),
    sa.ForeignKeyConstraint(['member_id'], ['members.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('store_records ')
    op.drop_table('sportspreferences')
    op.drop_table('membership_fees')
    op.drop_table('game_captains')
    op.drop_table('facilitation_fees')
    op.drop_table('store_items')
    op.drop_table('sports')
    op.drop_table('patrons')
    op.drop_table('members')
    op.drop_table('club_roles')
    op.drop_table('agegroups')
    # ### end Alembic commands ###