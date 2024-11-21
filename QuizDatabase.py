import sqlite3
import random

databaseName = "quiz.db"

def create_database():
    connection = sqlite3.connect(databaseName)
    cursor = connection.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS quiz (
                id INTEGER PRIMARY KEY,
                question TEXT NOT NULL,
                answer TEXT NOT NULL
            )
        ''')

    cursor.execute('SELECT COUNT(*) FROM quiz')
    if cursor.fetchone()[0] == 0:
        sample_data = [
            ("Ki volt az első magyar király?", "Szent István"),
            ("Melyik évben fedezte fel Amerika partjait Kolumbusz Kristóf?", "1492"),
            ("Mi volt a rómaiak nyelve?", "Latin"),
            ("Mikor volt a mohácsi csata?", "1526"),
            ("Melyik ország kezdte az ipari forradalmat?", "Nagy-Britannia"),
            ("Mi volt az Árpád-ház alapítója?", "Árpád fejedelem"),
            ("Ki volt Mátyás király apja?", "Hunyadi János"),
            ("Hol épült az első gőzmozdony?", "Angliában"),
            ("Melyik évben egyesült Olaszország?", "1861"),
            ("Mi a Magna Charta?", "Egy 1215-ben kiadott angol szabadságlevél"),
            ("Mi Magyarország legnagyobb tava?", "Balaton"),
            ("Melyik a világ legmagasabb hegysége?", "Himalája"),
            ("Melyik kontinens a legnagyobb területű?", "Ázsia"),
            ("Hol található a Nílus folyó?", "Afrikában"),
            ("Mi a Föld legmélyebb óceáni árka?", "Mariana-árok"),
            ("Mi Olaszország fővárosa?", "Róma"),
            ("Melyik ország zászlaja piros-fehér-zöld? (merőlegesen)", "Magyarország"),
            ("Melyik a világ legnépesebb országa?", "Kína"),
            ("Melyik országban található a Grand Canyon?", "Amerikai Egyesült Államok"),
            ("Milyen éghajlata van az Amazonas-medencének?", "Trópusi"),
            ("Ki írta a Toldi trilógiát?", "Arany János"),
            ("Ki írta a Pál utcai fiúk című regényt?", "Molnár Ferenc"),
            ("Mi Petőfi Sándor legismertebb szerelmes verse?", "Szeptember végén"),
            ("Melyik dráma hőse Rómeó és Júlia?", "William Shakespeare"),
            ("Ki írta az Egri csillagok című regényt?", "Gárdonyi Géza"),
            ("Mit jelent az elbeszélő költemény?", "Verses formájú történetmesélés"),
            ("Ki volt a görög mitológia főistene?", "Zeusz"),
            ("Melyik nép mondáiban szerepel a Kalevala?", "Finn"),
            ("Ki írta a Bűn és bűnhődés című regényt?", "Dosztojevszkij"),
            ("Melyik költő írta a Himnuszt?", "Kölcsey Ferenc"),
            ("Mennyi 12 × 8?", "96"),
            ("Mennyi az 50%-a 200-nak?", "100"),
            ("Mennyi 3⁴ értéke?", "81"),
            ("Hány fokos egy háromszög belső szögeinek összege?", "180°"),
            ("Mi az a prímszám?", "Olyan szám, amelynek csak 1 és önmaga az osztója"),
            ("Mennyi 2/3 és 1/3 összege?", "1"),
            ("Mi az a tangens egy derékszögű háromszögben?", "A szemközti befogó és a szomszédos befogó aránya"),
            ("Mennyi 2x, ha x=7?", "14"),
            ("Mi a kör területe, ha sugara 5 cm?", "25π cm²"),
            ("Mi a fotoszintézis során felszabaduló gáz?", "Oxigén"),
            ("Melyik bolygó a Naprendszer legnagyobb bolygója?", "Jupiter"),
            ("Mi a víz képlete?", "H₂O"),
            ("Milyen típusú állat a bálna?", "Emlős"),
            ("Mi az emberi test legnagyobb szerve?", "Bőr"),
            ("Mi a csontváz funkciója?", "Tartást ad és védi a belső szerveket"),
            ("Hol található a szív a testben?", "A mellkasban, bal oldalon"),
            ("Mi a klorofill?", "Egy zöld színanyag, amely a fotoszintézisben vesz részt"),
            ("Mi a Föld legkülső rétege?", "Kéreg"),
            ("Milyen állatok a hüllők?", "Hidegvérű, tojásokkal szaporodó állatok"),
            ("Hány játékos van egy kosárlabdacsapatban a pályán?", "5"),
            ("Mi a leghíresebb kerékpárverseny neve?", "Tour de France"),
            ("Melyik sportághoz kapcsolódik Lionel Messi?", "Labdarúgás"),
            ("Hány szett szükséges egy teniszmeccs megnyeréséhez?", "Legalább 2 (férfiaknál Grand Slam: 3)"),
            ("Melyik ország rendezte az első modern olimpiai játékokat?", "Görögország"),
            ("Mi a vízilabda labdájának neve?", "Egyszerűen vízilabda"),
            ("Mennyi egy focimeccs rendes játékideje?", "90 perc"),
            ("Mi a sakk legértékesebb figurája?", "Királynő"),
            ("Melyik sportban van ütő?", "Tenisz"),
            ("Ki az NBA történetének legismertebb játékosa?", "Michael Jordan"),
            ("Hány szín van a szivárványban?", "7"),
            ("Mi Magyarország hivatalos nyelve?", "Magyar"),
            ("Mi a világ leggyorsabb állata?", "Vándorsólyom"),
            ("Mi a világ legismertebb mesehőse, akinek piros nadrágja van?", "Mickey egér"),
            ("Ki találta fel a villanykörtét?", "Thomas Edison"),
            ("Mi a tőkehal májából nyert olaj neve?", "Halolaj"),
            ("Hol található a Louvre múzeum?", "Párizs"),
            ("Mi a pi értéke két tizedesjegy pontossággal?", "3,14"),
            ("Mi a fővárosa Japánnak?", "Tokió")
        ]
        cursor.executemany('INSERT INTO quiz (question, answer) VALUES (?, ?)', sample_data)

    connection.commit()
    connection.close()

def get_questions_random():
    connection = sqlite3.connect(databaseName)
    cursor = connection.cursor()
    cursor.execute('SELECT question, answer FROM quiz')
    questions = cursor.fetchall()
    random.shuffle(questions)
    return questions