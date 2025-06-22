# src/fraud_detection/pipelines/enriquecimento/nodes.py


import pandas as pd
import numpy as np
from pathlib import Path

def enriquecer_transacoes(caminho_csv: str) -> pd.DataFrame:
    # Lê o CSV manualmente
    df = pd.read_csv(caminho_csv, parse_dates=["TransactionTime"])

    # Ordena por cliente e tempo
    df = df.sort_values(by=["UserId", "TransactionTime"])

    # Tempo desde a última transação
    df["TempoDesdeUltima"] = (
        df.groupby("UserId")["TransactionTime"]
        .diff()
        .dt.total_seconds()
    )

    # Cria coluna de Ano/Mês
    df["AnoMes"] = df["TransactionTime"].dt.to_period("M")

    # Valor total por usuário/mês
    gasto_mensal = (
        df.groupby(["UserId", "AnoMes"])["ValorTotal"]
        .sum()
        .rename("GastoMensal")
        .reset_index()
    )
    df = df.merge(gasto_mensal, on=["UserId", "AnoMes"], how="left")

    # Média de gasto por usuário
    media_gasto = (
        df.groupby("UserId")["ValorTotal"]
        .mean()
        .rename("MediaGastoUser")
        .reset_index()
    )
    df = df.merge(media_gasto, on="UserId", how="left")

    # Frequência de compras por mês
    freq_mensal = (
        df.groupby(["UserId", "AnoMes"])
        .size()
        .rename("FrequenciaMensal")
        .reset_index()
    )
    df = df.merge(freq_mensal, on=["UserId", "AnoMes"], how="left")

    # 🔍 Regras básicas de detecção de fraude
    df["is_fraud"] = 0

    # 1. Valor da transação muito acima da média do usuário
    df.loc[df["ValorTotal"] > df["MediaGastoUser"] * 5, "is_fraud"] = 1

    # 2. Transações de madrugada (00h–05h)
    df["Hora"] = df["TransactionTime"].dt.hour
    df.loc[df["Hora"].between(0, 5), "is_fraud"] = 1

    # 3. País fora da Europa
    paises_europeus = [
        "United Kingdom", "Germany", "France", "Spain", "Italy", "Portugal",
        "Belgium", "Netherlands", "Sweden", "Norway", "Finland", "Denmark",
        "Austria", "Switzerland", "Ireland", "Greece", "Poland", "Czech Republic",
        "Hungary", "Romania"
    ]
    df.loc[~df["Country"].isin(paises_europeus), "is_fraud"] = 1

    # 4. Transações muito rápidas em sequência (< 60 segundos)
    df.loc[df["TempoDesdeUltima"] < 60, "is_fraud"] = 1

    return df
