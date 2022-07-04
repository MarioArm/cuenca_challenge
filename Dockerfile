FROM python:3.8.13-slim
WORKDIR /challenge
COPY . /challenge
RUN pip install -e .
CMD pytest
ENTRYPOINT ["python3", "/challenge/src/eight_queen/eight_queen_puzzle.py"]
