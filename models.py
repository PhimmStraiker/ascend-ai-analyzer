"""
Data models for Ascend AI Analyzer
"""
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class TestStatus(str, Enum):
    PASS = "pass"
    FAIL = "fail"
    UNKNOWN = "unknown"

class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class ControlCategory(str, Enum):
    SECURITY = "Security"
    SAFETY = "Safety"
    TRUST = "Trust"

class AscendTestResult(BaseModel):
    """Individual test result from Ascend AI assessment"""
    id: str
    application_id: str
    straiker_id: str
    assessment_id: str
    control_id: str
    batch_id: int
    timestamp: datetime
    score: float
    status: TestStatus
    product_category: str
    base_prompt: str
    evasions_applied: List[str] = Field(default_factory=list)
    detection_status_code: int
    input_guardrails_false_positive: bool
    input_guardrails_false_negative: bool
    explanation: Optional[str] = None
    chat_history: List[Dict[str, Any]] = Field(default_factory=list)
    user_interaction_record: Dict[str, Any] = Field(default_factory=dict)
    workflow: Dict[str, Any] = Field(default_factory=dict)

class AssessmentSummary(BaseModel):
    """Summary of an entire assessment"""
    assessment_id: str
    application_id: str
    total_tests: int
    passed_tests: int
    failed_tests: int
    unknown_tests: int
    overall_risk_level: RiskLevel
    risk_score: float
    categories_tested: List[str]
    evasions_used: List[str]
    timestamp: datetime

class ControlMetrics(BaseModel):
    """Metrics for a specific control"""
    control_id: str
    control_category: ControlCategory
    total_tests: int
    passed_tests: int
    failed_tests: int
    failure_rate: float
    risk_level: RiskLevel
    evasions_used: List[str]
    common_failure_patterns: List[str]

class EvasionMetrics(BaseModel):
    """Metrics for evasion techniques"""
    evasion_name: str
    total_uses: int
    success_rate: float
    failure_rate: float
    controls_affected: List[str]
    risk_impact: RiskLevel

class RiskAnalysis(BaseModel):
    """Comprehensive risk analysis"""
    overall_risk_score: float
    risk_level: RiskLevel
    critical_vulnerabilities: List[str]
    high_risk_areas: List[str]
    recommended_actions: List[str]
    compliance_issues: List[str]

class GraphNode(BaseModel):
    """Node for graph visualization"""
    id: str
    label: str
    node_type: str
    properties: Dict[str, Any] = Field(default_factory=dict)

class GraphEdge(BaseModel):
    """Edge for graph visualization"""
    source: str
    target: str
    relationship: str
    weight: float = 1.0
    properties: Dict[str, Any] = Field(default_factory=dict)

class DashboardMetrics(BaseModel):
    """Metrics for dashboard display"""
    total_assessments: int
    total_tests: int
    overall_pass_rate: float
    risk_distribution: Dict[str, int]
    top_failing_controls: List[ControlMetrics]
    top_evasions: List[EvasionMetrics]
    recent_trends: Dict[str, Any]
