# arcmetal.si

Spletna stran ARC METAL (statična, brez WordPressa).

- Objavljene datoteke so v korenu repozitorija (`index.html`, podmape za podstrani, `style.css`, `main.js`).
- Izvorna koda generatorja je v `_izvor/`. Besedila se urejajo v `_izvor/build.py`, nato:

```
cd _izvor
python3 build.py site
cp -r dist-site/. ..
```
