DROP DATABASE IF EXISTS `nidus`;
CREATE DATABASE `nidus`;
USE `nidus`;

CREATE TABLE `user` (
  `id` varchar(255) NOT NULL,
  `tw_id` varchar(255) NOT NULL,
  `tw_name` varchar(255),
  `tw_access_token` varchar(255) NOT NULL,
  `tw_access_token_verifier` varchar(255) NOT NULL,
  `tw_profile_picture` varchar(255),
  `tw_email` varchar(100) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `settings` (
  `id` varchar(255) NOT NULL,
  `user_id` varchar(255) NOT NULL,
  `note` boolean NOT NULL DEFAULT true,
  `task` boolean NOT NULL DEFAULT true,
  `reminder` boolean NOT NULL DEFAULT true,
  `email` boolean NOT NULL DEFAULT false,
  `push` boolean NOT NULL DEFAULT true,
  PRIMARY KEY (`id`),
  KEY `settings_user_fk` (`user_id`),
  CONSTRAINT `settings_user_fk` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `session` (
	`id` varchar(255) NOT NULL,
    `user_id` varchar(255) NOT NULL,
    `access_token` varchar(255) NOT NULL,
    `active` boolean NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `end_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`),
	KEY `session_user_fk` (`user_id`),
	CONSTRAINT `session_user_fk` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `notes` (
	`id` varchar(255) NOT NULL,
    `tweet_id` varchar(255),
    `user_id` varchar(255) NOT NULL,
    `content` varchar(300) NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`),
	KEY `notes_user_fk` (`user_id`),
	CONSTRAINT `notes_user_fk` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `reminders` (
	`id` varchar(255) NOT NULL,
    `tweet_id` varchar(255),
    `user_id` varchar(255) NOT NULL,
    `content` varchar(300) NOT NULL,
    `date` DATETIME NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`),
	KEY `reminders_user_fk` (`user_id`),
	CONSTRAINT `reminders_user_fk` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `tasklists` (
	`id` varchar(255) NOT NULL,
    `tweet_id` varchar(255),
    `user_id` varchar(255) NOT NULL,
    `content` varchar(300) NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`),
	KEY `tasklists_user_fk` (`user_id`),
	CONSTRAINT `tasklists_user_fk` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `tasks` (
	`id` varchar(255) NOT NULL,
    `tasklist_id` varchar(255) NOT NULL,
    `content` varchar(300) NOT NULL,
	PRIMARY KEY (`id`),
	KEY `tasks_tasklists_fk` (`tasklist_id`),
	CONSTRAINT `tasks_tasklists_fk` FOREIGN KEY (`tasklist_id`) REFERENCES `tasklists` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;