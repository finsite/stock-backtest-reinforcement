"""Processor module for stock-backtest-reinforcement signal generation.

Validates incoming messages and simulates RL policy action selection
based on current market state inputs.
"""

from typing import Any

from app.utils.setup_logger import setup_logger
from app.utils.types import ValidatedMessage
from app.utils.validate_data import validate_message_schema

logger = setup_logger(__name__)


def validate_input_message(message: dict[str, Any]) -> ValidatedMessage:
    """Validate the incoming raw message against the expected schema.

    Args:
        message (dict[str, Any]): Raw input message.

    Returns:
        ValidatedMessage: A validated message object.

    Raises:
        ValueError: If the input format is invalid.

    """
    logger.debug("🔍 Validating message schema...")
    if not validate_message_schema(message):
        logger.error("❌ Invalid message schema: %s", message)
        raise ValueError("Invalid message format")
    return message  # type: ignore[return-value]


def generate_rl_signal(message: ValidatedMessage) -> dict[str, Any]:
    """Simulate an RL policy choosing an action based on market state.

    Args:
        message (ValidatedMessage): The validated input data.

    Returns:
        dict[str, Any]: Message enriched with action and confidence.

    """
    symbol = message.get("symbol", "UNKNOWN")
    logger.info("🧠 Generating RL signal for %s", symbol)

    # Placeholder policy logic (in reality: policy.predict(state_features))
    action = "BUY"
    confidence = 0.82

    result = {
        "rl_action": action,
        "rl_confidence": confidence,
    }

    logger.debug("🎯 RL decision for %s: %s", symbol, result)
    return {**message, **result}
