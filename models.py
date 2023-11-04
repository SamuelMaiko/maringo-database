from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class User(db.Model):
    
    __tablename__='users'
    
    id=db.Column(db.Integer, primary_key=True)
    full_name=db.Column(db.String(255), nullable=False)
    gender=db.Column(db.String(255), nullable=False)
    next_of_kin_contact=db.Column(db.String(255), nullable=True)
    date_of_birth=db.Column(db.DateTime, nullable=False)
    email=db.Column(db.String(255), nullable=False)
    role=db.Column(db.Enum('Admin','Member'), nullable=False)
    password=db.Column(db.String(255), nullable=False)
    sub_county=db.Column(db.String(255), nullable=True)
    learning_institution=db.Column(db.String(255), nullable=True)
    weight=db.Column(db.Integer, nullable=True)
    heigth=db.Column(db.Integer, nullable=True)
    special_needs=db.Column(db.String(255), nullable=True)
    
    created_at=db.Column(db.DateTime, server_default=db.func.now() )
    updated_at=db.Column(db.DateTime, onupdate=db.func.now() )
    
class Sport(db.Model):
    
    __tablename__='sports'
    
    id=db.Column(db.Integer, primary_key=True)
    sport_name=db.Column(db.String(255), nullable=False)
    
    created_at=db.Column(db.DateTime, server_default=db.func.now() )
    updated_at=db.Column(db.DateTime, onupdate=db.func.now() )
    
# # class SportsPreference(db.Model):
    
# #     __tablename__='sportspreferences'    
    
# #     id=db.Column(db.Integer, primary_key=True)
# #     member_id=db.Column(db.Integer, db.ForeignKey('users.id'))
# #     sport_id=db.Column(db.Integer, db.ForeignKey('sports.id'))
    
# #     created_at=db.Column(db.DateTime, server_default=db.func.now() )
# #     updated_at=db.Column(db.DateTime, onupdate=db.func.now() )
    
# class MembershipFee(db.Model):
    
#     __tablename__='membership_fees'
    
#     id=db.Column(db.Integer, primary_key=True)
#     registration_date=db.Column(db.DateTime, nullable=False)
#     individual_fee=db.Column(db.Integer, nullable=False)
#     group_fee=db.Column(db.Integer, nullable=False)
#     # member_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    
#     created_at=db.Column(db.DateTime, server_default=db.func.now() )
#     updated_at=db.Column(db.DateTime, onupdate=db.func.now() )
    

# class AgeGroup(db.Model):
    
#     __tablename__='agegroups'
    
#     id=db.Column(db.Integer, primary_key=True)
#     group_name=db.Column(db.String(255), nullable=False)
    
#     created_at=db.Column(db.DateTime, server_default=db.func.now())
#     updated_at=db.Column(db.DateTime, onupdate=db.func.now())
    
# class StoreItem(db.Model):
    
#     __tablename__='store_items'
    
#     id=db.Column(db.Integer, primary_key=True)
#     item_name=db.Column(db.String(255), nullable=False)
#     item_price=db.Column(db.Float, nullable=False)
    
#     created_at=db.Column(db.DateTime, server_default=db.func.now() )
#     updated_at=db.Column(db.DateTime, onupdate=db.func.now() )

# class StoreRecord(db.Model):
    
#     __tablename__='store_records'
    
#     id=db.Column(db.Integer, primary_key=True)
#     sale_date=db.Column(db.DateTime, nullable=True)
#     # item_id=db.Column(db.Integer, db.ForeignKey('store_items.id'))
#     # member_id=db.Column(db.Integer, db.ForeignKey('users.id'))
#     quantity=db.Column(db.Integer, nullable=True)
#     total_price=db.Column(db.Float, nullable=True)
    
    
#     created_at=db.Column(db.DateTime, server_default=db.func.now() )
#     updated_at=db.Column(db.DateTime, onupdate=db.func.now() )
    
# class FacilitationFee(db.Model):
    
#     __tablename__='facilitation_fees'
    
#     id=db.Column(db.Integer, primary_key=True)
#     fee_amount=db.Column(db.Float, nullable=False)
#     facilitation_date=db.Column(db.DateTime, nullable=True)
#     # sport_id=db.Column(db.Integer, db.ForeignKey('sports.id'))
#     # member_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    
#     created_at=db.Column(db.DateTime, server_default=db.func.now() )
#     updated_at=db.Column(db.DateTime, onupdate=db.func.now() )
    
# class ClubRole(db.Model):
    
#     __tablename__='club_roles'
    
#     id=db.Column(db.Integer, primary_key=True)
#     role_name=db.Column(db.String(255), nullable=False)
    
#     created_at=db.Column(db.DateTime, server_default=db.func.now() )
#     updated_at=db.Column(db.DateTime, onupdate=db.func.now() )
    
# class Patron(db.Model):
    
#     __tablename__='patrons'
    
#     id=db.Column(db.Integer, primary_key=True)
#     patron_name=db.Column(db.String(255), nullable=False)
    
#     created_at=db.Column(db.DateTime, server_default=db.func.now() )
#     updated_at=db.Column(db.DateTime, onupdate=db.func.now() )
    
# class GameCaptain(db.Model):
    
#     __tablename__='game_captains'
    
#     id=db.Column(db.Integer, primary_key=True)
#     captain_name=db.Column(db.String(255), nullable=False)
#     sport_id=db.Column(db.Integer, db.ForeignKey('sports.id'))
    
#     created_at=db.Column(db.DateTime, server_default=db.func.now() )
#     updated_at=db.Column(db.DateTime, onupdate=db.func.now() )