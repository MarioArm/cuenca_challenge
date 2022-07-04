CREATE TABLE IF NOT EXISTS solutions (
    id VARCHAR(36) PRIMARY KEY,
    board_size INT NOT NULL,
    possible_solutions INT NOT NULL,
    created_at TIMESTAMP NOT NULL
);
