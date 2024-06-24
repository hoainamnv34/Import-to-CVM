FROM python:3.9-bullseye

RUN pip3 install requests

COPY import_to_cvm.py /import_to_cvm.py

ENTRYPOINT ["python3", "/import_to_cvm.py"]
