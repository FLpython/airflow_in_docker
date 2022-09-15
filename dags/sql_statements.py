create_table = """
        create table if not exists orders(
        id serial,
        product_name varchar,
        price numeric(6,2),
        currency varchar,
        purchase_date date);INSERT INTO orders(product_name,price,currency,purchase_date)
        VALUES ('acer',1540,'byn','08/02/2022'),
        ('toshiba',1890,'byn','01/28/2022'),
        ('hp',540,'usd','06/21/2022'),
        ('apple',1400,'usd','02/26/2022');
        create table if not exists sold(
        id serial primary key,
        product_name varchar,
        price numeric(6,2),
        currency varchar,
        purchase_date date)"""

select_byn = """SELECT product_name, price, currency, purchase_date FROM orders WHERE currency = 'byn';"""

insert_converted = """INSERT INTO sold (product_name, price, currency, purchase_date) 
VALUES (%s, %s, %s, %s);"""

copy_el_usd = """insert into sold(product_name,price,currency,purchase_date) 
                    select product_name,price,currency,purchase_date FROM orders 
                    WHERE currency = 'usd';"""

sql_dict = {'create_table': create_table, 'copy_el_usd': copy_el_usd, 'insert_converted': insert_converted,
      'select_byn': select_byn}
