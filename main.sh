#!/bin/bash
eval "$(conda shell.bash hook)"
conda activate ginza-api
uvicorn main:app --reload --host 0.0.0.0 --port 7932