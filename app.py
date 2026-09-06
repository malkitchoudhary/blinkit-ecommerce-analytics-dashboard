"""Blinkit-inspired portfolio analytics dashboard with live filtered data."""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from src.analytics import apply_filters, category_sales, kpis, product_sales
from src.data_loader import build_order_view, load_data, build_item_view
from src.styles import apply_base_theme, COLORS
from src.ui_components import (
    kpi_card, chart_header, section_label, apply_chart_theme,
    donut_chart, application_header, empty_state, insight_box,
    two_column_layout, three_column_layout
)
from utils import format_value

st.set_page_config(page_title="Blinkit | Business Intelligence", page_icon="🟡", layout="wide", initial_sidebar_state="expanded")

@st.cache_data(show_spinner=False)
def csv_bytes(frame):
    return frame.to_csv(index=False).encode("utf-8")

def sidebar(data):
    """Render sidebar with Blinkit branding and filters."""
    st.sidebar.markdown('<div class="brand"><div class="wordmark">blink<span>it</span></div><div class="tagline">India\'s last-minute<br>retail intelligence</div></div>', unsafe_allow_html=True)
    st.sidebar.markdown('<div class="filter-title">Filter panel</div>', unsafe_allow_html=True)
    
    orders = data["orders"]
    dates = st.sidebar.date_input(
        "Order date",
        value=(orders.order_date.min().date(), orders.order_date.max().date())
    )
    
    area = st.sidebar.selectbox(
        "Outlet location",
        ["All"] + sorted(data["customers"].area.dropna().unique().tolist())
    )
    
    segment = st.sidebar.selectbox(
        "Outlet type",
        ["All"] + sorted(data["customers"].customer_segment.dropna().unique().tolist())
    )
    
    category = st.sidebar.selectbox(
        "Item type",
        ["All"] + sorted(data["products"].category.dropna().unique().tolist())
    )
    
    product = st.sidebar.selectbox(
        "Product",
        ["All"] + sorted(data["products"].product_name.dropna().unique().tolist())
    )
    
    status = st.sidebar.selectbox(
        "Delivery status",
        ["All"] + sorted(orders.delivery_status.dropna().unique().tolist())
    )
    
    rating = st.sidebar.selectbox(
        "Minimum rating",
        ["All", "1 ★", "2 ★", "3 ★", "4 ★", "5 ★"]
    )
    
    if st.sidebar.button("Reset all filters", width="stretch"):
        st.rerun()
    
    st.sidebar.markdown("---")
    st.sidebar.caption("Interactive portfolio dashboard • Live values refresh with every filter selection.")
    
    return {
        "dates": dates if isinstance(dates, tuple) and len(dates) == 2 else None,
        "area": area,
        "category": category,
        "product": product,
        "delivery_status": status,
        "rating": rating,
        "customer_segment": segment
    }

def apply_dashboard_filters(data, filters):
    """Apply filters and maintain data integrity across tables."""
    filtered = apply_filters(data, filters)
    order_ids = set(filtered["orders"].order_id)
    
    if filters["customer_segment"] != "All":
        ids = set(data["customers"].loc[data["customers"].customer_segment == filters["customer_segment"], "customer_id"])
        order_ids &= set(filtered["orders"].loc[filtered["orders"].customer_id.isin(ids), "order_id"])
    
    if filters["product"] != "All":
        product_ids = set(data["products"].loc[data["products"].product_name == filters["product"], "product_id"])
        order_ids &= set(data["items"].loc[data["items"].product_id.isin(product_ids), "order_id"])
    
    if filters["rating"] != "All":
        minimum_rating = float(filters["rating"].split()[0])
        order_ids &= set(data["feedback"].loc[data["feedback"].rating >= minimum_rating, "order_id"])
    
    filtered = dict(filtered)
    for key in ("orders", "items", "delivery", "feedback"):
        filtered[key] = filtered[key][filtered[key].order_id.isin(order_ids)]
    
    return filtered

