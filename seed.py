from models import Role, Audition, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///theater.db')
Session = sessionmaker(bind=engine)
session = Session()

# Creating roles
role1 = Role(character_name="Hamlet")
role2 = Role(character_name="Macbeth")

# Creating auditions
audition1 = Audition(actor="John Doe", location="New York", phone=123456789, hired=False, role=role1)
audition2 = Audition(actor="Jane Smith", location="Los Angeles", phone=987654321, hired=True, role=role1)
audition3 = Audition(actor="Alice Johnson", location="Chicago", phone=567890123, hired=False, role=role2)

session.add_all([role1, role2, audition1, audition2, audition3])
session.commit()
print("Database seeded successfully!")
