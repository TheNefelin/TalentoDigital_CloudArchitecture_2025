
```sh
unzip code.zip
```

```sh
cd python_3
python3 create_table.py
```

```sh
aws dynamodb list-tables --region us-east-1
```

```sh
aws dynamodb put-item \
--table-name FoodProducts \
--item file://../resources/not_an_existing_product.json \
--region us-east-1
```

```sh
aws dynamodb put-item \
--table-name FoodProducts \
--item file://../resources/an_existing_product.json \
--condition-expression "attribute_not_exists(product_name)" \
--region us-east-1
```

```sh
python3 conditional_put.py
```

```sh
python3 test_batch_put.py
```

```sh
python3 batch_put.py
```

```sh
python3 get_one_item.py
```

```sh
python3 add_gsi.py
```

```sh
python3 scan_with_filter.py
```
