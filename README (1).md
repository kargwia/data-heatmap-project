# 📊 data-heatmap-project

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.0-green?logo=pandas)
![Flask](https://img.shields.io/badge/Flask-API-black?logo=flask)
![Seaborn](https://img.shields.io/badge/Seaborn-Heatmap-orange)

> Үш сандық баған (`a`, `b`, `c`) бар `triple.csv` деректер жиыны негізінде **корреляция матрицасын** есептеп, **жылу картасын (heatmap)** визуализациялайтын Python жобасы.

---

## 📁 Жоба құрылымы

```
data-heatmap-project/
│
├── 📄 triple.csv               # Деректер жиыны (20 жол, 3 баған: a, b, c)
├── 📄 corr_matrix.csv          # Нәтиже: корреляция матрицасы (task12 жасайды)
├── 🖼️ heatmap.png              # Нәтиже: жылу картасы (task13 жасайды)
│
├── 🐍 task09_centering.py      # Матрица центрлеу — орташаны азайту
├── 🐍 task10_cov_corr.py       # Ковариация + корреляция (формуламен)
├── 🐍 task11_pandas_corr.py    # Pandas .corr() эталон + салыстыру
├── 🐍 task12_save_csv.py       # Матрицаны CSV-ге сақтау
├── 🐍 task13_heatmap.py        # Seaborn heatmap → PNG
├── 🐍 task14_api.py            # Flask REST API (GET/POST → JSON)
│
├── 📄 requirements.txt         # Тәуелділіктер
└── 📄 README.md
```

---

## ⚙️ Орнату

```bash
# Репозиторийді клондаңыз
git clone https://github.com/СІЗДІҢ_АТЫңыз/data-heatmap-project.git
cd data-heatmap-project

# Тәуелділіктерді орнатыңыз
pip install -r requirements.txt
```

---

## 🚀 Іске қосу

### Тапсырма 9 — Матрица центрлеу
```bash
python task09_centering.py
```
> `triple.csv` оқып, әр бағаннан орташаны азайтады (центрлеу).

---

### Тапсырма 10 — Ковариация және корреляция (формуламен)
```bash
python task10_cov_corr.py
```
> `a` және `b` бағандары арасындағы `cov(a,b)` және `corr(a,b)` мәндерін математикалық формула арқылы есептейді.

---

### Тапсырма 11 — Pandas эталон + салыстыру
```bash
python task11_pandas_corr.py
```
> `df.corr()` арқылы 3×3 матрица шығарады және тапсырма 10 нәтижесімен салыстырады.

---

### Тапсырма 12 — CSV сақтау
```bash
python task12_save_csv.py
```
> Корреляция матрицасын `corr_matrix.csv` файлына сақтайды.

**`corr_matrix.csv` мысалы:**
```
,a,b,c
a,1.0,-1.0,1.0
b,-1.0,1.0,-1.0
c,1.0,-1.0,1.0
```

---

### Тапсырма 13 — Heatmap визуализация
```bash
python task13_heatmap.py
```
> Seaborn арқылы 3×3 корреляция жылу картасын сызады және `heatmap.png` ретінде сақтайды.

---

### Тапсырма 14 — Flask REST API
```bash
python task14_api.py
```
> Сервер `http://127.0.0.1:5000` мекенжайында іске қосылады.

**GET сұранысы:**
```bash
curl http://127.0.0.1:5000/corr
```

**POST сұранысы (файл жіберу):**
```bash
curl -X POST -F "file=@triple.csv" http://127.0.0.1:5000/corr
```

**JSON нәтиже:**
```json
{
  "status": "ok",
  "method": "POST",
  "rows": 20,
  "corr_matrix": {
    "a": {"a": 1.0, "b": -1.0, "c": 1.0},
    "b": {"a": -1.0, "b": 1.0, "c": -1.0},
    "c": {"a": 1.0, "b": -1.0, "c": 1.0}
  }
}
```

---

## 📊 Тапсырмалар кестесі

| № | Файл | Кіріс | Шығыс |
|---|------|-------|-------|
| 9 | `task09_centering.py` | `triple.csv` | Консоль |
| 10 | `task10_cov_corr.py` | `triple.csv` | Консоль |
| 11 | `task11_pandas_corr.py` | `triple.csv` | Консоль |
| 12 | `task12_save_csv.py` | `triple.csv` | `corr_matrix.csv` |
| 13 | `task13_heatmap.py` | `triple.csv` | `heatmap.png` |
| 14 | `task14_api.py` | HTTP сұраныс | JSON |

---

## 🛠️ Технологиялар

| Кітапхана | Қолданылуы |
|-----------|-----------|
| `numpy` | Матрица операциялары, центрлеу |
| `pandas` | CSV оқу, `.corr()` |
| `matplotlib` | Графика негізі |
| `seaborn` | Heatmap визуализация |
| `flask` | REST API |

---

## 👤 Автор

**GitHub:** [@СІЗДІҢ_АТЫңыз](https://github.com/СІЗДІҢ_АТЫңыз)

---

> 📌 Зертханалық жұмыс — Python + Data Analysis
