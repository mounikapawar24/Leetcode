/* Write your T-SQL query statement below */
select employee_id,
iif (employee_id%2 = 1 and name not like 'M%' , salary , 0) as bonus
from employees 
order by employee_id asc