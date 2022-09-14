create_table = """
        create table if not exists orders(
        product_name varchar,
        price real,
        currency varchar,
        purchase_date varchar);INSERT INTO orders(product_name,price,currency,purchase_date)
        VALUES ('acer',1540,'byn','02082022'),
        ('toshiba',1890,'byn','28012022'),
        ('hp',540,'usd','21062022'),
        ('apple',1400,'usd','26022022');
        create table if not exists sold(id serial primary key,
        product_name varchar,
        price real,
        currency varchar,
        purchase_date varchar)"""

select_byn = """SELECT * FROM orders WHERE currency = 'byn';"""

insert_converted = """INSERT INTO sold (product_name, price, currency, purchase_date) 
VALUES (%s, %s, %s, %s);"""

copy_el_usd = """insert into sold(product_name,price,currency,purchase_date) 
                    select product_name,price,currency,purchase_date FROM orders 
                    WHERE currency = 'usd';"""

sql_dict = {'create_table': create_table, 'copy_el_usd': copy_el_usd, 'insert_converted': insert_converted,
      'select_byn': select_byn}