def executive_overview(data, values):
    """Render the premium Executive Overview dashboard."""
    st.markdown(
        f'''<div class="dashboard-header">
            <div>
                <div class="eyebrow">Executive command centre</div>
                <h1>Blinkit Grocery Performance</h1>
                <p>Sales, customer and last-mile operations — one decision-ready view.</p>
            </div>
            <div class="data-badge"><b>{values["Orders"]:,}</b> orders in current view</div>
        </div>''',
        unsafe_allow_html=True
    )
    
    # KPI Cards with proper color coding - fixed wrapping issue
    cols = st.columns(4)
    
    with cols[0]:
        kpi_card(
            "TOTAL SALES",
            format_value("Revenue", values["Revenue"]),
            "Order revenue in view",
            "yellow"
        )
    
    with cols[1]:
        kpi_card(
            "AVERAGE SALES",
            format_value("AOV", values["AOV"]),
            "Average order value",
            "green"
        )
    
    with cols[2]:
        kpi_card(
            "NO. OF ITEMS",
            f'{values["Items sold"]:,}',
            "Items sold across orders",
            "blue"
        )
    
    with cols[3]:
        kpi_card(
            "AVG RATING",
            format_value("Rating", values["Rating"]),
            "Customer feedback score",
            "purple"
        )
    
    # Sales & outlet performance section
    section_label("Sales & outlet performance")
    
    order_view = build_order_view(data)
    monthly = data["orders"].assign(
        period=lambda f: f.order_date.dt.to_period("M").astype(str)
    ).groupby("period", as_index=False).agg(revenue=("order_total", "sum"))
    
    categories = category_sales(data).head(9)
    delivery = data["delivery"].delivery_status.value_counts().rename_axis("status").reset_index(name="orders")
    areas = order_view.groupby("area", as_index=False).agg(revenue=("order_total", "sum")).sort_values("revenue", ascending=False).head(5)
    segments = order_view.groupby("customer_segment", as_index=False).agg(
        revenue=("order_total", "sum"),
        orders=("order_id", "nunique")
    ).sort_values("revenue", ascending=False)
    
    # Left column: Outlet establishment trend
    left, right = st.columns([1.42, 1])
    
    with left:
        chart_header("Outlet establishment trend", "Revenue movement by month")
        fig = px.area(
            monthly,
            x="period",
            y="revenue",
            color_discrete_sequence=[COLORS["primary_yellow"]]
        )
        fig.update_traces(
            line=dict(color="#c79700", width=2.5),
            fillcolor="rgba(247,208,70,.48)",
            hovertemplate="<b>%{x}</b><br>Sales: ₹%{y:,.0f}<extra></extra>"
        )
        st.plotly_chart(
            apply_chart_theme(fig, 290),
            width="stretch",
            config={"displayModeBar": False}
        )
    
    with right:
        chart_header("Service reliability", "Delivery-status distribution")
        center_text = f'<b>{values["On-time"]:.0%}</b><br><span style="font-size:9px">ON TIME</span>'
        fig = donut_chart(
            delivery,
            "status",
            "orders",
            [COLORS["primary_green"], COLORS["primary_yellow"], "#d85a42"],
            center_text
        )
        st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})
    
    # Three-column layout: Categories, Category mix, and Top areas
    st.markdown("", unsafe_allow_html=True)  # Spacing
    
    chart_cols = st.columns([1.04, 1.14, 1.1])
    
    with chart_cols[0]:
        chart_header("Item type", "Revenue contribution by category")
        fig = px.bar(
            categories.sort_values("revenue"),
            x="revenue",
            y="category",
            orientation="h",
            color_discrete_sequence=["#d3a920"]
        )
        fig.update_traces(hovertemplate="<b>%{y}</b><br>Revenue: ₹%{x:,.0f}<extra></extra>")
        st.plotly_chart(
            apply_chart_theme(fig, 350),
            width="stretch",
            config={"displayModeBar": False}
        )
    
    with chart_cols[1]:
        chart_header("Category mix", "Where product revenue comes from")
        fig = donut_chart(
            categories,
            "category",
            "revenue",
            ["#0c831f", "#f7d046", "#668e45", "#e8ae28", "#a3c44c", "#435f39", "#df7f38"],
            '<b>Revenue</b><br><span style="font-size:9px">CATEGORY MIX</span>',
            350
        )
        st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})
    
    with chart_cols[2]:
        chart_header("Outlet location", "Top delivery areas by revenue")
        fig = px.bar(
            areas.sort_values("revenue"),
            x="revenue",
            y="area",
            orientation="h",
            color_discrete_sequence=[COLORS["primary_green"]]
        )
        fig.update_traces(hovertemplate="<b>%{y}</b><br>Revenue: ₹%{x:,.0f}<extra></extra>")
        st.plotly_chart(
            apply_chart_theme(fig, 350),
            width="stretch",
            config={"displayModeBar": False}
        )
    
    # Segment analysis
    st.markdown("", unsafe_allow_html=True)  # Spacing
    
    seg_left, seg_right = st.columns([1.25, 1])
    
    with seg_left:
        chart_header("Outlet type", "Revenue and order volume by customer segment")
        fig = go.Figure()
        fig.add_bar(
            name="Total sales",
            x=segments["customer_segment"],
            y=segments["revenue"],
            marker_color=COLORS["primary_green"],
            hovertemplate="<b>%{x}</b><br>Revenue: ₹%{y:,.0f}<extra></extra>"
        )
        fig.add_scatter(
            name="Orders",
            x=segments["customer_segment"],
            y=segments["orders"],
            mode="markers+lines",
            yaxis="y2",
            marker=dict(color=COLORS["primary_yellow"], size=9),
            line=dict(color="#d3a920", width=2),
            hovertemplate="<b>%{x}</b><br>Orders: %{y:,.0f}<extra></extra>"
        )
        fig.update_layout(yaxis2=dict(overlaying="y", side="right", showgrid=False, title="Orders"), barmode="group")
        st.plotly_chart(
            apply_chart_theme(fig, 310),
            width="stretch",
            config={"displayModeBar": False}
        )
    
    with seg_right:
        chart_header("Top products", "Highest item-value products")
        top_products = product_sales(data).head(6).sort_values("revenue")
        fig = px.bar(
            top_products,
            x="revenue",
            y="product_name",
            orientation="h",
            color_discrete_sequence=[COLORS["primary_yellow"]]
        )
        fig.update_traces(hovertemplate="<b>%{y}</b><br>Item value: ₹%{x:,.0f}<extra></extra>")
        st.plotly_chart(
            apply_chart_theme(fig, 310),
            width="stretch",
            config={"displayModeBar": False}
        )
    legacy_duplicate_code = '''
    left, middle, right = st.columns([1.04, 1.14, 1.1])
    with left:
        figure_card("Item type", "Revenue contribution by category")
        fig = px.bar(categories.sort_values("revenue"), x="revenue", y="category", orientation="h", color_discrete_sequence=["#d3a920"]); fig.update_traces(hovertemplate="<b>%{y}</b><br>Revenue: ₹%{x:,.0f}<extra></extra>")
        st.plotly_chart(chart_layout(fig, 350), width="stretch", config={"displayModeBar": False})
    with middle:
        figure_card("Category mix", "Where product revenue comes from")
        st.plotly_chart(donut(categories, "category", "revenue", ["#0c831f", "#f7d046", "#668e45", "#e8ae28", "#a3c44c", "#435f39", "#df7f38"], '<b>Revenue</b><br><span style="font-size:9px">CATEGORY MIX</span>', 350), width="stretch", config={"displayModeBar": False})
    with right:
        figure_card("Outlet location", "Top delivery areas by revenue")
        fig = px.bar(areas.sort_values("revenue"), x="revenue", y="area", orientation="h", color_discrete_sequence=["#0c831f"]); fig.update_traces(hovertemplate="<b>%{y}</b><br>Revenue: ₹%{x:,.0f}<extra></extra>")
        st.plotly_chart(chart_layout(fig, 350), width="stretch", config={"displayModeBar": False})
    left, right = st.columns([1.25, 1])
    with left:
        figure_card("Outlet type", "Revenue and order volume by customer segment")
        fig = go.Figure(); fig.add_bar(name="Total sales", x=segments["customer_segment"], y=segments["revenue"], marker_color="#0c831f", hovertemplate="<b>%{x}</b><br>Revenue: ₹%{y:,.0f}<extra></extra>"); fig.add_scatter(name="Orders", x=segments["customer_segment"], y=segments["orders"], mode="markers+lines", yaxis="y2", marker=dict(color="#f7d046", size=9), line=dict(color="#d3a920", width=2), hovertemplate="<b>%{x}</b><br>Orders: %{y:,.0f}<extra></extra>"); fig.update_layout(yaxis2=dict(overlaying="y", side="right", showgrid=False, title="Orders"), barmode="group")
        st.plotly_chart(chart_layout(fig, 310), width="stretch", config={"displayModeBar": False})
    with right:
        figure_card("Top products", "Highest item-value products")
        top = product_sales(data).head(6).sort_values("revenue"); fig = px.bar(top, x="revenue", y="product_name", orientation="h", color_discrete_sequence=["#f7d046"]); fig.update_traces(hovertemplate="<b>%{y}</b><br>Item value: ₹%{x:,.0f}<extra></extra>")
        st.plotly_chart(chart_layout(fig, 310), width="stretch", config={"displayModeBar": False})
    '''

