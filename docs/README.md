# 🏨 HotelHub

HotelHub is een webapplicatie voor hotelreserveringen, ontwikkeld met **FastAPI**. De applicatie maakt het mogelijk voor **gasten** om hotels te zoeken en te boeken, en voor **hoteleigenaars** om hun aanbod te beheren.

---

## 🚀 Functionaliteiten

### 🔎 Gebruiker (Gast)
- Hotels zoeken op locatie, datum en kenmerken
- Beschikbare kamers bekijken en reserveren
- Reviews achterlaten na een verblijf

### 🏨 Hoteleigenaar
- Hotels en kamers toevoegen en beheren
- Boekingen bekijken in een kalenderoverzicht
- Gasten beoordelen na verblijf

### ⚙️ Systeem
- Realtime controle op beschikbaarheid bij reserveren
- Beveiligde login via JWT-authenticatie

---
### 💻 Technologieën

FastAPI

SQLAlchemy

Pydantic

SQLite (ontwikkelomgeving)

JWT-authenticatie

## 🛠️ Installatie & Uitvoeren

```bash
# Virtuele omgeving aanmaken
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate

# Benodigde pakketten installeren
pip install -r requirements.txt

# Applicatie starten
uvicorn app.main:app --reload
