CREATE TABLE users (
id bigint unsigned auto_increment primary key,
name varchar(100) not null,
email varchar(255) not null unique,
password_hash varchar(255) not null,
is_verified boolean not null default false,
created_at timestamp default current_timestamp
);
CREATE TABLE notes (
id bigint unsigned auto_increment primary key,
user_id bigint unsigned not null,
title varchar(150) not null,
content text not null,
created_at timestamp default current_timestamp,
updated_at timestamp default current_timestamp on update current_timestamp,
 FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE
);
CREATE TABLE file_data (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT UNSIGNED NOT NULL,
    original_name VARCHAR(255) NOT NULL,
    stored_name VARCHAR(255) NOT NULL,
    mime_type VARCHAR(128) NOT NULL,
    size_bytes BIGINT UNSIGNED NOT NULL,
    storage_path VARCHAR(500),
    FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE
);