# 📊 AI Data Analysis Agent

An AI-powered data analysis assistant that enables users to upload CSV datasets, ask questions in natural language, and receive AI-generated insights, summaries, and recommendations using the Claude API.

---

## ✨ Features

- Upload and analyze CSV datasets
- AI-generated data insights
- Natural language question answering
- Automatic data summarization
- Interactive Streamlit interface
- Claude API integration

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- Anthropic Claude API

---

## 🚀 Installation

```bash
git clone https://github.com/maliharana607-debug/Data-Analysis-Agent.git

cd Data-Analysis-Agent

pip install -r requirements.txt

streamlit run src/streamlit_analyzer.py
```

---

## 📌 Usage

1. Add your Anthropic API key to the `.env` file.
2. Launch the Streamlit application.
3. Upload a CSV dataset.
4. Ask questions about your data.
5. View AI-generated insights and summaries.

---

## 📂 Project Structure

```text
Data-Analysis-Agent/
│
├── src/
│   ├── data_analyzer.py
│   ├── streamlit_analyzer.py
│   └── test_api.py
│
├── assets/
├── sample_data.csv
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🔄 Workflow

```text
Upload CSV
      │
      ▼
Read Dataset
      │
      ▼
Process Data
      │
      ▼
Claude API
      │
      ▼
Generate Insights
      │
      ▼
Display Results
```

---

## 🚀 Future Improvements

- Support Excel (.xlsx) files
- Generate charts automatically
- Export AI-generated reports
- Multi-file analysis
- Cloud deployment

---

## 📄 License

This project is licensed under the MIT License.
