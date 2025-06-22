"""Project pipelines."""
from __future__ import annotations

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from fraud_detection.pipelines.enriquecimento import pipeline as enriquecimento_pipeline
from fraud_detection.pipelines.detectar_fraudes import create_pipeline as detectar_fraudes_pipeline
from fraud_detection.pipelines.pipeline_visualizacao import pipeline as pipeline_visualizacao



def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines()
    pipelines["__default__"] = sum(pipelines.values())
    return pipelines

