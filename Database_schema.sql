-- Task 1. Cast the columns of the orders_table to the correct data types.
Alter Table orders_table
Alter column date_uuid TYPE UUID USING date_uuid::UUID,
Alter column user_uuid TYPE UUIDUSING user_uuid::UUID,
Alter column card_number TYPE Varchar(11),
Alter column store_code TYPE varchar(12),
Alter column product_code TYPE varchar(11),
Alter column product_quantity TYPE smallint:


-- Task 2. Cast the columns of the dim_users table to the correct data types.
Alter Table dim_users_table
Alter column first_name TYPE VARCHAR(55),
Alter column last_name TYPE VARCHAR(55),
Alter column date_of_birth TYPE date,
Alter column country code TYPE varchar(2),
Alter column useruuid TYPE uuid USING user_uuid::UUID,
Alter column join_date TYPE date,
ADD primary key(user_uuid);

-- Task 3. Update the dim_store_details table.
Alter Table dim_store_details
Alter column longitude TYPE float,
Alter column locality TYPE VARCHAR(255),
Alter column store_code TYPE  Varchar(12)
Alter column staff_numbers TYPE small int USING staff_numbers::SMALLINT,
Alter column opening_date TYPE date,
Alter column store_type TYPE VARCHAR(255),
ALTER COLUmn store_type DROP NOT NULL,
ALTER COLUMN country_code TYPE VARCHAR(3),
ALTER COLUMN continent TYPE VARCHAR(255),
ADD PRIMARY KEY (store_code);

-- Task 4. Make changes to the dim_products table for the delivery team.
UPDATE dim_products
SET product_price = LTRIM(product_price, '£');
ALTER TABLE dim_products,
Add COLUMN weight_class TYPE VARCHAR(14),
SET weight_class = 
        CASE
            WHEN weight < 2.0 THEN 'Light'
            WHEN weight >= 2.0 AND weight < 40.0 THEN 'Mid_Sized'
            WHEN weight >= 40.0 AND weight < 140.0 THEN 'Heavy'
            WHEN weight >= 140.0 THEN 'Truck_Required'
        END;

-- Task 5. Update the dim_products table with the required data types.
Alter Table dim_products
RENAME removed TO still_available;
Alter column product_price TYPE FLOAT,  
Alter column weight TYPE FLOAT,
Alter column EAN TYPE VARCHAR(17),
Alter column product_code TYPE VARCHAR(11),
Alter column date_added TYPE DATE date_uuid::UUID,
Alter column uuid TYPE UUID,
Alter column still_available TYPE BOOL CASE still_available WHEN 'Still_avaliable' THEN TRUE ELSE FALSE END,
ADD PRIMARY KEY (product_code);

-- Task 6. Update the dim_date_times table.
dim users table:
Alter Table dim_users_table
Alter column first_name TYPE VARCHAR(55),
Alter column last_name TYPE VARCHAR(55),,
Alter column date_of_birth TYPE date,
Alter column country code TYPE varchar(2),
Alter column useruuid TYPE uuid,
Alter column join_date TYPE date,
ADD PRIMARY KEY (date_uuid);

-- Task 7. Update the dim_card_details table
alter table dim_card_details
alter column card_number type varchar(19),
alter column expiry_date type varchar(5),
alter column date_confirmed_payment type date.
ADD PRIMARY KEY (card_number);
-- Task 8. Create the primary keys in the dimension table
-- Task 9. Add foreign keys to the orders table
ALTER TABLE orders_table
    ADD FOREIGN KEY (date_uuid) REFERENCES dim_date_times(date_uuid),
    ADD FOREIGN KEY (user_uuid) REFERENCES dim_users(user_uuid),
    ADD FOREIGN KEY (card_number) REFERENCES dim_card_details(card_number),
    ADD FOREIGN KEY (store_code) REFERENCES dim_store_details(store_code),
    ADD FOREIGN KEY (product_code) REFERENCES dim_products(product_code);





