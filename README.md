# Blood Test Analysis – AI-Powered Health Advisor

This repository contains the **final, working version** of the "Blood Test Analysis" assignment. The application analyzes user-uploaded blood test reports (PDF format), identifies abnormal values, finds relevant research articles, and provides actionable health advice using LLM-powered agents.

---

## Bugs Found & Fixes Implemented

Below is a breakdown of key bugs found in the original code (debug-assignment.zip) and how they were addressed in the fixed version (this repo).

### main.py

| Issue                                      | Fix Implemented                                                              |
| ------------------------------------------ | ---------------------------------------------------------------------------- |
| Incorrect imports and undefined references | Corrected all module imports and ensured LLM/tool references are defined     |
| Missing Streamlit interface                | Implemented file upload, button triggers, and result display using Streamlit |
| Crew kickoff logic missing                 | Added proper initialization and kickoff using the `Crew().kickoff()` pattern |

### agents.py

| Issue                              | Fix Implemented                                                   |
| ---------------------------------- | ----------------------------------------------------------------- |
| `llm = llm` caused undefined crash | Replaced with a correctly instantiated Gemini model               |
| Agent structures invalid           | Rewritten using valid CrewAI `Agent()` instantiation              |
| Missing tool references            | Injected `search_tool`, `web_search_tool` into appropriate agents |

### tools.py

| Issue                      | Fix Implemented                                                          |
| -------------------------- | ------------------------------------------------------------------------ |
| Missing `@tool` decorators | Added decorators to all usable tool functions                            |
| Poor PDF parsing logic     | Rewrote parsing function for better text extraction and keyword matching |

### task.py

| Issue                            | Fix Implemented                                |
| -------------------------------- | ---------------------------------------------- |
| Task definitions incomplete      | Structured prompt flows and agent-task linkage |
| No data output for task chaining | Enabled JSON-based data passing between tasks  |

### Additional Files

#### `medical_crew.py`

- Structured class-based definitions for Blood Test Analyst, Medical Research Specialist, and Holistic Health Advisor agents.
- Injected common LLM instance and tools into relevant roles.

#### `train_agents.py`

- Implements a mock training loop to simulate agent interactions.
- Includes method presence validation and saves agent configuration to JSON.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/cherry-1729-9090/BLOOD_TEST_ANALYSIS.git
cd BLOOD_TEST_ANALYSIS
```

### 2. Set Up Python Environment

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory with the following content:

```
GOOGLE_API_KEY=your_google_api_key
SERPER_API_KEY=your_serper_key
LITELLM_PROVIDER=google
LITELLM_MODEL=gemini-1.5-flash
GOOGLE_APPLICATION_CREDENTIALS=./gcp_key.json
```

> Ensure you have your Google Cloud and Serper credentials available before starting.

### 5. Run the Application

```bash
streamlit run main.py
```

---

## Application Workflow

This application uses Streamlit as the user interface and CrewAI agents for reasoning and task execution.

**Steps:**

1. Upload a valid blood test report (PDF).
2. Application extracts and parses lab data.
3. Three agents collaboratively work to:
   - Analyze the report
   - Find relevant literature
   - Generate holistic health advice
4. Final output is displayed on-screen.

---

## Agent Details

| Agent Role                  | Responsibilities                       | Method                                |
| --------------------------- | -------------------------------------- | ------------------------------------- |
| Blood Test Analyst          | Parse report and flag abnormal markers | `analyze_report(input_data)`          |
| Medical Research Specialist | Search for articles on findings        | `conduct_research(input_data)`        |
| Holistic Health Advisor     | Generate practical recommendations     | `provide_recommendations(input_data)` |

Agents are created and orchestrated using the `MedicalCrew` structure.

---

## Technologies Used

- Python 3.10+
- LangChain / CrewAI
- Google Gemini (via LangChain + LiteLLM)
- PyPDF2
- Streamlit

---

## Directory Structure

```
BLOOD_TEST_ANALYSIS/
├── main.py
├── agents.py
├── tools.py
├── task.py
├── medical_crew.py
├── train_agents.py
├── requirements.txt
├── gcp_key.json
├── README.md
```

---

## Demo Video

Watch the full walkthrough of the working Blood Test Analysis application:

👉 [Click here to view the demo on Google Drive]\([https://drive.google.com/file/d/1a-0mNEsoCkZBa6sreH5U0IWecah-6FBR/view?usp=sharing](https://drive.google.com/file/d/1a-0mNEsoCkZBa6sreH5U0IWecah-6FBR/view?usp=sharing))

## Project Setup Notes

* On the first run, the model will be trained using `train_agents.py`.
  The `.pkl` file is **not included** in the repository to keep it clean and lightweight.
* Similarly, the `db/` folder is excluded from version control because it contains runtime-generated data (e.g., ChromaDB).
* Refer to `.gitignore` for details on excluded files and directories.

---

### .gitignore (Summary)

```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Virtual environments
.venv/
venv/
ENV/
env.bak/

# Environment variables
.env

# VS Code / JetBrains
.vscode/
.idea/

# OS-generated files
.DS_Store
Thumbs.db

# Local DB and vector store
/db/

# Model checkpoints, pickles, and temp files
*.pkl
*.joblib
*.sav

# Logs and reports
*.log

# Misc
*.sqlite3
```

