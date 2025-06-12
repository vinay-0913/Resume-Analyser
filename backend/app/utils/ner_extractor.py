import spacy
nlp = spacy.load("en_core_web_sm")

def extract_named_entities(text):
    doc = nlp(text)
    ents = {"ORG": [], "PERSON": [], "GPE": [], "SKILL": []}

    # Built-in NER
    for ent in doc.ents:
        if ent.label_ in ents:
            ents[ent.label_].append(ent.text)

    # Manual skill-like tokens
    ents["SKILL"] = list(set([
        token.text for token in doc if token.pos_ == "NOUN" and len(token.text) > 2
    ]))

    for k in ents:
        ents[k] = list(set(ents[k]))
    return ents
