from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]


@st.cache_data(show_spinner=False)
def load_data():
    read = lambda name: pd.read_csv(ROOT / name)
    orders = read("blinkit_orders.csv")
    items = read("blinkit_order_items.csv")
    customers = read("blinkit_customers.csv")
    products = read("blinkit_products.csv")
    delivery = read("blinkit_delivery_performance.csv")
    feedback = read("blinkit_customer_feedback.csv")
    marketing = read("blinkit_marketing_performance.csv")
    inventory = read("blinkit_inventory.csv")

    date_columns = [
        (orders, ["order_date", "promised_delivery_time", "actual_delivery_time"]),
        (customers, ["registration_date"]),
        (delivery, ["promised_time", "actual_time"]),
        (feedback, ["feedback_date"]),
        (marketing, ["date"]),
        (inventory, ["date"]),
    ]
    for frame, columns in date_columns:
        for column in columns:
            # Sources mix ISO timestamps with day-first calendar dates.
            # ``mixed`` infers each source representation independently.
            frame[column] = pd.to_datetime(
                frame[column], errors="coerce", format="mixed", dayfirst=True
            )

    delivery["computed_delivery_minutes"] = (
        delivery["actual_time"] - delivery["promised_time"]
    ).dt.total_seconds().div(60)
    delivery["is_late"] = delivery["computed_delivery_minutes"] > 0
    items["item_value"] = items["quantity"] * items["unit_price"]
    return {"orders": orders, "items": items, "customers": customers, "products": products,
            "delivery": delivery, "feedback": feedback, "marketing": marketing, "inventory": inventory}


def build_order_view(data):
    orders = data["orders"].copy()
    customers = data["customers"].drop_duplicates("customer_id")
    delivery = data["delivery"].drop_duplicates("order_id")
    return (orders.merge(customers[["customer_id", "area", "customer_segment"]], on="customer_id", how="left", validate="many_to_one")
            .merge(delivery[["order_id", "computed_delivery_minutes", "is_late"]], on="order_id", how="left", validate="one_to_one"))


def build_item_view(data):
    return data["items"].merge(data["products"], on="product_id", how="left", validate="many_to_one")
