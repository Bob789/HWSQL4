select sum(p.price * po.quantity) as "order2 total"
from product_order po
join products p on po.product_id = p.product_id
where order_id = 2;