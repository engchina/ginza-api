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
or on windows
./main.bat
or on linux
./main.sh
```

## Use

```
http://localhost:7932/v1/tokenize
```

## Test

```
python client.py
```

## Reference

- [https://spacy.io/models](https://spacy.io/models)