FROM python:3.10-slim

WORKDIR /app/project


COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
COPY project/__init__.py /project/__init__.py
COPY project/services/__init__.py /app/project/services/__init__.py
COPY  project/utilities/__init__.py /app/ project/utilities/__init__.py
COPY project/services/read_meta_data/__init__.py /app/project/services/read_meta_data/__init__.py
COPY project/config/settings /app/project/config/settings
COPY project/services/read_meta_data/manager /app/project/services/read_meta_data/manager
COPY project/utilities/logger /app/project/utilities/logger

CMD ["python", "-m", "project.services.read_meta_data.main"]