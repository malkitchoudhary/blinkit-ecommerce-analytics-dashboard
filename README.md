# 🛒 Blinkit E-Commerce Analytics Dashboard

### End-to-End Business Intelligence & Data Analytics Project

An interactive, portfolio-ready **E-Commerce Business Intelligence Dashboard** built using **Python, Pandas, Plotly and Streamlit** to analyze sales, customers, products, delivery operations, inventory, marketing performance and customer feedback.

> **Disclaimer:** This is a Blinkit-inspired analytics project created for educational and portfolio purposes. It is not an official Blinkit application and does not represent official Blinkit internal data.

---

## 📌 Project Overview

The **Blinkit E-Commerce Analytics Dashboard** is an end-to-end Data Analytics and Business Intelligence project designed to transform multiple raw e-commerce datasets into meaningful business insights.

The project brings together different business functions into one centralized interactive dashboard:

- 💰 Sales & Revenue
- 🛒 Orders & Order Items
- 👥 Customer Analytics
- 📦 Product Analytics
- 🚚 Delivery Analytics
- 🏪 Inventory Analytics
- 📢 Marketing Analytics
- ⭐ Customer Feedback
- 💡 Business Insights

The objective is to help business stakeholders understand performance, identify trends, discover operational problems and make data-driven decisions.

---

# 🎯 Business Problem

E-commerce businesses generate large volumes of data across multiple departments. When this data is stored in separate files, it becomes difficult to get a complete view of business performance.

Important business questions include:

- What is the total revenue?
- How many orders are being generated?
- Which products generate the most revenue?
- Which categories perform best?
- Which customers are the most valuable?
- Which locations perform better?
- Are deliveries happening on time?
- Which products have inventory problems?
- Which marketing campaigns perform best?
- How satisfied are customers?
- What areas require immediate business attention?

This project solves these problems by combining multiple datasets and converting them into a centralized interactive Business Intelligence application.

---

# 🎯 Project Objectives

The major objectives of this project are:

1. Analyze overall sales performance.
2. Track revenue and order trends.
3. Identify top-performing products.
4. Identify underperforming products.
5. Analyze category performance.
6. Understand customer purchasing behavior.
7. Analyze customer value and repeat purchasing where supported.
8. Evaluate delivery performance.
9. Identify inventory risks.
10. Analyze marketing effectiveness.
11. Analyze customer ratings and feedback.
12. Generate actionable business insights.
13. Provide data-driven recommendations.
14. Build a professional portfolio-level Data Analyst project.

---

# 🔄 Complete End-to-End Data Analytics Workflow

Business Problem
        ↓
Data Collection
        ↓
Raw CSV / Excel Files
        ↓
Data Inspection
        ↓
Data Profiling
        ↓
Data Cleaning
        ↓
Data Validation
        ↓
Relationship Identification
        ↓
Data Modeling
        ↓
Data Transformation
        ↓
Exploratory Data Analysis
        ↓
KPI Calculation
        ↓
Business Analysis
        ↓
Interactive Visualization
        ↓
Streamlit Dashboard
        ↓
Business Insights
        ↓
Business Recommendations
        ↓
Data-Driven Decisions

---

# 📂 Data Sources

The project works with multiple datasets covering different areas of the business.

| Dataset | Purpose |
|---|---|
| `blinkit_customers.csv` | Customer information and customer analysis |
| `blinkit_orders.csv` | Order-level transaction analysis |
| `blinkit_order_items.csv` | Product-level order and quantity analysis |
| `blinkit_products.csv` | Product and category information |
| `blinkit_inventory.csv` | Inventory and stock analysis |
| `blinkit_inventoryNew.csv` | Inventory snapshot/version comparison |
| `blinkit_delivery_performance.csv` | Delivery and operational performance |
| `blinkit_marketing_performance.csv` | Marketing and campaign performance |
| `blinkit_customer_feedback.csv` | Customer ratings and feedback |
| `Category_Icons.xlsx` | Category visual assets |
| `Rating_Icon.xlsx` | Rating visual assets |

---

# 🏗️ Project Architecture

