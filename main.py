import re

import spacy
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

nlp_ja_model = spacy.load('ja_ginza_electra')
nlp_en_model = spacy.load('en_core_web_lg')


class QueryText(BaseModel):
    query_text: str


@app.post("/split-query/")
def split_query(query: QueryText):
    """
    Extracts relevant search texts from the input query text based on specific token tags.
    No '名詞-数詞'.

    Args:
    - query_text (str): The input query text to extract search texts from.

    Returns:
    - list: A list of search texts extracted from the input query text.
    """
    print(f"{query.query_text=}")
    ja_split_queries = list(set([token.text for token in nlp_ja_model(query.query_text) if
                                 any(token.tag_.startswith(tag) for tag in
                                     ['名詞-普通名詞', '名詞-固有名詞', '動詞-一般'])]))
    english_words = [text for text in ja_split_queries if re.match(r'^[a-zA-Z]', text)]
    en_split_queries = list(
        set([token.text for token in nlp_en_model(' '.join(english_words)) if token.pos_ in ['PROPN', 'NOUN', 'VERB']]))
    final_split_queries = list(set(ja_split_queries).difference(english_words).union(en_split_queries))
    return final_split_queries
