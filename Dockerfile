# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY  Ass.py random_paragraphs.txt  ./

# Install NLTK and download required resources
RUN pip install --no-cache-dir nltk && \
    python -m nltk.downloader punkt && \
    python -m nltk.downloader stopwords

# Run the Python script when the container launches
CMD ["python", "Ass.py"]