The project is structured into separate application, analytical, styling and UI components.

    blinkit-ecommerce-analytics-dashboard/
    │
    ├── app.py
    │
    ├── pages/
    │   ├── 01_Executive_Overview.py
    │   ├── 02_Sales_Analytics.py
    │   ├── 03_Customer_Analytics.py
    │   ├── 04_Product_Analytics.py
    │   ├── 05_Delivery_Analytics.py
    │   ├── 06_Inventory_Analytics.py
    │   ├── 07_Marketing_Analytics.py
    │   ├── 08_Feedback_Analytics.py
    │   └── 09_Business_Insights.py
    │
    ├── src/
    │   ├── analytics.py
    │   ├── data_loader.py
    │   ├── data_model.py
    │   ├── styles.py
    │   └── ui_components.py
    │
    ├── assets/
    │   ├── Category_Icons.xlsx
    │   └── Rating_Icon.xlsx
    │
    ├── data/
    │   └── Dataset files
    │
    ├── app.py
    ├── utils.py
    ├── requirements.txt
    ├── .gitignore
    └── README.md

---

# 🔗 Data Relationship Concept

The analytical model connects the major business entities through validated keys.

    CUSTOMERS
        │
        │ customer_id
        ↓
      ORDERS
        │
        │ order_id
        ↓
    ORDER_ITEMS
        │
        │ product_id
        ↓
     PRODUCTS
        │
        ↓
    INVENTORY


    ORDERS ───────────────→ DELIVERY

    CUSTOMERS ────────────→ FEEDBACK

    MARKETING ────────────→ CAMPAIGN PERFORMANCE

Relationships are validated against the actual datasets before analysis.

Special attention is given to joins to prevent duplicated orders, duplicated revenue and incorrect aggregations.

---

# 🧹 Data Cleaning & Preparation

The project follows a structured data preparation process.

### Data Cleaning Steps

1. Load CSV and Excel datasets.
2. Inspect dataset structure.
3. Identify columns and data types.
4. Check missing values.
5. Check duplicate records.
6. Validate primary keys.
7. Validate foreign keys.
8. Convert date/time columns.
9. Standardize categorical values.
10. Convert numeric fields.
11. Identify invalid records.
12. Validate dataset relationships.
13. Create analytical datasets.
14. Validate important calculations.

Raw data is preserved and analytical transformations are handled separately.

---

# 🔍 Data Quality Checks

The project validates:

- Missing values
- Duplicate records
- Data types
- Date fields
- Numeric fields
- Primary keys
- Foreign keys
- Orphan records
- Invalid values
- Duplicate transactions
- Incorrect joins
- Revenue duplication
- Aggregation accuracy

This helps ensure that the dashboard presents reliable analytical results.

---

# 📊 Dashboard Structure

The application contains nine major analytical sections:

1. Executive Overview
2. Sales Analytics
3. Customer Analytics
4. Product Analytics
5. Delivery Analytics
6. Inventory Analytics
7. Marketing Analytics
8. Feedback Analytics
9. Business Insights

---

# 1️⃣ Executive Overview

The Executive Overview provides a high-level summary of business performance.

### Key KPIs

- Total Sales
- Average Sales / Average Order Value
- Total Items
- Average Rating
- Total Orders
- Other relevant supported business KPIs

### Visualizations

- Revenue trend
- Order trend
- Category performance
- Outlet/location performance
- Delivery reliability
- KPI cards
- High-level business performance

### Purpose

This page provides a quick management-level view of the overall business.

---

# 2️⃣ Sales Analytics

The Sales Analytics page focuses on revenue and transaction performance.

### Analysis

- Total revenue
- Order trends
- Revenue trends
- Average Order Value
- Category-wise revenue
- Product-wise revenue
- Location-wise sales
- Top-performing products
- Bottom-performing products
- Quantity sold
- Revenue contribution
- Sales growth

### Business Questions

- Which products generate the most revenue?
- Which categories contribute the most sales?
- Which locations perform best?
- How does revenue change over time?
- Which products are underperforming?

---

# 3️⃣ Customer Analytics

The Customer Analytics page focuses on customer behavior and value.

### Analysis

- Total customers
- Customer revenue
- Orders per customer
- Average revenue per customer
- Customer purchase frequency
- Top customers
- Repeat customers where supported
- Customer segmentation where supported

