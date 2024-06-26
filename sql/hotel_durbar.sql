create database if not exists hotel_durbar;

use hotel_durbar;

create table if not exists user(
	user_id int(10) primary key auto_increment,
    username varchar(50) not null unique,
    password varchar(20) not null,
    user_type varchar(20) not null,
    user_status varchar(10) not null,
    full_name varchar(50) not null
);

insert into user(username, password, user_type, user_status, full_name) values('admin@gmail.com', 'admin123', 'admin', 'active', 'Admin');

CREATE TABLE IF NOT EXISTS guest (
    guest_id INT(10) PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(20) NOT NULL,
    middle_name VARCHAR(20),
    last_name VARCHAR(20) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    contact VARCHAR(10) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    address TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

create table if not exists room(
	room_id int(10) primary key auto_increment,
    room_number varchar(10) not null unique,
    type varchar(10) not null,
    price double(10, 2) not null,
    status enum('Available', 'Booked', 'Under Maintenance') default 'Available' not null,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

create table if not exists service(
	service_id int(10) primary key auto_increment,
    name varchar(20) not null,
    price double(10, 2) not null,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

create table if not exists booking(
	booking_id int(10) primary key auto_increment,
    check_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    check_out TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status enum('Pending', 'Booked', 'Check Out') default 'Pending' not null,
    guest_id int(10) not null,
    room_id int(10) not null,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

create table if not exists service_request(
	service_request_id int(10) primary key auto_increment,
    quantity int(10) not null,
    total_price double(10, 2) not null,
    booking_id int(10) not null,
    service_id int(10) not null,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Foreign key constraint for booking table
alter table booking add constraint fk_booking_guest_id foreign key (guest_id) references guest (guest_id);
alter table booking add constraint fk_booking_room_id foreign key (room_id) references room (room_id);

-- Foreign key constraint for service request table
alter table service_request add constraint fk_service_request_booking_id foreign key (booking_id) references booking (booking_id);
alter table service_request add constraint fk_service_request_service_id foreign key (service_id) references service (service_id);