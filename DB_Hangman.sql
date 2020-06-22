ALTER TABLE sessions
ADD partie INT NOT NULL UNIQUE,
ADD date_sessions DATE NOT NULL,
ADD FOREIGN KEY ( partie ) REFERENCES partie( partie_id );