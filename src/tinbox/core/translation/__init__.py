"""Translation engine for Tinbox."""

from tinbox.core.translation.interface import (
    TranslationRequest,
    TranslationResponse,
    ModelInterface,
    TranslationError,
)
from tinbox.core.translation.litellm import LiteLLMTranslator
from tinbox.core.types import TranslationConfig, ModelType


def create_translator(config: TranslationConfig) -> ModelInterface:
    """Create a translator instance based on configuration.

    Args:
        config: Translation configuration

    Returns:
        Configured translator instance
    """
    # Use smaller token limits for local models (LM Studio and Ollama)
    # since they typically have smaller context windows and less capacity
    if config.model in (ModelType.LMSTUDIO, ModelType.OLLAMA):
        max_tokens = 2048  # More conservative for local models
    else:
        max_tokens = 4096  # Standard for cloud models

    translator = LiteLLMTranslator(max_tokens=max_tokens)

    # Create translation request with model-specific parameters
    model_params = {}
    if config.model_name:
        model_params["model_name"] = config.model_name

    return translator


__all__ = [
    "TranslationRequest",
    "TranslationResponse",
    "ModelInterface",
    "TranslationError",
    "LiteLLMTranslator",
    "create_translator",
]
