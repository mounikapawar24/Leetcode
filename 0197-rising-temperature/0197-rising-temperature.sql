# Write your MySQL query statement below
select a.id from weather as a
join weather as b
on datediff(a.recorddate,b.recorddate)=1
where a.temperature>b.temperature;