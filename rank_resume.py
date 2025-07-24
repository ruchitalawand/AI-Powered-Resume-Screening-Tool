from transformers import BertTokenizer, BertModel
import torch
import numpy as np
import os

class ResumeRanker:
    def __init__(self, model_name='bert-base-uncased'):
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertModel.from_pretrained(model_name)

    def get_embedding(self, text):
        tokens = self.tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
        with torch.no_grad():
            outputs = self.model(**tokens)
        return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

    def rank_resumes(self, resumes, job_description):
        jd_embedding = self.get_embedding(job_description)
        scores = {}
        for name, text in resumes.items():
            resume_embedding = self.get_embedding(text)
            similarity = self.cosine_similarity(jd_embedding, resume_embedding)
            scores[name] = similarity
        return sorted(scores.items(), key=lambda x: x[1], reverse=True)

    @staticmethod
    def cosine_similarity(vec1, vec2):
        return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
