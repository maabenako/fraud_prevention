import pandas as pd

df = pd.read_csv('/home/maabe/fraud_prevention/fraud-detection/data/01_raw/transaction_data.csv')

# Contagem de UserId inválidos (-1 ou ausentes)
total = len(df)
invalidos = df[df["UserId"] == -1].shape[0]
porcentagem = (invalidos / total) * 100

print(f"🚨 UserId '-1': {invalidos} registros ({porcentagem:.2f}%) de um total de {total}")

print(df)
print(df.info())