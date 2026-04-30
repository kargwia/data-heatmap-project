# data-heatmap-project

Үш сандық баған (a, b, c) бар triple.csv негізінде корреляция матрицасын есептеп, жылу картасын визуализациялайтын Python жобасы.

#Орнату

```bash
pip install -r requirements.txt
```

#Іске қосу

```bash
python task09_centering.py
python task10_cov_corr.py
python task11_pandas_corr.py
python task12_save_csv.py
python task13_heatmap.py
python task14_api.py
```

#API

```bash
curl http://127.0.0.1:5000/corr
curl -X POST -F "file=@triple.csv" http://127.0.0.1:5000/corr
```

#Технологиялар

Python, NumPy, Pandas, Matplotlib, Seaborn, Flask
