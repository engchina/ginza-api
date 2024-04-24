# ginza-api
GiNZA API

## Prepare

```
conda create -n ginza-api python=3.11 -y
conda activate ginza-api
```

```
pip install -r requirements.txt
```

## Run

```
uvicorn main:app --reload --host 0.0.0.0 --port 7932
```