### Business Questions

- Who are the highest-value customers?
- Which customers purchase most frequently?
- Which customer groups generate the most revenue?
- What is the repeat purchase behavior?

---

# 4️⃣ Product Analytics

The Product Analytics page analyzes product performance.

### Analysis

- Top products by revenue
- Top products by quantity
- Bottom-performing products
- Category performance
- Product pricing
- Product contribution
- Product demand
- Rating vs sales where supported

### Business Questions

- Which products are most popular?
- Which products generate the highest revenue?
- Which products are underperforming?
- Does product rating relate to sales performance?

---

# 5️⃣ Delivery Analytics

The Delivery Analytics page evaluates last-mile operational performance.

### Analysis

- Average delivery time
- Delivery status
- On-time delivery
- Delayed deliveries
- Cancelled orders
- Delivery performance by location
- Delivery trends
- Delivery-time distribution

### Business Questions

- Which locations have delivery problems?
- What percentage of deliveries are delayed?
- Which areas have operational bottlenecks?
- How reliable is the delivery operation?

---

# 6️⃣ Inventory Analytics

The Inventory Analytics page focuses on inventory health.

### Analysis

- Inventory quantity
- Stock availability
- Low-stock products
- Out-of-stock products
- Inventory by category
- Inventory by location
- Inventory risk
- Stock vs demand

### Business Questions

- Which products are at risk of stockout?
- Which products have excessive inventory?
- Which categories require additional stock?
- Which locations have inventory issues?

---

# 7️⃣ Marketing Analytics

The Marketing Analytics page evaluates marketing effectiveness.

### Analysis

- Marketing spend
- Campaign performance
- Revenue generated
- Marketing channels
- Customer acquisition
- ROAS where supported
- Campaign comparison

### Business Questions

- Which campaign performs best?
- Which marketing channel generates the strongest return?
- Where is marketing spending most effective?
- Which campaigns deserve additional investment?

---

# 8️⃣ Feedback Analytics

The Feedback Analytics page analyzes customer satisfaction.

### Analysis

- Average rating
- Rating distribution
- Product ratings
- Category ratings
- Location ratings
- Feedback trends
- Customer complaints/themes where supported

### Business Questions

- How satisfied are customers?
- Which products receive low ratings?
- Which areas have customer experience problems?
- What are the most common customer concerns?

---

# 9️⃣ Business Insights

The Business Insights page converts analytical findings into actionable recommendations.

Instead of only displaying charts, this section focuses on:

### What Happened?

Identify important trends and changes.

### Why Does It Matter?

Explain the potential business impact.

### What Should Be Done?

Provide a practical data-driven recommendation.

Example:

Finding:
A specific category contributes a significant share of total revenue.

Impact:
A decline in demand for this category could materially affect overall revenue.

Recommendation:
Prioritize inventory availability and promotional planning for this category.

All insights are based on actual calculated values from the dataset.

No fake statistics or fabricated findings are used.

---

# 📌 KPI Framework

The dashboard calculates relevant KPIs based on the available dataset.

## 💰 Sales KPIs

- Total Revenue
- Total Orders
- Average Order Value
- Total Items Sold
- Revenue Growth
- Category Contribution

## 👥 Customer KPIs

- Total Customers
- Average Revenue per Customer
- Orders per Customer
- Repeat Customer Rate where supported

## 🚚 Delivery KPIs

- Average Delivery Time
- On-Time Delivery Rate
- Delayed Delivery Rate
- Cancellation Rate

## 📦 Inventory KPIs

- Total Stock
- Out-of-Stock Rate
- Low-Stock Products
- Inventory Value where supported

## 📢 Marketing KPIs

- Marketing Spend
- Revenue Generated
- ROAS where supported
- Campaign Performance

## ⭐ Feedback KPIs

- Average Rating
- Rating Distribution
- Product Rating
- Category Rating

> Unsupported metrics are not fabricated. A KPI is calculated only when the available data is sufficient.

---

# 🎨 UI/UX Design

The dashboard uses a modern, professional Business Intelligence interface.

### Design Features

