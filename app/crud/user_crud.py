from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schemas import UserCreate
from app.utils.auth import hash_password

# Deze functie maakt een nieuwe gebruiker in de database
def create_user(db: Session, user: UserCreate,role_id:str=2):
    db_user = User(
        name=user.name,
        email=user.email,
        hashed_password=hash_password(user.password),# versleutel het wachtwoord
        is_beheerder=user.is_beheerder,
        role_id=role_id
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Deze functie zoekt een gebruiker op e-mail
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

# Deze functie geeft alle gebruikers terug uit de database
def get_all_users(db: Session):
    return db.query(User).all()

# Deze functie zoekt een gebruiker op ID
def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
