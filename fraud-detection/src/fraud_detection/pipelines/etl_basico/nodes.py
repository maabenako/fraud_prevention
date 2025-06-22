# src/fraud_detection/pipelines/etl_basico/nodes.py

import polars as pl
from pathlib import Path
import pandas as pd

def transformar_com_polars(_: None) -> pd.DataFrame:
    df = pl.read_csv(
        "/home/maabe/fraud_prevention/fraud-detection/data/01_raw/transaction_data.csv",
        dtypes={"UserId": pl.Utf8}
    )


    df = df.with_columns([
        df["UserId"].cast(pl.Utf8),  # força ser string dentro do Polars
        (df["NumberOfItemsPurchased"] * df["CostPerItem"]).alias("ValorTotal"),
        df["TransactionTime"].str.strptime(
            pl.Datetime,
            format="%a %b %d %H:%M:%S %Z %Y",
            strict=False
        ).alias("TransactionTime")
    ])

    df = df.with_columns([
        df["TransactionTime"].dt.year().alias("Ano"),
        df["TransactionTime"].dt.month().alias("Mes"),
        df["TransactionTime"].dt.weekday().alias("DiaSemana"),
        df["TransactionTime"].dt.hour().alias("Hora")
    ])

    df = df.drop_nulls().unique()

    # Converte e reforça string no Pandas
    df = df.to_pandas()
    df["UserId"] = df["UserId"].astype(str)  # redundante, mas garante no Pandas

    # Remove registros inválidos com UserId igual a -1
    df = df[df["UserId"] != "-1"].reset_index(drop=True)

    return df
 


