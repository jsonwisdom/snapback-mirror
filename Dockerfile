FROM python:3.12-slim

WORKDIR /archive

COPY scripts/ /archive/scripts/
COPY templates/ /archive/templates/

RUN pip install --no-cache-dir hashlib  # already in stdlib

ENTRYPOINT ["python", "/archive/scripts/package_archive.py"]
