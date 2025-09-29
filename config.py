"""
Configuration settings for Ascend AI Analyzer
"""
import os
from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = BASE_DIR / "reports"
STATIC_DIR = BASE_DIR / "static"

# Neo4j configuration
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

# Application settings
APP_NAME = "Ascend AI Results Analyzer"
APP_VERSION = "1.0.0"
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Data processing settings
MAX_FILE_SIZE_MB = 100
SUPPORTED_FORMATS = [".csv"]

# Visualization settings
DEFAULT_COLORS = {
    "pass": "#28a745",
    "fail": "#dc3545", 
    "unknown": "#ffc107",
    "high_risk": "#dc3545",
    "medium_risk": "#ffc107",
    "low_risk": "#28a745"
}

# Control categories mapping
CONTROL_CATEGORIES = {
    "harmful_content": "Safety",
    "lava": "Security", 
    "data_leakage": "Security",
    "llm_evasion": "Security",
    "application_grounding": "Trust",
    "system_prompt_leak": "Security",
    "excessive_agency": "Security"
}

# Evasion techniques
EVASION_TECHNIQUES = [
    "typoglycemia",
    "policy_puppetry", 
    "base64_encoding",
    "unicode_encoding",
    "leetspeak",
    "role_playing",
    "jailbreaking",
    "prompt_injection"
]
