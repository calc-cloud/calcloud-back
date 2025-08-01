from enum import Enum


class PredefinedFlowName(Enum):
    """Enum for predefined flow names."""

    ILS_FLOW = "ILS_FLOW"
    SUPPORT_USD_FLOW = "SUPPORT_USD_FLOW"
    AVAILABLE_USD_FLOW = "AVAILABLE_USD_FLOW"
    MIXED_USD_FLOW = "MIXED_USD_FLOW"
    SUPPORT_USD_ABOVE_400K_FLOW = "SUPPORT_USD_ABOVE_400K_FLOW"
    MIXED_USD_ABOVE_400K_FLOW = "MIXED_USD_ABOVE_400K_FLOW"