def standard_page(data, page):
    """Render analytical pages with consistent styling and improved layout."""
    st.markdown(f'<div class="eyebrow">Blinkit business intelligence</div><h1>{page}</h1>', unsafe_allow_html=True)
    
    metric_data = kpis(data)
    metric_items = list(metric_data.items())[:4]
    
    cols = st.columns(4)
    for col, (label, value) in zip(cols, metric_items):
        col.metric(label, format_value(label, value))
    
    st.markdown("---", unsafe_allow_html=True)
    
    if page == "Sales Analytics":
        daily = data["orders"].assign(date=lambda frame: frame.order_date.dt.date).groupby("date", as_index=False).order_total.sum()
        left, right = st.columns(2)
        
        with left:
            chart_header("Daily order revenue", "Revenue trend over time")
            fig = px.line(
                daily,
                x="date",
                y="order_total",
                markers=True,
                color_discrete_sequence=[COLORS["sales_blue"]]
            )
            st.plotly_chart(
                apply_chart_theme(fig),
                width="stretch"
            )
        
        with right:
            chart_header("Quantity sold by category", "Item volume distribution")
            fig = px.bar(
                category_sales(data),
                x="category",
                y="quantity",
                color_discrete_sequence=[COLORS["sales_blue"]]
            )
            st.plotly_chart(
                apply_chart_theme(fig),
                width="stretch"
            )
        
        st.markdown("---", unsafe_allow_html=True)
        st.markdown("### Product Performance Details")
        items = build_item_view(data)
        st.dataframe(
            items.groupby(["product_id", "product_name", "category"], as_index=False).agg(
                quantity=("quantity", "sum"),
                item_value=("item_value", "sum")
            ).sort_values("item_value", ascending=False),
            width="stretch",
            hide_index=True
        )
    
    elif page == "Customer Analytics":
        view = data["customers"].merge(
            data["orders"].groupby("customer_id", as_index=False).agg(
                actual_orders=("order_id", "nunique"),
                revenue=("order_total", "sum")
            ),
            on="customer_id",
            how="left"
        )
        
        chart_header("Revenue by customer segment", "")
        fig = px.bar(
            view.groupby("customer_segment", as_index=False).revenue.sum(),
            x="customer_segment",
            y="revenue",
            color_discrete_sequence=[COLORS["customer_purple"]]
        )
        st.plotly_chart(
            apply_chart_theme(fig),
            width="stretch"
        )
        
        st.markdown("---", unsafe_allow_html=True)
        st.markdown("### Top 25 Customers by Revenue")
        st.dataframe(
            view.sort_values("revenue", ascending=False).head(25),
            width="stretch",
            hide_index=True
        )
    
    elif page == "Product Analytics":
        view = product_sales(data)
        
        chart_header("Revenue vs Quantity by Product", "Size represents quantity sold")
        fig = px.scatter(
            view,
            x="revenue",
            y="quantity",
            size="quantity",
            color="category",
            hover_name="product_name"
        )
        st.plotly_chart(
            apply_chart_theme(fig),
            width="stretch"
        )
        
        st.markdown("---", unsafe_allow_html=True)
        st.markdown("### Complete Product Catalog")
        st.dataframe(view, width="stretch", hide_index=True)
    
    elif page == "Delivery Analytics":
        view = data["delivery"]
        left, right = st.columns(2)
        
        with left:
            chart_header("Promised-to-actual variance", "Time difference in minutes")
            fig = px.histogram(
                view,
                x="computed_delivery_minutes",
                color="delivery_status"
            )
            st.plotly_chart(apply_chart_theme(fig), width="stretch")
        
        with right:
            chart_header("Delivery status mix", "Distribution of delivery outcomes")
            fig = px.bar(
                view.delivery_status.value_counts().rename_axis("status").reset_index(name="orders"),
                x="status",
                y="orders",
                color_discrete_sequence=[COLORS["delivery_red"]]
            )
            st.plotly_chart(apply_chart_theme(fig), width="stretch")
        
        st.markdown("---", unsafe_allow_html=True)
        st.markdown("### Delivery Performance Metrics")
        st.dataframe(
            view.groupby("delivery_status", as_index=False).agg(
                orders=("order_id", "nunique"),
                avg_variance=("computed_delivery_minutes", "mean"),
                max_variance=("computed_delivery_minutes", "max")
            ),
            width="stretch",
            hide_index=True
        )
    
    elif page == "Inventory Analytics":
        view = data["inventory"].copy()
        view["available_units"] = view.stock_received - view.damaged_stock
        
        st.caption("Available units represent received stock less damaged stock; the source does not provide a validated inventory-value or turnover measure.")
        
        trend = view.groupby("date", as_index=False).available_units.sum()
        
        chart_header("Available inventory movement", "Inventory level trend")
        fig = px.line(
            trend,
            x="date",
            y="available_units",
            color_discrete_sequence=[COLORS["inventory_teal"]]
        )
        st.plotly_chart(apply_chart_theme(fig), width="stretch")
        
        st.markdown("---", unsafe_allow_html=True)
        st.markdown("### Inventory Details by Product")
        st.dataframe(
            view.groupby("product_id", as_index=False).agg(
                received=("stock_received", "sum"),
                damaged=("damaged_stock", "sum"),
                available=("available_units", "sum")
            ).sort_values("available"),
            width="stretch",
            hide_index=True
        )
    
    elif page == "Marketing Analytics":
        view = data["marketing"].groupby(["campaign_name", "channel"], as_index=False).agg(
            spend=("spend", "sum"),
            revenue=("revenue_generated", "sum"),
            conversions=("conversions", "sum"),
            roas=("roas", "mean")
        )
        
        chart_header("Marketing spend vs generated revenue", "Bubble size represents conversions")
        fig = px.scatter(
            view,
            x="spend",
            y="revenue",
            size="conversions",
            color="channel",
            hover_name="campaign_name"
        )
        st.plotly_chart(apply_chart_theme(fig), width="stretch")
        
        st.markdown("---", unsafe_allow_html=True)
        st.markdown("### Marketing Campaign Performance")
        st.dataframe(
            view.sort_values("roas", ascending=False),
            width="stretch",
            hide_index=True
        )
    
    elif page == "Feedback Analytics":
        view = data["feedback"]
        left, right = st.columns(2)
        
        with left:
            chart_header("Rating distribution", "Customer ratings")
            fig = px.histogram(
                view,
                x="rating",
                color="sentiment",
                nbins=5
            )
            st.plotly_chart(apply_chart_theme(fig), width="stretch")
        
        with right:
            chart_header("Feedback themes", "Category breakdown")
            fig = px.bar(
                view.feedback_category.value_counts().rename_axis("category").reset_index(name="feedback"),
                x="category",
                y="feedback",
                color_discrete_sequence=[COLORS["feedback_cyan"]]
            )
            st.plotly_chart(apply_chart_theme(fig), width="stretch")
        
        st.markdown("---", unsafe_allow_html=True)
        st.markdown("### Detailed Feedback Records")
        st.dataframe(
            view[["rating", "sentiment", "feedback_category", "feedback_text", "feedback_date"]].sort_values("rating").head(50),
            width="stretch",
            hide_index=True
        )
    
    else:  # Business Insights
        categories, products, delivery, feedback = category_sales(data), product_sales(data), data["delivery"], data["feedback"]
        insights = [
            (
                "Category leader",
                f"{categories.iloc[0].category} leads item value at {format_value('Revenue', categories.iloc[0].revenue)}.",
                "Prioritize availability and promotion planning for this category."
            ),
            (
                "Product demand concentration",
                f"{products.iloc[0].product_name} is the highest item-value product at {format_value('Revenue', products.iloc[0].revenue)}.",
                "Use this demand signal in replenishment and cross-sell planning."
            ),
            (
                "Delivery variance",
                f"{delivery.is_late.mean():.1%} of records are later than promised.",
                "Review capacity and traffic patterns around late deliveries."
            ),
            (
                "Customer voice",
                f"Average feedback rating is {feedback.rating.mean():.2f}/5 across {len(feedback):,} records.",
                "Pair low-rated feedback categories with operational owners."
            ),
        ]
        
        st.markdown("### Strategic Insights")
        for title, observation, recommendation in insights:
            insight_box(title, observation, recommendation, highlight=(title == "Category leader"))


def render(page="Executive Overview"):
    """Main application orchestrator."""
    # A Streamlit page is executed independently, so inject the shared theme
    # here rather than only while this module is imported by the home page.
    apply_base_theme()
    data = load_data()
    filtered = apply_dashboard_filters(data, sidebar(data))
    
    if filtered["orders"].empty:
        st.warning("No records match the current filter selection. Please reset or widen a filter.")
        return
    
    values = kpis(filtered)
    
    application_header(values)
    
    if page == "Executive Overview":
        executive_overview(filtered, values)
    else:
        standard_page(filtered, page)
    
    st.markdown("---", unsafe_allow_html=True)
    section_label("Filtered data explorer")
    
    explorer = build_order_view(filtered).head(500)
    st.dataframe(explorer, width="stretch", hide_index=True)
    st.download_button(
        "Download filtered orders",
        csv_bytes(explorer),
        "blinkit_filtered_orders.csv",
        "text/csv"
    )
    
    st.markdown('<div class="portfolio-note">Made by <b>Malkit Choudhary</b></div>', unsafe_allow_html=True)

if __name__ == "__main__":
    render()
