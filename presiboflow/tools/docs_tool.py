from loguru import logger
from typing import Dict, Any

class DocsTool:
    def __init__(self, folder_id: str = None):
        self.folder_id = folder_id

    async def create_document(self, title: str, content: str):
        """Create a Google Doc for referral letters or reports."""
        logger.info(f"Creating document: {title} in folder {self.folder_id}")
        # Integration logic (Google Docs API) would go here
        return {"status": "success", "doc_url": "https://docs.google.com/document/d/mock_id"}
        
    async def generate_referral_letter(self, patient_data: Dict[str, Any]):
        title = f"Referral Letter - {patient_data.get('name', 'Patient')}"
        content = f"Date: {patient_data.get('date')}\nRecipient: {patient_data.get('recipient')}\n\nClinical Summary: {patient_data.get('summary')}"
        return await self.create_document(title, content)

    async def generate_prescription(self, prescription_data: Dict[str, Any]):
        title = f"Prescription - {prescription_data.get('patient_name', 'Patient')}"
        meds = "\n".join([f"- {m['drug']} ({m['dose']}) - {m['freq']} for {m['duration']}" for m in prescription_data.get('medications', [])])
        content = f"Prescription Date: {prescription_data.get('date')}\n\nMedications:\n{meds}\n\nNotes: {prescription_data.get('notes', 'None')}"
        return await self.create_document(title, content)

    async def generate_evaluation_report(self, soap_data: Dict[str, Any]):
        title = f"Clinical Evaluation - {soap_data.get('patient_name', 'Patient')}"
        content = f"SOAP Evaluation Record\n\nS: {soap_data.get('subjective')}\nO: {soap_data.get('objective')}\nA: {soap_data.get('assessment')}\nP: {soap_data.get('plan')}"
        return await self.create_document(title, content)
