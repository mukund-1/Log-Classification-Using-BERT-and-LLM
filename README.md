# Log Classification With Hybrid Classification Framework

This project implements a **hybrid log classification system**, combining three complementary approaches to handle varying levels of complexity in log patterns. The classification methods ensure **flexibility and effectiveness** in processing predictable, complex, and poorly labeled data.

---

## Classification Approaches

1.

### Regular Expression (Regex)

* Handles **simplified and predictable** patterns.
* Ideal for logs that can be matched using predefined rules.

2.

### Sentence Transformer + Logistic Regression

* Targets **complex patterns** when there is **sufficient training data**.
* Uses **Sentence Transformers** to generate embeddings, followed by **Logistic Regression** for classification.

3.

### Large Language Models (LLMs)

* Used when **training data is insufficient**.
* Acts as a **fallback or complementary** method for complex and less structured log data.

---

### Architecture

---

## Folder Structure

| Folder       | Description                                                                                                          |
| ------------ | -------------------------------------------------------------------------------------------------------------------- |
| `training/`  | Contains code for training the sentence transformer + logistic regression model, and for regex-based classification. |
| `models/`    | Stores saved models, including sentence embeddings and the logistic regression model.                                |
| `resources/` | Includes supporting files like test CSVs, output files, and architecture images.                                     |
| *(Root)*     | Contains the FastAPI server file: `server.py`.                                                                       |

---

## ⚙️ Setup Instructions

### 1. Install Dependencies

Ensure Python is installed. Then, install the required libraries:

```bash
pip install -r requirements.txt
```

### 2. Run the FastAPI Server

Start the server using:

```bash
uvicorn server:app --reload
```

Once running, you can access:

* API Root: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Usage

Upload a CSV file containing logs via the FastAPI endpoint. Ensure your file has the following columns:

* `source`
* `log_message`

The system will return a CSV file with an additional column:

* `target_label` → the classified label for each log entry.

---
