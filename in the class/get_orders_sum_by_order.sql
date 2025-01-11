select order_id, sum(p.price * po.quantity) as total
from product_order po
join products p on po.product_id = p.product_id
group by order_id;