- 🟡 Blinkit-inspired yellow branding
- 🟢 Green primary accent
- 🎨 Color-coded navigation
- 📊 Modern KPI cards
- 📈 Interactive Plotly charts
- 🧱 Rounded cards
- 🌫️ Soft shadows
- 📐 Consistent spacing
- 🖥️ Responsive layout
- 🔎 Interactive filters
- 📥 CSV download
- ✨ Custom CSS
- 🎯 Clear visual hierarchy

The goal is to make the application look like a professional BI product instead of a default Streamlit dashboard.

---

# 🎨 Navigation Theme

Each page has a subtle visual identity while maintaining one consistent application theme.

| Page | Accent |
|---|---|
| Executive Overview | Green + Yellow |
| Sales Analytics | Blue |
| Customer Analytics | Purple |
| Product Analytics | Orange |
| Delivery Analytics | Red |
| Inventory Analytics | Teal |
| Marketing Analytics | Violet |
| Feedback Analytics | Cyan |
| Business Insights | Coral |

---

# 🔎 Interactive Features

The dashboard provides:

- Date range filters
- Location filters
- Category filters
- Product filters
- Order status filters
- Delivery status filters
- Rating filters
- Interactive Plotly charts
- Hover tooltips
- Sortable tables
- Search functionality
- CSV download
- Reset filters

Filters dynamically update relevant KPIs and visualizations.

---

# 📱 Responsive Dashboard

The dashboard is designed to work across different desktop screen sizes.

The interface handles:

- KPI card sizing
- Chart responsiveness
- Navigation
- Text overflow
- Filter layouts
- Responsive columns
- Dashboard spacing

Special attention is given to important KPI values so that large numbers remain readable.

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming and analytics |
| Pandas | Data cleaning and transformation |
| Plotly | Interactive visualization |
| Streamlit | Dashboard application |
| Excel | Supporting assets |
| Git | Version control |
| GitHub | Source code and portfolio hosting |

---

# 🧠 Analytical Methodology

The project follows a complete Data Analyst methodology:

### 1. Business Understanding

Identify the business problem and analytical requirements.

### 2. Data Understanding

Inspect all available datasets and understand their structure.

### 3. Data Profiling

Analyze:

- Rows
- Columns
- Data types
- Missing values
- Duplicates
- Unique values
- Keys
- Relationships

### 4. Data Cleaning

Handle:

- Missing values
- Duplicate records
- Invalid values
- Data types
- Dates
- Categorical inconsistencies

### 5. Data Modeling

Create meaningful relationships between customers, orders, products, inventory, delivery, marketing and feedback datasets.

### 6. Data Transformation

Prepare analytical datasets and derived metrics using Python and Pandas.

### 7. Exploratory Data Analysis

Identify:

- Trends
- Patterns
- Outliers
- Category performance
- Product performance
- Customer behavior
- Operational performance

### 8. KPI Development

Create business-focused KPIs.

### 9. Visualization

Convert analytical findings into interactive Plotly charts.

### 10. Dashboard Development

Build the final interactive Streamlit application.

### 11. Business Insights

Convert findings into actionable recommendations.

---

# 🔄 Application Workflow

User Opens Dashboard
        ↓
Data Loading
        ↓
Data Cleaning
        ↓
Data Transformation
        ↓
Analytical Data Model
        ↓
KPI Calculation
        ↓
User Applies Filters
        ↓
Metrics Recalculate
        ↓
Charts Update
        ↓
User Explores Performance
        ↓
Business Insights
        ↓
Data-Driven Decisions

---

# 💼 Business Value

The dashboard can help business stakeholders:

- Monitor revenue performance
- Identify high-performing products
- Understand customer behavior
- Improve inventory planning
- Detect delivery problems
- Evaluate marketing effectiveness
- Monitor customer satisfaction
- Compare locations
- Identify operational bottlenecks
- Prioritize business opportunities
- Make data-driven decisions

---

# 🧪 Validation & Accuracy

Before finalizing analytical outputs, important metrics are validated against the underlying datasets.

Validation includes:

- Order counts
- Revenue totals
- Item quantities
- Average Order Value
- Customer counts
- Rating calculations
- Delivery metrics
- Inventory calculations

