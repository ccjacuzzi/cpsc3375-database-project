create database blog;

use blog;

create table blog_user (
	user_id int auto_increment primary key,
    name varchar(50) not null,
    email varchar(100) not null,
    phone int not null
);

alter table blog_user modify column phone varchar(50);
alter table blog_user add password varchar(25);

create table blog_post (
	post_id int auto_increment primary key,
    title varchar(200) not null,
    content varchar(1000) not null,
    user_id int,
    foreign key (user_id) references blog_user(user_id)
);

insert into blog_user(name, email, phone) values
	("Casey Jacuzzi", "ccjacuzzi@ualr.edu", "5017498368"),
    ("Bob Dylan", "bdylan@gmail.com", "5012228888"),
    ("Tom Sylva", "tommys@toh.com", "8889990000");

    
insert into blog_post (title, content, user_id) values
	("My First Post!", "This is my first blog post. I am so happy to have a blog. This is a dream come true!", 1);

select * from blog_user;
select user_id from blog_user where email = "Ironman@marvel.com" AND password = "password";