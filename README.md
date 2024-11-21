# KK Quiz

### Név: Kiss Klarissza
### Neptun kód: EVH9UW

## Projekt Leírása:
A KK Quiz játék egy interaktív kvíz alkalmazás, amelyet a Python tkinter könyvtárának segítségével hoztam létre. Az alkalmazás egy játékos módot biztosít a különböző témakörökben való ismeretek tesztelésére, véletlenszerű kérdések bemutatásával. Az alkalmazás SQLite adatbázisban tárolja a kérdéseket és válaszokat, amelyeket a játék kezdetén véletlenszerű sorrendben jelenít meg.

## Modulok
### main.py
Az alkalmazás grafikus felhasználói felületének megvalósítása és vezérlése.

#### Főbb osztályok és funkciók:
KKQuizApp: Az alkalmazás fő osztálya, amely az interaktív játék logikáját és a UI-t kezeli.

### QuizDatabase.py
Az adatbázis létrehozásával és kezeléssel kapcsolatos funkciókat tartalmazza.

#### Főbb függvények:
create_database: Létrehozza az SQLite adatbázist (quiz.db) 
get_questions_random: Az adatbázisból véletlenszerű sorrendben kinyeri a kérdéseket és válaszokat.
