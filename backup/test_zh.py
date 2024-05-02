import spacy

# 加载模型
nlp_core = spacy.load('zh_core_web_lg')  # Core模型，适用于一般的文本处理


def process_text(text):
    """
    使用Ginza和Core模型结合处理文本。
    Args:
    - text (str): 输入的文本。

    Returns:
    - dict: 包含从两个模型中提取的信息。
    """
    # 使用Core模型进行词性标注
    doc_core = nlp_core(text)
    pos_tags = [(token.text, token.pos_) for token in doc_core]

    # 返回结合两种模型的结果
    return {
        "pos_tags": pos_tags  # Core的词性标注结果
    }


# 示例文本
text = "spaCy语言模型包含了一些强大的文本分析功能，如词性标注和命名实体识别功能。This is a sentence.江苏爱康太阳能科技股份有限公司报告期内第一大客户是谁？"

# 处理文本
results = process_text(text)
print("词性标注结果:", results["pos_tags"])