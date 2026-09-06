def kpis(data):
    orders, items, delivery = data["orders"], data["items"], data["delivery"]
    return {
        "Revenue": orders["order_total"].sum(),
        "Orders": orders["order_id"].nunique(),
        "Customers": orders["customer_id"].nunique(),
        "Items sold": items["quantity"].sum(),
        "AOV": orders["order_total"].mean(),
        "On-time": (delivery["delivery_status"] == "On Time").mean(),
        "Rating": data["feedback"]["rating"].mean(),
        "Inventory units": int((data["inventory"]["stock_received"] - data["inventory"]["damaged_stock"]).sum()),
        "Repeat rate": (data["customers"]["total_orders"] > 1).mean(),
    }


def apply_filters(data, filters):
    orders = data["orders"]
    if filters.get("dates"):
        start, end = filters["dates"]
        orders = orders[orders["order_date"].dt.date.between(start, end)]
    for column in ["delivery_status"]:
        if filters.get(column) and filters[column] != "All":
            orders = orders[orders[column] == filters[column]]
    if filters.get("customer_id") and filters["customer_id"] != "All":
        orders = orders[orders["customer_id"] == filters["customer_id"]]
    if filters.get("area") and filters["area"] != "All":
        ids = set(data["customers"].loc[data["customers"]["area"] == filters["area"], "customer_id"])
        orders = orders[orders["customer_id"].isin(ids)]
    if filters.get("category") and filters["category"] != "All":
        joined = data["items"].merge(data["products"], on="product_id", validate="many_to_one")
        ids = set(joined.loc[joined["category"] == filters["category"], "order_id"])
        orders = orders[orders["order_id"].isin(ids)]
    order_ids = set(orders["order_id"])
    result = dict(data)
    result["orders"] = orders
    result["items"] = data["items"][data["items"]["order_id"].isin(order_ids)]
    result["delivery"] = data["delivery"][data["delivery"]["order_id"].isin(order_ids)]
    result["feedback"] = data["feedback"][data["feedback"]["order_id"].isin(order_ids)]
    return result


def category_sales(data):
    items = data["items"].merge(data["products"][["product_id", "category"]], on="product_id", validate="many_to_one")
    return items.groupby("category", as_index=False).agg(revenue=("item_value", "sum"), quantity=("quantity", "sum")).sort_values("revenue", ascending=False)


def product_sales(data):
    items = data["items"].merge(data["products"][["product_id", "product_name", "category"]], on="product_id", validate="many_to_one")
    return items.groupby(["product_id", "product_name", "category"], as_index=False).agg(revenue=("item_value", "sum"), quantity=("quantity", "sum")).sort_values("revenue", ascending=False)
