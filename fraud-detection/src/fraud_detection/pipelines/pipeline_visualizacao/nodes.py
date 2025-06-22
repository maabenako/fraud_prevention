import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def plot_metricas_modelo(relatorio: pd.DataFrame):
    relatorio = relatorio.drop(index=["accuracy", "macro avg", "weighted avg"], errors="ignore")

    relatorio[["precision", "recall", "f1-score"]].plot(kind="bar")
    plt.title("Desempenho por Classe")
    plt.tight_layout()
    path = Path("data/09_visuals/metricas_modelo.png")
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(path)
    plt.close()

def plot_fraudes_por_pais(dados: pd.DataFrame):
    df = dados.copy()
    top_paises = df[df["is_fraud"] == 1]["Country"].value_counts().nlargest(10)
    top_paises.plot(kind="barh", title="Top 10 Países com Mais Fraudes")
    plt.tight_layout()
    plt.savefig("data/09_visuals/fraudes_por_pais.png")
    plt.close()

def plot_heatmap_correlacoes(dados: pd.DataFrame):
    corr = dados.select_dtypes(include='number').corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlação entre Variáveis")
    plt.tight_layout()
    plt.savefig("data/09_visuals/correlacoes.png")
    plt.close()

