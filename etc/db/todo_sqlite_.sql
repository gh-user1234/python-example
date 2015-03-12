create table task(
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    title       TEXT    NOT NULL,
    timelimit   TEXT    NOT NULL
);

create table task_log(
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id     INTEGER NOT NULL,
    timestamp   TEXT    NOT NULL,
    note        TEXT    NOT NULL,
    status      INTEGER NOT NULL,
    user_id     INTEGER NOT NULL
);

create table task_serial_number(
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    serial_no     INTEGER  NOT NULL,
    project_id    INTEGER  NOT NULL,
    task_id       INTEGER  NOT NULL,
    UNIQUE(project_id, task_id)
);

create table project(
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    name            TEXT        NOT NULL,
    description     TEXT        NOT NULL,
    status          INTEGER     NOT NULL,
    created         TEXT        NOT NULL,
    user_id         INTEGER     NOT NULL
);

create table user(
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT NOT NULL
);
