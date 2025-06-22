from kedro.pipeline import Pipeline, node, pipeline
from .nodes import transformar_com_polars


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=transformar_com_polars,  # ← nome certo da função
            inputs="transacoes_brutas",
            outputs="transacoes_tratadas",
            name="node_etl_transacoes"
        )
    ])



