# Pipeline: detectar_fraudes
# Objetivo: preparar os dados para modelagem e detectar possíveis fraudes com base em padrões anômalos

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import preparar_dados_modelo, treinar_modelo, avaliar_modelo

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=preparar_dados_modelo,
            inputs="transacoes_enriquecidas",
            outputs="dados_para_modelo",
            name="preparar_dados_modelo_node",
        ),
        node(
            func=treinar_modelo,
            inputs="dados_para_modelo",
            outputs="modelo_fraude",
            name="treinar_modelo_node",
        ),
        node(
            func=avaliar_modelo,
            inputs=dict(modelo="modelo_fraude", dados="dados_para_modelo"),
            outputs="avaliacao_modelo",
            name="avaliar_modelo_node",
        ),
    ])

