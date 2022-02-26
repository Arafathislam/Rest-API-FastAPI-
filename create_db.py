from database import Base,engine
from models import Item

print("creating Database .....")
Base.metadata.create_all(engine)

