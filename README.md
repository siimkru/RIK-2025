# Osaühingu haldamise rakendus

See on Flask-põhine veebirakendus, mis võimaldab hallata osaühingute andmeid: otsing, detailvaade ja asutamine.

## Funktsionaalsus

- **Avaleht:** Otsing osaühingu nime, registrikoodi või osaniku järgi.
- **Detailvaade:** Kuvab osaühingu põhiteavet ja osanike nimekirja.
- **Asutamise vorm:** Uue osaühingu andmete lisamine koos osanike teabega.

## Kasutatavad tehnoloogiad

- **Backend:** Flask, SQLAlchemy, SQLite
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap
- **Server:** Gunicorn (tootmisrežiimiks)
- **Testimine:** pytest

## Paigaldusjuhised

1. **Klooni repository:**
   ```
   git clone <repository_url>
   cd projekti_nimi
   ```
2. **Loo virtuaalkeskkond ja aktiveeri see:**
   ```
   python -m venv venv
   source venv/bin/activate   # Linux/MacOS
   venv\Scripts\activate      # Windows
   ```
3. **Installi sõltuvused:**
   ```
   pip install -r requirements.txt
   ```
4. **Käivita rakendus arendusrežiimis:**
   ```
   python run.py
   ```
5. **Testide käivitamine:**
   ```
   pytest
   ```

## Konfiguratsioon

Muuda failis `config.py` olevaid seadeid vastavalt vajadusele. Näiteks:
- `SECRET_KEY` – sessioonide ja CSRF kaitse jaoks.
- `SQLALCHEMY_DATABASE_URI` – andmebaasi ühenduse string.