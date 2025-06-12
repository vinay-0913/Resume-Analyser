from nltk.tokenize import sent_tokenize
from sentence_transformers import SentenceTransformer, util

# Load SBERT once (any good model)
sbert_model = SentenceTransformer('all-MiniLM-L6-v2')  # lightweight + accurate

def get_semantic_matches(keywords, resume_text, threshold=0.58):
    matches = []
    resume_sentences = sent_tokenize(resume_text)

    for keyword in keywords:
        kw_embedding = sbert_model.encode(keyword, convert_to_tensor=True)
        
        for sentence in resume_sentences:
            sent_embedding = sbert_model.encode(sentence, convert_to_tensor=True)
            similarity = util.cos_sim(kw_embedding, sent_embedding).item()

            if similarity >= threshold:
                matches.append({
                    "keyword": keyword,
                    "matched_sentence": sentence.strip(),
                    "score": round(similarity, 2)
                })
                break  # stop after first match
    return matches
