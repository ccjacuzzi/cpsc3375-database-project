create database dropship;
use dropship;

/* 
supplier_address
A supplier may have more than one address. This table links supplier IDs with address 
IDs to make a list of supplier addresses. The supplier table has columns to hold three
supplier_address_id records.
*/
create table supplier_address (
	supplier_address_id int,
    supplier_id int,
    address_id int,
    primary key (supplier_address_id)
);

alter table supplier_address modify column supplier_address_id int auto_increment not null;
alter table supplier_address modify column supplier_id int not null;
alter table supplier_address modify column address_id int not null;
alter table supplier_address add foreign key (supplier_id) references supplier(supplier_id);
alter table supplier_address add foreign key (address_id) references address(address_id);

## How do I instert tuples into a table that automatically increments the PK and only has FKs as the remaining values?

create table address(
	address_id int,
    street varchar(50),
    city varchar(25),
    state varchar(2),
    zipcode int,
    primary key (address_id)
);

create table customer_address (
	customer_address_id int,
    customer_id int,
    address_id int,
    primary key (customer_address_id)
);

create table login (
	login_id int,
    username varchar(25),
    password varchar(25),
    type varchar(25),
    primary key (login_id)
);

create table supplier (
	supplier_id int,
    sales_rep_name varchar(50),
    phone int,
    supplier_address_id int,
    primary key (supplier_id)
);

create table customer (
	customer_id int,
    name varchar(50),
    customer_address_id int,
    email varchar(50),
    login_id int,
    customer_start_date date,
    birthday date,
    customer_type varchar(25),
    primary key (customer_id)
);

create table employee (
	employee_id int,
    name varchar(50),
    email varchar(50),
    login_id int,
    hire_date date,
    birthday date,
    supervisor varchar(50),
    position varchar(25),
    pay_grade int,
    primary key (employee_id)
);

create table sales_order (
	sales_order_number int,
    customer_id int,
    order_date date,
    delivery_date date,
    primary key (sales_order_number)
);

create table return_request (
	return_id int,
    customer_id int,
    date_requested date,
    date_received date,
    return_reason varchar(2000),
    sales_order_number int,
    employee_id int,
    primary key (return_id)
);

create table purchase_order (
	purchase_order_id int,
    sales_order_number int,
    order_date date,
    delivery_date date,
    employee_id int,
    primary key (purchase_order_id)
);

create table sales_line_item (
	sales_order_number int,
    product_id int,
    quantity int
);

create table return_line_item (
	return_id int,
    product_id int,
    quantity int
);

create table purchase_order_line_item (
	purchase_order_id int,
    product_id int,
    quantity int
);

create table product (
	product_id int,
    supplier_part_number int,
    name varchar(25),
    supplier_id int,
    category varchar(25)
);

create table inventory (
	product_id int,
    quantity int,
    warehouse_location varchar(25)
);




show tables;




