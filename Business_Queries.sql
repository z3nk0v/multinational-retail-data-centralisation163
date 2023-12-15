-- Task 1. How many stores does the business have and in which countries?
Select country_code,
		count(*) as total_no_stores
from dim_store_details
Where country_code IN ('GB','DE','US')
group by country_code
order by total_no_stores DESC;


-- Task 2. Which locations currently have the most stores?
select locality 
	count(*) as total_no_stores
from dim_store_details
group by locality
order by total_no_stores DESC


-- Task 3. Which months produce the average highest cost of sales typically?
select 
round(sum(product_quantity*productprice.)) as total_sales, month
from orders_table
INNER join dim_date_times on orders_table.date_uuid = dim_date_times.date_uuid
join dim_products on orders_table.product_code
group by dim_dates_times.month
order by sum(orders_table.product_quantity*dim_products.product_price) DESC




select count (orders_table.product_quantity) as number_of_sales
sum (orders_table.product_quantity) as product_quantity_count,
case 
when dim_store_details.store_code = 'WEB-1388012W' then 'Web'
else 'Offline'
end as location
		
		
		
		
from orders_table 
join dim_date_times on  orders_table.date_uuid = dim_date_times.date_uuid
join dim_products on  orders_table.product_code = dim_products.product_code
join dim_store_details on orders_table.store_code = dim_store_details.store_code
group by product_location
ORDER BY sum(orders_table.product_quantity) aSC;
	




select 	dim_store_details.store_type, 
sum (orders_table.product_quantity*dim_products.product_price) as total_sales,
sum(orders_table.product_quantity*dim_products.product_price*100)/(sum(sum(orders_table.product_quantity*dim_products.product_price)) over ()) AS percentage_total(%)
from orders_table
join dim_date_times on  orders_table.date_uuid = dim_date_times.date_uuid
join dim_products on  orders_table.product_code = dim_products.product_code
join dim_store_details on orders_table.store_code = dim_store_details.store_code
group by dim_store_details.store_type
ORDER BY percentage_total DESC;





select dim_date_times.year,dim_date_times.month, round(sum(orders_table.product_quantity*dim_products.product_price)) as total_sales
from orders_table
join dim_date_times on  orders_table.date_uuid = dim_date_times.date_uuid
join dim_products on  orders_table.product_code = dim_products.product_code
join dim_store_details on orders_table.store_code = dim_store_details.store_code
group by 	dim_date_times.month,dim_date_times.year
ORDER BY    sum(orders_table.product_quantity*dim_products.product_price)  DESC;



select sum(dim_store_details.staff_numbers) as total_staff_numbers, dim_store_details.country_code
from dim_store_details
group by dim_store_details.country_code
order by sum(dim_store_details.staff_numbers) DESC


select round(count(orders_table.date_uuid)) as total_sales	, 
dim_store_details.store_type, 
dim_store_details.country_code
from orders_table
join dim_date_times on  orders_table.date_uuid = dim_date_times.date_uuid
join dim_products on  orders_table.product_code = dim_products.product_code
join dim_store_details on orders_table.store_code = dim_store_details.store_code
where dim_store_details.country_code = 'DE'
group by 	dim_store_details.store_type,dim_store_details.country_code
ORDER BY    sum(orders_table.product_quantity*dim_products.product_price)  ASC;

select dim_date_times.year
lead(year, )


-- Task 9. How quickly is the company making sales?
WITH all_orders_by_time AS (
SELECT
    year,
    TO_TIMESTAMP(year || '-' || month || '-' || day || ' ' || timestamp, 'YYYY-MM-DD HH24:MI:SS') AS timestamp
FROM
    orders_table AS ot
INNER JOIN
    dim_date_times AS ddt ON ot.date_uuid = ddt.date_uuid
ORDER BY
    timestamp
), lead_table AS (
SELECT
    year,
    timestamp,
    LEAD(timestamp) OVER (ORDER BY timestamp) AS next
FROM
    all_orders_by_time
)
SELECT
    year,
    AVG(next - timestamp) AS actual_time_taken
FROM
    lead_table
GROUP BY
    year
ORDER BY
    actual_time_taken DESC
LIMIT 5;