Special attention is given to joins between Orders, Order Items, Products, Customers, Delivery and Feedback datasets to prevent incorrect aggregations.

---

# 🔐 Data Integrity Principles

The project follows these principles:

- Raw datasets are preserved.
- No fabricated data is used.
- No fabricated KPIs are used.
- No fabricated business insights are used.
- Dataset relationships are validated.
- Revenue duplication is avoided.
- Unsupported metrics are not calculated.
- Analytical calculations are reproducible.
- Original data is not unnecessarily modified.

---

# 🚀 Future Improvements

Future versions could include:

- Real-time data integration
- Automated scheduled data refresh
- Cloud deployment
- Database integration
- Advanced customer segmentation
- Sales forecasting
- Demand forecasting
- Inventory forecasting
- Product recommendation system
- Advanced NLP for customer feedback
- Automated email reports
- Role-based dashboard access
- Production database integration
- Automated ETL pipelines
- Cloud database integration

---

# 🎥 Project Demo

## Video Demonstration

Add the project walkthrough video here:

[▶️ Watch Project Demo](YOUR_VIDEO_LINK)

---

# 📸 Dashboard Preview

The project includes multiple interactive analytical pages:

- Executive Overview
- Sales Analytics
- Customer Analytics
- Product Analytics
- Delivery Analytics
- Inventory Analytics
- Marketing Analytics
- Feedback Analytics
- Business Insights

Add dashboard screenshots or a GIF here to demonstrate the application.

---

# 📊 Business Questions Answered

The dashboard is designed to answer questions such as:

1. What is the total revenue?
2. How many orders were placed?
3. What is the average order value?
4. How many items were sold?
5. Which category generates the most revenue?
6. Which products sell the most?
7. Which products generate the highest revenue?
8. Which products are underperforming?
9. Which customers generate the highest revenue?
10. Which locations perform best?
11. What is the average delivery time?
12. What percentage of deliveries are delayed?
13. Which locations have delivery problems?
14. Which products have inventory risks?
15. Which marketing campaigns perform best?
16. Which channels generate stronger returns?
17. What is the average customer rating?
18. Which products receive poor ratings?
19. What are the most important business trends?
20. What actions should the business take?

---

# 🧑‍💻 Skills Demonstrated

## Python

- Pandas
- Data transformation
- Data validation
- Analytical calculations
- Modular programming

## Data Analytics

- Data Cleaning
- Data Profiling
- Exploratory Data Analysis
- KPI Development
- Trend Analysis
- Customer Analysis
- Product Analysis
- Operational Analysis
- Business Intelligence

## Data Visualization

- Plotly
- Interactive charts
- KPI visualization
- Trend analysis
- Category analysis
- Performance analysis

## Streamlit

- Multi-page application
- Interactive filters
- Custom CSS
- Dashboard components
- Responsive layouts
- Data downloads

## Git & GitHub

- Git version control
- Repository management
- Documentation
- Portfolio project management

---

# 📚 Key Learnings

Through this project, I gained practical experience in:

- Working with multiple datasets
- Data cleaning
- Data validation
- Data modeling
- Dataset relationships
- Exploratory Data Analysis
- KPI development
- Business metrics
- Interactive visualization
- Streamlit application development
- Business insight generation
- Data-driven recommendations
- Git and GitHub workflow

---

# ⚙️ Installation

## Clone Repository

    git clone https://github.com/YOUR_USERNAME/blinkit-ecommerce-analytics-dashboard.git

## Navigate to Project

    cd blinkit-ecommerce-analytics-dashboard

## Create Virtual Environment

### Windows

    python -m venv .venv

### Activate Environment

    .venv\Scripts\activate

### macOS / Linux

    python3 -m venv .venv

    source .venv/bin/activate

---

# 📦 Install Dependencies

    pip install -r requirements.txt

---

# ▶️ Run the Dashboard

    streamlit run app.py

The application will open in the browser.

Default local address:

    http://localhost:8501

---

