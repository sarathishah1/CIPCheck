from sentence_transformers import SentenceTransformer, util
import pandas as pd
import numpy as np


def create_base_encoding():
  # Initialize the pre-trained model
  # df=pd.read_pickle('df_embedded 1.pkl')
  # df['Intermediate Description']=df['Idea Title Statement']+". "+df['Summarized Idea']
  # model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

  # # Define the predefined statements
  # statements = df['Intermediate Description'].tolist()
  # # Compute embeddings Afor all sentences
  # statement_embeddings = model.encode(statements)
  np_load_old = np.load
  # modify the default parameters of np.load
  np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
  statement_embeddings=np.load('embeddings.npy')
  return statement_embeddings

def create_input_encoding(input_statement):
  # Initialize the pre-trained model
  model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

  input_embedding = model.encode(input_statement)

  # Compute cosine similarity scores
  similarity_scores = util.cos_sim(input_embedding, baseencoding)
  return similarity_scores


def generate_output(similarity_scores,statemets):
  o=[]
  for i in range(len(similarity_scores[0])):
    o.append([i,similarity_scores[0][i].item()])
    v=pd.DataFrame(o,columns=['index','similarity']).sort_values('similarity',ascending=[False])[:5]['index']
  outputstr=[]
  for i in v:
    outputstr.append(statemets[i])
  return outputstr
