# Dostęp

Front: [https://zciwolvo.github.io/skapiec/]
API: [https://www.igorgawlowicz.pl/skapiec/get_data]

# Instrukcja lokalnego uruchamiania

Aby uruchomić projekt lokalnie należy zmienić URL podane w fetchach w `skapiec/skapiec/src/app.js` w 15 i 16 linijce, zmieniamy:

`https://www.igorgawlowicz.pl/skapiec/scrape?phrase=${search}` na `http://127.0.0.1:5000/scrape?phrase=${search}`

oraz

`https://www.igorgawlowicz.pl/skapiec/get_data?phrase=${search}` na `http://127.0.0.1:5000/get_data?phrase=${search}`

następnie musimy przygotować dwa okna terminala:

pierwsze otwieramy w głównym repozytorium, musimy mieć zainstalowanego pythona3, następnie piszemy:

```bash
pip install -r requirements.txt

python server.py
```

Teraz musimy otworzyć drugi terminal w ścieżce `skapiec/skapiec`, musimy mieć zainstalowanego `node`'a:

```bash
npm install

npm start
```

Aplikacja uruchomi się lokalnie i możemy korzystać z niej z URL w konsoli
