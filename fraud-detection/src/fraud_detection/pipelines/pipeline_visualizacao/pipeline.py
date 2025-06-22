from kedro.pipeline import Pipeline, node, pipeline
from .nodes import plot_metricas_modelo, plot_fraudes_por_pais, plot_heatmap_correlacoes

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=plot_metricas_modelo,
            inputs="avaliacao_modelo",
            outputs=None,
            name="plot_metricas_modelo_node"
        ),
        node(
            func=plot_fraudes_por_pais,
            inputs="transacoes_enriquecidas",
            outputs=None,
            name="plot_fraudes_por_pais_node"
        ),
        node(
            func=plot_heatmap_correlacoes,
            inputs="transacoes_enriquecidas",
            outputs=None,
            name="plot_heatmap_correlacoes_node"
        ),
    ])
