select distinct City from SampleCustomers order by City asc LIMIT (
select count(distinct City) / 2 as Arbeitsaufwand from SampleCustomers);

select distinct City from SampleCustomers order by City desc LIMIT (
select count(distinct City) / 2 as Arbeitsaufwand from SampleCustomers);