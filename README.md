# 📊 AI Data Analysis Agent

An AI-powered data analysis application built with **Python**, **Streamlit**, and **Claude AI**. Upload a CSV dataset, ask questions in natural language, and receive intelligent insights instantly.

## 🚀 Features

- 📂 Upload CSV datasets
- 🤖 AI-powered data analysis using Claude AI
- 💬 Ask questions in natural language
- 📊 Interactive dataset preview
- ⚡ Fast and user-friendly Streamlit interface
- 🔒 Secure API key management using `.env`

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- Anthropic Claude API
- python-dotenv

## 📂 Project Structure

```text
AI-Data-Analysis-Agent/
│
├── assets/
│   ├── home.jpg
│   ├── dataset-upload.jpg
│   └── ai-analysis.jpg
│
├── src/
│   ├── data_analyzer.py
│   ├── streamlit_analyzer.py
│   └── test_api.py
│
├── .gitignore
├── LICENSE
├── requirements.txt
├── sample_employee_data.csv
└── README.md
```

## 📸 Screenshots

### 🏠 Home Page

![Home](assets/home.jpg)

### 📂 Dataset Upload

![Dataset Upload](assets/dataset-upload.jpg)

### 🤖 AI Analysis

![AI Analysis](assets/ai-analysis.jpg)

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/maliharana607-debug/AI-Data-Analysis-Agent.git
```

Move into the project directory:

```bash
cd AI-Data-Analysis-Agent
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root and add your Anthropic API key:

```env
ANTHROPIC_API_KEY=your_api_key_here
```

## ▶️ Run the Application

```bash
streamlit run src/streamlit_analyzer.py
```

The application will open in your browser at:

```
http://localhost:8501
```


## 📊 Sample Dataset

A sample employee dataset is included to help users quickly test the application and explore its AI-powered analysis capabilities.

## 🔮 Future Improvements

- Support Excel (.xlsx) files
- Interactive charts and visualizations
- Export AI-generated reports
- Data cleaning recommendations
- Multi-file analysis
- Download analysis results


## 📄 License

This project is licensed under the MIT License.


## 👩‍💻 Author

**Maliha Rana**

If you found this project useful, feel free to ⭐ the repository.