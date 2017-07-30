from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from database_setup import *

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

# Creates a session. If a rollback to the 
# previous commit is wished, simply use session.rollback().
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Delete Categories, items and users if exisitng.
session.query(Category).delete()
session.query(Items).delete()
session.query(User).delete()

# Populate the database with an initial user (myself)
User1 = User(name="Philip Harms",
              email="philip.harms@whu.edu",
              picture='https://goo.gl/Pdjc4U')
session.add(User1)
session.commit()

# Create categories in the DB
Category1 = Category(name="Football",
                      user_id=1)
session.add(Category1)
session.commit()

Category2 = Category(name="Tennis",
                      user_id=1)
session.add(Category2)
session.commit()

Category3 = Category(name="Ski",
                      user_id=1)
session.add(Category3)
session.commit()

# Populate a category with items for testing
# Using different users for items also
Item1 = Items(name="Soccer Shoes",
               date=datetime.datetime.now(),
               description="Shoes to become a soccer player.",
               picture="https://goo.gl/baMnct",
               category_id=1,
               user_id=1)
session.add(Item1)
session.commit()

Item2 = Items(name="Jersey",
               date=datetime.datetime.now(),
               description="A jersey of your favourite soccer team.",
               picture="https://goo.gl/wn8LLu",
               category_id=1,
               user_id=1)
session.add(Item2)
session.commit()

Item3 = Items(name="Football",
               date=datetime.datetime.now(),
               description="A perfectly round Football.",
               picture="https://goo.gl/tHxnPE",
               category_id=1,
               user_id=1)
session.add(Item3)
session.commit()

print "The database has been initialized and populated with great soccer related items."
