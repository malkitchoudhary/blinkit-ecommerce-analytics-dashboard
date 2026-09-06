"""Reusable UI components for Blinkit BI Dashboard."""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from utils import format_value
from src.styles import COLORS, get_page_color

def kpi_card(label, value, caption, color_class="yellow", col=None):
    """
    Create a professional KPI card.
    
    Args:
        label: Card label (e.g., "TOTAL SALES")
        value: Value to display (e.g., "₹11,009,308")
        caption: Short explanation (e.g., "Order revenue in view")
        color_class: CSS class name for left border color ("yellow", "green", "blue", etc.)
        col: Streamlit column to place card in (optional)
    """
    html_content = f'''
    <div class="metric-card {color_class}">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-caption">{caption}</div>
    </div>
    '''
    
    if col:
        col.markdown(html_content, unsafe_allow_html=True)
    else:
        st.markdown(html_content, unsafe_allow_html=True)

def kpi_row(metrics, colors=None):
    """
    Create a row of KPI cards.
    
    Args:
        metrics: List of tuples (label, value, caption)
        colors: List of color class names ("yellow", "green", "blue", etc.)
    """
    if colors is None:
        colors = ["yellow", "green", "blue", "purple"]
    
    cols = st.columns(len(metrics))
    for col, (label, value, caption), color in zip(cols, metrics, colors):
        kpi_card(label, value, caption, color, col)

def chart_header(title, subtitle=""):
    """Display a chart section header."""
    st.markdown(
        f'<div class="chart-heading">{title}</div>' +
        (f'<div class="chart-subtitle">{subtitle}</div>' if subtitle else ''),
        unsafe_allow_html=True
    )

def section_label(title):
    """Display a section label."""
    st.markdown(f'<div class="section-label">{title}</div>', unsafe_allow_html=True)

def apply_chart_theme(fig, height=340, page_name="Executive Overview"):
    """Apply consistent Plotly chart theme."""
    page_color = get_page_color(page_name)
    
    fig.update_layout(
        height=height,
        margin=dict(l=10, r=10, t=42, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="DM Sans, sans-serif", color=COLORS["dark_ink"]),
        legend=dict(orientation="h", y=1.08, x=0),
        hovermode="x unified"
    )
    
    fig.update_xaxes(
        showgrid=False,
        linecolor=COLORS["light_border"],
        linewidth=1
    )
    
    fig.update_yaxes(
        gridcolor=COLORS["light_border"],
        zeroline=False,
        linecolor=COLORS["light_border"],
        linewidth=1
    )
    
    return fig

def render_metric_cards(metrics_dict):
    """
    Render metric cards with automatic color assignment.
    
    Args:
        metrics_dict: Dict of {label: value_tuple}
                      where value_tuple = (formatted_value, caption)
    """
    color_sequence = ["yellow", "green", "blue", "purple", "orange", "red", "teal", "cyan"]
    
    cols = st.columns(len(metrics_dict))
    for idx, (col, (label, (value, caption))) in enumerate(zip(cols, metrics_dict.items())):
        color = color_sequence[idx % len(color_sequence)]
        kpi_card(label, value, caption, color, col)

def donut_chart(frame, names, values, colors, center_text, height=285):
    """Create a professional donut chart."""
    fig = px.pie(frame, names=names, values=values, hole=0.70, color_discrete_sequence=colors)
    
    fig.update_traces(
        textposition="outside",
        textinfo="percent",
        textfont_size=10,
        marker=dict(line=dict(color=COLORS["white"], width=2)),
        hovertemplate="<b>%{label}</b><br>%{value:,.0f}<br>%{percent}<extra></extra>"
    )
    
    fig.update_layout(
        annotations=[dict(
            text=center_text,
            x=0.5,
            y=0.5,
            font=dict(size=14, family="Nunito Sans", color=COLORS["dark_ink"]),
            showarrow=False
        )],
        showlegend=False
    )
    
    return apply_chart_theme(fig, height)

def two_column_layout(left_title, left_subtitle, left_fig, right_title, right_subtitle, right_fig):
    """Create a two-column chart layout."""
    left, right = st.columns([1.42, 1])
    
    with left:
        chart_header(left_title, left_subtitle)
        st.plotly_chart(left_fig, width="stretch", config={"displayModeBar": False})
    
    with right:
        chart_header(right_title, right_subtitle)
        st.plotly_chart(right_fig, width="stretch", config={"displayModeBar": False})

def three_column_layout(charts_data):
    """
    Create a three-column chart layout.
    
    Args:
        charts_data: List of 3 tuples (title, subtitle, fig)
    """
    cols = st.columns([1.04, 1.14, 1.1])
    
    for col, (title, subtitle, fig) in zip(cols, charts_data):
        with col:
            chart_header(title, subtitle)
            st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})

def insight_box(title, observation, recommendation, highlight=False):
    """Display an insight/recommendation box."""
    css_class = "insight-card highlight" if highlight else "insight-card"
    st.markdown(
        f'''<div class="{css_class}">
            <strong>{title}</strong>
            <p>{observation}</p>
            <p style="color: var(--muted); font-size: 11px; margin-top: 8px;">
                <strong>Recommendation:</strong> {recommendation}
            </p>
        </div>''',
        unsafe_allow_html=True
    )

def application_header(values):
    """Render the premium application header."""
    st.markdown(
        f'''<div class="topbar">
            <div class="topbar-logo">blink<span>it</span></div>
            <div class="topbar-copy">
                <small>Executive command centre</small>
                <strong>Blinkit Grocery Performance</strong>
                <p>Sales, customer and last-mile operations — one decision-ready view.</p>
            </div>
            <div class="topbar-meta">
                <div class="orders-pill">
                    <b>●</b> {values.get("Orders", 0):,} orders in current view
                </div>
                <div class="updated">
                    ▣ <b>Live dashboard</b>Filters applied
                </div>
            </div>
        </div>''',
        unsafe_allow_html=True
    )

def empty_state(message="No records match the current filters."):
    """Display empty state message."""
    st.info(message)
