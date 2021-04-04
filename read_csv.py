import pandas as pd

def read_csv(filename):
  data = pd.read_csv(filename)
  return data