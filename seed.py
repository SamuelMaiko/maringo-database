# from models import db, User,Sport,SportsPreference,MembershipFee,AgeGroup,StoreItem,StoreRecord,FacilitationFee,ClubRole,Patron,GameCaptain
from models import db, User,Sport
from app import app
from faker import Faker
import random

fake=Faker()

with app.app_context():
    
    User.query.delete()
    Sport.query.delete()
    print("deleting all ...")
    # AgeGroup.query.delete()
    # SportsPreference.query.delete()
    # MembershipFee.query .delete()
    
    # creating members__________________________________________________
    print("adding members...")
    all_members=list()
    gender_options=["Male","Female"]
    
    for n in range(0,5,1):
        new_member=User(id=n+1,full_name=fake.name(),gender=random.choice(gender_options),next_of_kin_contact=fake.phone_number(),
        date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=80),email=fake.email(),
        role="Admin",password=f'{fake.first_name()}254',sub_county=fake.city(),
        learning_institution=fake.unique.company(),weight=random.randint(50,120),heigth=random.randint(100,220),
        special_needs=fake.sentence(nb_words=5)
        )
        
        all_members.append(new_member)
    
    db.session.bulk_save_objects(all_members)
    
    # _____________________________________________ adding myself
    new_user=User(id=6,full_name="Samuel Maiko",gender="Male",next_of_kin_contact="do@gmail.com",
        date_of_birth=fake.date_of_birth(minimum_age=19, maximum_age=20),email="thatsepic@gmail.com",
        role="Admin",password="juanGonzalez",sub_county="Somewhere",
        learning_institution="USIU",weight=65,heigth=172,
        special_needs="None at all")
        
    db.session.add(new_user);
    
    new_user2=User(id=7,full_name="Big Daws",gender="Male",next_of_kin_contact="bd@gmail.com",
        date_of_birth=fake.date_of_birth(minimum_age=19, maximum_age=20),email="bigdaws@gmail.com",
        role="Member",password="bigdaws",sub_county="Somewhere",
        learning_institution="USIU",weight=65,heigth=172,
        special_needs="None at all")
        
    db.session.add(new_user2);
    # adding sports________________________________________
    all_sports=list()
    
    sports_options=["swimming", "hockey"," lawn tennis"," table tennis", "darts", "badminton", "volleyball", 
"basketball", "netball", "football", "baseball", "rugby", "pool", "chess", "draft"]
    count=1
    for each_sport in sports_options:
        new_sport=Sport(id=count,sport_name=each_sport)
        all_sports.append(new_sport)
        count+=1
        
    db.session.bulk_save_objects(all_sports)
        
     # adding sports_preferences________________________________________*************
    # all_sports_preferences=list()
    # for n in range(0,40):
    #     new_sports_reference=SportsPreference(member_id=random.randint(1,20),sport_id=random.randint(1,15))
    #     all_sports_preferences.append(new_sports_reference)
    
    # db.session.bulk_save_objects(all_sports_preferences)
        
       
    # # adding membership fees________________________________________****************
    # all_membership_fees=list()
    # individual_fee_options=[4500,10000,6000,8000]
    # group_fee_options=[14500,10000,16000,20000]
    # for n in range(0,20):
    #     new_membership_fee=MembershipFee(registration_date=fake.date_of_birth(minimum_age=18, maximum_age=80),
    #                                      individual_fee=random.choice(individual_fee_options),group_fee=random.choice(group_fee_options),
    #                                      member_id=random.randint(1,20)
    #                                      )
                                                    
    #     all_membership_fees.append(new_membership_fee)
    
    # db.session.bulk_save_objects(all_membership_fees)
    
    
    # # adding age groups________________________________________
    # all_agegroups=list()
    # agegroup_options=['btn 12-17 yrs', 'btn 18-25 yrs','btn 25-35 yrs']
    # for n in range(0,3):
    #     new_agegroup=AgeGroup(group_name=random.choice(agegroup_options))
    #     all_agegroups.append(new_agegroup)
    
    # db.session.bulk_save_objects(all_agegroups)
        
    
    
    db.session.commit()
    