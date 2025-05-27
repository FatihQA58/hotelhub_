# Deze bestand maakt verbinding met de database
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Lees de .env bestand
load_dotenv()

# Haal de database link uit .env bestand
DATABASE_URL = os.getenv("DATABASE_URL")

# Maak verbinding met SQLite database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Maak een sessie om met de database te werken
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Basisstructuur voor alle tabellen
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()