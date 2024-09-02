CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    topic VARCHAR(255),
    question_text TEXT,
    difficulty_level INT
);

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    progress JSONB
);
