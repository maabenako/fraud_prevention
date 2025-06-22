# src/fraud_detection/pipelines/enriquecimento/pipeline.py

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import enriquecer_transacoes


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=enriquecer_transacoes,
                inputs=dict(caminho_csv="params:caminho_transacoes"),
                outputs="transacoes_enriquecidas",
                name="node_enriquecimento"
            )
        ]
    )
