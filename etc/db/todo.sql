create table `task`(
    `id`            INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
    `title`         VARCHAR(255) NOT NULL,
    `description`   VARCHAR(65535) NOT NULL,
    `deadline`      DATETIME NOT NULL,
    `created`       DATETIME NOT NULL,
    `created_by`    INT(11) UNSIGNED NOT NULL,
    PRIMARY KEY(`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table `task_serial_number`(
    `id`            INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
    `serial_no`     INT(11) UNSIGNED NOT NULL,
    `project_id`    INT(11) UNSIGNED NOT NULL,
    `task_id`       INT(11) UNSIGNED NOT NULL,
    UNIQUE(`serial_no`, `project_id`, `task_id`),
    PRIMARY KEY(`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table `task_history`(
    `id`            INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
    `task_id`       INT(11) UNSIGNED NOT NULL,
    `status`        INT(11) NOT NULL,
    `note`          VARCHAR(65535) NOT NULL,
    `modified`      DATETIME NOT NULL,
    `modified_by`   INT(11) UNSIGNED NOT NULL,
    PRIMARY KEY(`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table `project`(
    `id`            INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
    `name`          VARCHAR(255) NOT NULL,
    `description`   VARCHAR(65535) NOT NULL,
    `status`        VARCHAR(2) NOT NULL,
    `created`       DATETIME NOT NULL,
    `created_by`    INT(11) UNSIGNED NOT NULL,
    `modified`      DATETIME NOT NULL,
    `modified_by`   INT(11) UNSIGNED NOT NULL,
    PRIMARY KEY(`id`),
    UNIQUE(name),
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table `user`(
    `id`            INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
    `name`          VARCHAR(255) NOT NULL,
    PRIMARY KEY(`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
