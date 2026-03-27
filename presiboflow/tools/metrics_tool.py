from loguru import logger
from typing import Dict, Any

class MetricsTool:
    async def log_vitals(self, vitals: Dict[str, Any]):
        """Log vital signs to the patient metric database."""
        logger.info(f"Logging vitals: {vitals}")
        # Logic to save to database or EHR integration
        return {"status": "success", "metrics_captured": list(vitals.keys())}
        
    async def detect_anomaly(self, metrics: Dict[str, Any]):
        """Simple rule-based anomaly detection for vitals."""
        anomalies = []
        if float(metrics.get("bp_systolic", 0)) > 140:
            anomalies.append("High Blood Pressure")
        return anomalies
