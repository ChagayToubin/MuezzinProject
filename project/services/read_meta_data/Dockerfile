FROM python:3.10-slim

WORKDIR /app/project


COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY project ./project
# COPY project/services /app/project/services
# COPY  project/utilities /app/ project/utilities
# COPY project/services/read_meta_data /app/project/services/read_meta_data

# COPY project/config/settings /app/project/config/settings
# COPY project/services/read_meta_data/manager /app/project/services/read_meta_data/manager
# COPY project/utilities/logger /app/project/utilities/logger

CMD ["python", "-m", "project.services.read_meta_data.main"]