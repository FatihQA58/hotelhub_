from pydantic import BaseModel, EmailStr

# Dit model wordt gebruikt als iemand een nieuwe gebruiker maakt
class UserCreate(BaseModel):
    name: str             # naam is verplicht
    email: EmailStr       # geldig e-mailadres
    password: str         # wachtwoord (gewoon tekst bij invoer)

# Dit model wordt gebruikt als iemand probeert in te loggen
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Dit model wordt gebruikt om info terug te geven zonder wachtwoord
class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True  # yeni Pydantic v2 standardı
