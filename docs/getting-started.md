# Getting Started with PresiboFlow

Follow these steps to get your voice-first healthcare framework up and running.

## 1. Environment Setup

### Clone the Repository
```bash
git clone https://github.com/your-org/presiboflow.git
cd presiboflow
```

### Configure Environment Variables
Copy the template and fill in your keys:
```bash
cp .env.example .env
```
Key variables to set:
- `LIVEKIT_URL`, `LIVEKIT_API_KEY`, `LIVEKIT_API_SECRET`
- `OPENAI_API_KEY` (if using OpenAI) or `OLLAMA_BASE_URL` (if using local LLMs)

## 2. Running with Docker (Recommended)

The easiest way to start PresiboFlow is using Docker Compose:

```bash
docker compose up -d
```

This starts:
1. The **LiveKit Agent Worker**: Listens for room connections and processes audio.
2. (Optional) **Ollama**: If un-commented in `docker-compose.yml`.

## 3. Local Development Setup

If you prefer running without Docker:

### Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
pip install -e .
```

### Start the Worker in Dev Mode
```bash
python -m presiboflow.core.livekit_worker dev
```

## 4. Testing the Voice Pipeline

1. Open `frontend/index.html` in your browser.
2. Select a role (e.g., **Doctor**).
3. Click **"Start Listening"**.
4. Speak clinical intents like:
   - *"Schedule an appointment for next Tuesday at 10 AM."*
   - *"Patient's BP is 120/80 and heart rate is 72."*
5. Watch the **Real-time Insights** sidebar for detected actions and metrics.

## 5. Building Workflows

Navigate to `frontend/canvas.html` to design your own patient journey flows using the drag-and-drop builder.
