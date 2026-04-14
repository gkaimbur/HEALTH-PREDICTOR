FROM python:3.11-slim

WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY app.py .
COPY train_classification_model.py .
COPY train_birth_weight_model.py .
COPY Maternal_Risk.csv .
COPY birth_weight_dataset.csv .

# Create directories for artifacts and visualizations
RUN mkdir -p artifacts visualizations/classification visualizations/birth_weight

# Copy artifact files if they exist
COPY artifacts/ artifacts/ 2>/dev/null || true

# Expose port for Streamlit (default 8501)
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
