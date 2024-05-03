import spacy

# 加载模型
nlp_ginza = spacy.load('ja_ginza_electra')  # Ginza模型，适用于复杂的NLP任务
nlp_core = spacy.load('ja_core_news_lg')  # Core模型，适用于一般的文本处理


def process_text(text):
    """
    使用Ginza和Core模型结合处理文本。
    Args:
    - text (str): 输入的文本。

    Returns:
    - dict: 包含从两个模型中提取的信息。
    """
    # 使用Ginza模型进行实体识别
    doc_ginza = nlp_ginza(text)
    entities = [(ent.text, ent.label_) for ent in doc_ginza.ents]

    # 使用Core模型进行词性标注
    doc_core = nlp_core(text)
    pos_tags = [(token.text, token.pos_) for token in doc_core]

    # 返回结合两种模型的结果
    return {
        "entities": entities,  # Ginza的实体识别结果
        "pos_tags": pos_tags  # Core的词性标注结果
    }


# 示例文本
# text = "日本の東京タワーと富士山は有名な観光地です。"
text = "オラクルデータベースとは？"

# 处理文本
results = process_text(text)
print("实体识别结果:", results["entities"])
print("词性标注结果:", results["pos_tags"])