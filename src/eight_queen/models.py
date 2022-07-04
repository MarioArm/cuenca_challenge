import uuid

import solutions_db

from datetime import datetime
from sqlalchemy import Column, Integer, String, DATETIME


class Solution(solutions_db.Base):
    __tablename__ = 'solutions'
    id = Column(String(36), primary_key=True)
    board_size = Column(Integer, nullable=False)
    possible_solutions = Column(Integer, nullable=False)
    created_at = Column(DATETIME, nullable=False)

    def __init__(self, board_size: int, possible_solutions: int):
        self.id = str(uuid.uuid4())
        self.board_size = board_size
        self.possible_solutions = possible_solutions
        self.created_at = datetime.now()

    def __repr__(self):
        return f'Solution({self.id}, {self.board_size}, {self.possible_solutions})'

    def __str__(self):
        return f'Solution({self.id}, {self.board_size}, {self.possible_solutions})'
