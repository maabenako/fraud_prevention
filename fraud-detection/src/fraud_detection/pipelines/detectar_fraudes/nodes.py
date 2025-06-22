#src/fraud_detection/pipelines/detectar_fraudes/nodes.py

# src/fraud_detection/pipelines/detectar_fraudes/nodes.py

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd


def preparar_dados_modelo(dados: pd.DataFrame) -> pd.DataFrame:
    dados = dados.copy()

    # ✅ Garante que a coluna 'is_fraud' existe
    if "is_fraud" not in dados.columns:
        raise ValueError("A coluna 'is_fraud' não foi encontrada nos dados enriquecidos.")

    # ✅ Garante tipo int (evita erro de string/float)
    dados["is_fraud"] = dados["is_fraud"].astype(int)

    # Seleciona features numéricas
    features = [
        "NumberOfItemsPurchased", "CostPerItem", "ValorTotal",
        "GastoMensal", "MediaGastoUser", "FrequenciaMensal", "TempoDesdeUltima"
    ]

    X = dados[features].fillna(0)
    y = dados["is_fraud"]

    # Normalização
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Junta com target e devolve dataframe pronto para modelagem
    df_modelo = pd.DataFrame(X_scaled, columns=features)
    df_modelo["is_fraud"] = y.reset_index(drop=True)
    return df_modelo


def treinar_modelo(dados: pd.DataFrame):
    from sklearn.ensemble import RandomForestClassifier

    X = dados.drop(columns=["is_fraud"])
    y = dados["is_fraud"]

    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)

    return modelo


def avaliar_modelo(modelo, dados):
    from sklearn.metrics import classification_report

    if "is_fraud" not in dados.columns:
        raise ValueError("A coluna 'is_fraud' não foi encontrada nos dados para avaliação.")

    X = dados.drop(columns=["is_fraud"])
    y = dados["is_fraud"].astype(int)

    y_pred = modelo.predict(X)
    relatorio = classification_report(y, y_pred, output_dict=True)

    return pd.DataFrame(relatorio).transpose()