# 📂 Project Structure

    📦 blinkit-ecommerce-analytics-dashboard
    │
    ├── 📄 app.py
    ├── 📄 README.md
    ├── 📄 requirements.txt
    ├── 📄 .gitignore
    ├── 📄 utils.py
    │
    ├── 📁 pages
    │   ├── Executive Overview
    │   ├── Sales Analytics
    │   ├── Customer Analytics
    │   ├── Product Analytics
    │   ├── Delivery Analytics
    │   ├── Inventory Analytics
    │   ├── Marketing Analytics
    │   ├── Feedback Analytics
    │   └── Business Insights
    │
    ├── 📁 src
    │   ├── analytics.py
    │   ├── data_loader.py
    │   ├── data_model.py
    │   ├── styles.py
    │   └── ui_components.py
    │
    ├── 📁 assets
    │
    └── 📁 data

---

# 💼 Data Analyst Interview Explanation

## 60-Second Project Explanation

"I developed an end-to-end e-commerce Business Intelligence dashboard using Python, Pandas, Plotly and Streamlit. The project combines multiple datasets covering customers, orders, order items, products, inventory, delivery, marketing and customer feedback. I started by profiling and cleaning the data, validating relationships between datasets and creating an analytical data model. I then performed exploratory analysis and developed business KPIs such as revenue, orders, average order value, product performance, delivery metrics and customer ratings. Finally, I built an interactive Streamlit dashboard with filters and visualizations and converted the analysis into actionable business insights and recommendations."

---

# 🗣️ Detailed Interview Workflow

### How did you start the project?

I started by understanding the business problem and identifying the available datasets and analytical requirements.

### How did you understand the data?

I performed data profiling to understand the columns, data types, missing values, duplicates, unique values and relationships between datasets.

### How did you clean the data?

I handled missing values, duplicate records, incorrect data types, date conversion, inconsistent categorical values and invalid records wherever required.

### How did you combine the datasets?

I identified and validated primary and foreign key relationships and created an analytical data model while ensuring joins did not duplicate revenue or transaction values.

### What analysis did you perform?

I analyzed sales, customers, products, delivery operations, inventory, marketing performance and customer feedback.

### Which technologies did you use?

I used Python and Pandas for data processing, Plotly for interactive visualization and Streamlit for building the dashboard.

### What was the final outcome?

The final application provides a centralized view of business performance and helps identify trends, operational issues, customer behavior and business opportunities.

---

# 📌 Project Summary

| Category | Details |
|---|---|
| Project Type | End-to-End Data Analytics / Business Intelligence |
| Domain | E-Commerce / Quick Commerce / Grocery |
| Programming | Python |
| Data Processing | Pandas |
| Visualization | Plotly |
| Dashboard | Streamlit |
| Version Control | Git |
| Repository | GitHub |

---

# 🌟 Project Highlights

- End-to-End Data Analyst Project
- Multi-Source E-Commerce Analytics
- Python-Based Data Processing
- Pandas Data Analysis
- Interactive Plotly Visualizations
- Streamlit Dashboard
- Sales Analytics
- Customer Analytics
- Product Analytics
- Delivery Analytics
- Inventory Analytics
- Marketing Analytics
- Customer Feedback Analytics
- Business Insights
- Interactive Filters
- KPI-Based Reporting
- Custom CSS
- Responsive UI
- GitHub Portfolio Ready

---

# 👨‍💻 Author

## Malkit Choudhary

**Data Analyst | Python | SQL | Excel | Power BI | Data Visualization**

This project was developed as part of my Data Analytics portfolio to demonstrate practical skills in data cleaning, analysis, visualization, dashboard development and Business Intelligence.

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐ Star.

---

# 📄 License

This project is created for educational and portfolio purposes.

The datasets used in this project are intended for analytics practice and demonstration.

---

# 🚀 Final Project Goal

The goal of this project is to demonstrate how raw business data can be transformed into actionable business intelligence.

RAW DATA
    ↓
DATA CLEANING
    ↓
DATA MODELING
    ↓
DATA ANALYSIS
    ↓
KPIs
    ↓
VISUALIZATION
    ↓
INTERACTIVE DASHBOARD
    ↓
BUSINESS INSIGHTS
    ↓
BUSINESS RECOMMENDATIONS
    ↓
DATA-DRIVEN DECISIONS

### Turning Data into Decisions. 📊
