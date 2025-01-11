-- 2
CREATE TABLE product_order (
	product_order_id INTEGER PRIMARY KEY AUTOINCREMENT
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
	UNIQUE(order_id, product_id)
	-- PRIMARY KEY(order_id, product_id)
	FOREIGN KEY (order_id) REFERENCES orders(order_id)
	FOREIGN KEY (product_id) REFERENCES products(product_id)
	);