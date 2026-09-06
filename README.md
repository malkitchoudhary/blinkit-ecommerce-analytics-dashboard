# Blinkit E-Commerce Analytics

A Streamlit business-intelligence dashboard built from the supplied Blinkit-style grocery data. It is an interactive analytical project, not official Blinkit company data.

## Business problem
Leaders need one place to understand sales, customer behavior, delivery reliability, inventory movement, marketing efficiency, and customer voice without duplicating revenue through unsafe joins.

## Data audit and model
The source contains 5,000 unique orders, 5,000 order items, 2,500 customers, 268 products, 5,000 delivery records, 5,000 feedback records, 5,400 marketing records, and 75,172 inventory records. Orders, delivery, items, and feedback join on `order_id`; customers join on `customer_id`; products join on `product_id`.

The order fact remains the revenue authority because item extensions sum to a different total. Product and quantity views use a validated item-to-product many-to-one join. `blinkit_inventory.csv` is used as the inventory movement history. `blinkit_inventoryNew.csv` is excluded: it has mixed month labels and duplicate `(product_id, date)` keys. The Excel files are optional icon assets, not analytical sources.

Cleaning includes explicit datetime parsing, numeric source preservation, a timestamp-derived delivery variance, and an item-value helper. Raw files are never overwritten. Negative source delivery durations are treated as a data-quality issue rather than silently used.

## Dashboard pages
1. Executive Overview
2. Sales Analytics
3. Customer Analytics
4. Product Analytics
5. Delivery Analytics
6. Inventory Analytics
7. Marketing Analytics
8. Feedback Analytics
9. Business Insights

Global filters include order date, area, category, delivery status, and customer. Every page includes filtered order exploration and CSV download.

## KPIs
Revenue, orders, customers, items sold, average order value, on-time delivery rate, average rating, inventory movement units, and repeat rate are calculated only where source columns support them. Inventory value and turnover are intentionally not claimed because no reliable on-hand balance or cost field exists.

## Key insights
The Business Insights page calculates the leading category, highest item-value product, timestamp-based late-delivery share, and average customer rating from the active filtered data. Recommendations are tied directly to those observed values.

## Technologies
Python, Pandas, Plotly, Streamlit.

## Install and run
```powershell
python -m pip install -r requirements.txt
streamlit run app.py
```

Keep the supplied CSV files beside `app.py`. The app uses relative paths and caches source loading.

## Architecture
```text
app.py
pages/                 Streamlit multipage entry points
src/data_loader.py     Cached loading, cleaning, validated joins
src/analytics.py       Filters and reusable aggregations
utils.py               Formatting and Plotly layout
requirements.txt
```

## Data-quality limitations
All 5,000 delivery records have valid timestamps, but the source `delivery_time_minutes` contains 1,563 negative values. Several source identifiers are synthetic-looking and customer names/emails are not fully unique. `inventoryNew` contains 7,359 duplicate rows and 12,534 duplicate product/date keys. Excel icon inspection requires `openpyxl`; these files are not needed to run the analytical dashboard.

## Screenshots
_Add screenshots here after deployment._

## Future improvements
Add a formal data-quality report page, robust outlet/location dimensions when supplied, inventory on-hand snapshots, cost data for profit margin, and automated tests for each validated relationship.

## Interview explanation
I built a grocery-commerce BI dashboard from multiple operational CSV sources. I first audited schemas, grain, missingness, duplicates, date fields, and key overlap. I modeled orders as the revenue fact, kept item analysis at item grain, and used validated many-to-one dimension joins to avoid inflating revenue. I cleaned dates and created auditable delivery variance from promised and actual timestamps. The dashboard gives executives filtered KPI views plus sales, customer, product, delivery, inventory, marketing, feedback, and insight pages. The main recommendations focus on category and product demand, late-delivery operations, and low-rating feedback ownership. A key analytical judgment was refusing to calculate unsupported inventory value, turnover, profit, or fabricated comparisons.

## Resume / portfolio description
Designed and built a modular Streamlit BI dashboard for a multi-source grocery-commerce dataset. Audited 9 CSV and 2 Excel inputs; validated order, customer, product, delivery, feedback, marketing, and inventory relationships; implemented cached Pandas data loading and grain-safe joins; developed interactive Plotly pages for revenue, customer behavior, product demand, last-mile performance, inventory movement, campaign ROAS, and customer feedback; added global filters, CSV export, data explorer, quality flags, and transparent rule-based business insights.
