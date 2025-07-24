# AI-Powered-Resume-Screening-Tool

## **Overview**
This tool uses NLP and BERT embeddings to rank resumes based on their similarity to a given job description. It allows recruiters to upload PDF resumes and get an AI-based ranking.

## **Features**
- Extracts text from resumes (PDF format).
- Compares resumes to job descriptions using BERT embeddings.
- Provides interactive ranking through a Streamlit web app.

## **Tech Stack**
- Python, Transformers (BERT), PyTorch
- Streamlit (for web UI)
- pdfplumber (for PDF parsing)

## **Setup Instructions**
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

## **Run Web App**
streamlit run src/app.py

