# PresiboFlow Installation Guide

**PresiboFlow** is an open-source, voice-first agentic AI assistant designed for healthcare professionals—especially doctors, clinics, and hospitals in Nigeria and Africa.

##  What It Helps With
- **Real-time Consultation Support**: Clerking notes analysis and differential diagnosis suggestions.
- **Vital Signs Logging**: Track BP, glucose, heart rate, and more.
- **Automated Documents**: Generate appointment letters, prescriptions, and referrals.
- **Patient Workflows**: Create medication reminders and follow-up schedules.
- **Voice Intelligence**: Passive listening during consultations (vitals extraction).

> [!IMPORTANT]
> PresiboFlow is a support tool, not a certified medical device. Always use your clinical judgment.

---

## System Requirements
- **OS**: Windows 10 / 11 (64-bit) recommended.
- **RAM**: Minimum 8 GB (16 GB+ strongly recommended).
- **Disk Space**: 5–15 GB (depending on AI models).
- **Internet**: Required only for initial download and model setup.

---

##  Installation Methods

### 1. Easiest: Windows .exe (Recommended for Doctors)
*No technical skills, Python, or Docker required.*

1. Go to the [Releases](https://github.com/olivestackscode/PresiboFlow/releases) page.
2. Download `PresiboFlow-Setup.exe`.
3. Double-click to install.
4. **First Launch**:
   - The app will help you install **Ollama** (the local AI engine).
   - It will automatically download a medical-capable model (~4 GB).
5. The dashboard will open in your browser automatically.

### 2. Docker (Reliable & Isolated)
*Best for hospitals with existing IT infrastructure.*

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/).
2. Run in PowerShell:
   ```bash
   git clone https://github.com/olivestackscode/PresiboFlow.git
   cd PresiboFlow
   docker compose up -d
   ```
3. Pull the AI model: `ollama pull llama3.2`

### 3. Manual Python Setup
*For developers and customization.*

1. Install Python 3.11+, Git, and [Ollama](https://ollama.com/).
2. Clone and setup:
   ```bash
   git clone https://github.com/olivestackscode/PresiboFlow.git
   cd PresiboFlow
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Run: `python presiboflow/desktop_entry.py`

---

##  First-Time Setup

1. **Pull the AI Model**: Open PowerShell and run `ollama pull llama3.2`.
2. **Choose Your Role**:
   - **Medical Professional**: Full clinical tools.
   - **Non-Medical**: Administrative automation.
3. **Test It**: Try saying or typing: *"Analyze these clerking notes: 45-year-old male with fever for 3 days."*

---

##  Privacy & Security
- **Local-First**: All AI processing happens on YOUR computer. No patient data is sent to external clouds by default.
- **PHI Redaction**: Built-in settings to redact sensitive identifiers before generating reports.

##  Troubleshooting
- **Ollama not found**: Ensure Ollama is running in your system tray.
- **Slow performance**: Use a smaller model (e.g., `llama3.2`) or upgrade your RAM.
