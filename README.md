# SemanticRec Lab

Исследовательский pet-проект по рекомендательным системам,
Semantic ID и генеративным рекомендациям.

## Цель проекта

Постепенно реализовать и сравнить:

- popularity baseline;
- collaborative filtering;
- matrix factorization;
- sequential Transformer;
- content embeddings;
- RQ-VAE;
- Semantic ID;
- DIGER-inspired обучение;
- UniGRec-inspired обучение.

## Текущий статус

Настройка окружения и структуры проекта.

## Окружение

- Python 3.13
- NumPy
- pandas
- matplotlib
- scikit-learn
- ipykernel

## Проверка окружения

Из корня проекта:

```powershell
.venv\Scripts\python.exe src\check_environment.

## Загрузка данных

Проект использует MovieLens 100K. Сам датасет не хранится
в Git-репозитории и загружается отдельным скриптом.

```powershell
python src\data\download_movielens.py
```

После запуска исходные файлы сохраняются в:

```text
data/raw/
```