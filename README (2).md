## 2048 Neon Edition

Implementare a jocului clasic 2048 în Python, cu interfață grafică construită în tkinter și o estetică neon vibrantă. Jucătorul combină plăcuțe numerotate pe o grilă de 4x4 pentru a atinge valoarea 2048.

---

## Ce face
* La pornire se generează automat două plăcuțe cu valorile 2 sau 4 în poziții aleatorii.
* **Săgeată stânga / dreapta / sus / jos:** Mută toate plăcuțele în direcția respectivă. Plăcuțele identice vecine se combină și se dublează.
* După fiecare mutare validă apare o plăcuță nouă (2 sau 4) într-o celulă liberă aleatorie.
* Dacă o celulă atinge valoarea **2048** apare un mesaj de victorie.
* Dacă nu mai există celule libere și nicio combinare posibilă, apare ecranul de **Game Over**.

---

## Tech
* **Limbaj:** Python 3
* **GUI:** tkinter
* **Biblioteci:** `random`, `tkinter.messagebox`

---

## Run
```
python main.py
```

Nu necesită instalarea niciunei biblioteci externe — tkinter este inclus în Python 3.

---

## Structura
```
2048-neon/
├── logic/
│   ├── game.py        # Clasa Joc2048 — logica și GUI-ul
│   └── constants.py   # Culorile pentru fiecare valoare de plăcuță
├── .gitignore
├── README.md
├── main.py            # Entry point — pornește aplicația
└── 2048_complet.py    # Tot codul într-un singur fișier
```
