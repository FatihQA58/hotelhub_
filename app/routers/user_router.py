from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user_schemas import UserCreate, UserOut
from app.crud.user_crud import create_user, get_user_by_email, get_user_by_id
from app.db.database import SessionLocal
from app.utils.auth import verify_password, create_access_token, get_current_user
from app.models.user_model import User

router = APIRouter(
     prefix="/users", 
     tags=["Gebruikers"]
)

# Veritabanı bağlantısı
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Yeni kullanıcı kaydı
@router.post("/register", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="E-mailadres bestaat al.")
    return create_user(db, user,role_id=2)


# Kullanıcı girişi ve token oluşturma
@router.post("/login")
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Ongeldige inloggegevens.")
    token = create_access_token(data={"user_id": user.id,"role_id":user.role_id})
    return {"access_token": token, "token_type": "bearer"}

# Giriş yapmış kullanıcıyı getir
@router.get("/me", response_model=UserOut)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

# Belirli kullanıcıyı ID ile getir
@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Gebruiker niet gevonden.")
    return user
