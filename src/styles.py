"""Centralized styling system for Blinkit BI Dashboard."""

import streamlit as st

# Color Palette
COLORS = {
    "primary_yellow": "#f7d046",
    "brand_yellow": "#ffd842",
    "primary_green": "#0c831f",
    "dark_ink": "#20231f",
    "muted_text": "#6f756b",
    "light_border": "#e8e3d0",
    "light_bg": "#fffdf5",
    "cream_bg": "#fffbe8",
    "white": "#ffffff",
    
    # Page accent colors
    "exec_green": "#0c831f",
    "sales_blue": "#1687db",
    "customer_purple": "#7a35c5",
    "product_orange": "#d28100",
    "delivery_red": "#d0392b",
    "inventory_teal": "#0b8b72",
    "marketing_violet": "#7245c9",
    "feedback_cyan": "#0094a8",
    "insights_coral": "#d94b37",
}

# Page color scheme mapping
PAGE_COLORS = {
    "Executive Overview": {
        "accent": COLORS["exec_green"],
        "light_bg": "#dff6e4",
        "border": "#94d9a2",
        "icon": "⌂",
    },
    "Sales Analytics": {
        "accent": COLORS["sales_blue"],
        "light_bg": "#dff0ff",
        "border": "#9dccf2",
        "icon": "▥",
    },
    "Customer Analytics": {
        "accent": COLORS["customer_purple"],
        "light_bg": "#f0e6ff",
        "border": "#caa7f0",
        "icon": "♟",
    },
    "Product Analytics": {
        "accent": COLORS["product_orange"],
        "light_bg": "#fff0d7",
        "border": "#f1c772",
        "icon": "◆",
    },
    "Delivery Analytics": {
        "accent": COLORS["delivery_red"],
        "light_bg": "#ffe4e1",
        "border": "#efaba2",
        "icon": "▣",
    },
    "Inventory Analytics": {
        "accent": COLORS["inventory_teal"],
        "light_bg": "#dcf6f0",
        "border": "#93dac9",
        "icon": "●",
    },
    "Marketing Analytics": {
        "accent": COLORS["marketing_violet"],
        "light_bg": "#eee8ff",
        "border": "#c4b0f0",
        "icon": "◖",
    },
    "Feedback Analytics": {
        "accent": COLORS["feedback_cyan"],
        "light_bg": "#dcf8fb",
        "border": "#8fdde5",
        "icon": "●",
    },
    "Business Insights": {
        "accent": COLORS["insights_coral"],
        "light_bg": "#ffe5dc",
        "border": "#f1afa0",
        "icon": "✦",
    },
}

def get_page_color(page_name):
    """Get the color scheme for a specific page."""
    return PAGE_COLORS.get(page_name, PAGE_COLORS["Executive Overview"])

def apply_base_theme():
    """Apply the base Blinkit theme to the entire application."""
    st.markdown(f"""<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Nunito+Sans:wght@700;800;900&display=swap');

:root {{
    --yellow: {COLORS['primary_yellow']};
    --green: {COLORS['primary_green']};
    --ink: {COLORS['dark_ink']};
    --muted: {COLORS['muted_text']};
    --line: {COLORS['light_border']};
}}

html, body, [class*="css"] {{
    font-family: 'DM Sans', sans-serif;
    color: var(--ink);
}}

.stApp {{
    background: radial-gradient(circle at 78% 4%, #fff2a6 0, #fff8d9 21%, #fffdf5 48%, #fff 100%);
}}

[data-testid="stHeader"] {{
    background: transparent;
}}

[data-testid="stSidebar"] {{
    background: var(--yellow);
    border-right: 1px solid #d9b120;
}}

[data-testid="stSidebar"] [data-testid="stSidebarContent"] {{
    padding: 0 14px 12px;
    position: relative;
}}

/* Fixed brand treatment for the otherwise unused navigation header space. */
[data-testid="stSidebar"] [data-testid="stSidebarContent"]:before {{
    content: "b";
    position: absolute;
    z-index: 20;
    top: 24px;
    left: 25px;
    display: grid;
    place-items: center;
    width: 48px;
    height: 48px;
    border-radius: 16px;
    background: #ffffff;
    color: #0c831f;
    font: 900 32px/1 'Nunito Sans', sans-serif;
    box-shadow: 0 7px 18px rgba(76, 60, 8, 0.20);
    pointer-events: none;
}}

[data-testid="stSidebar"] [data-testid="stSidebarContent"]:after {{
    content: "blinkit";
    position: absolute;
    z-index: 20;
    top: 36px;
    left: 84px;
    color: #1c251b;
    font: 900 25px/1.05 'Nunito Sans', sans-serif;
    letter-spacing: -1.4px;
    pointer-events: none;
}}

[data-testid="stSidebar"] * {{
    color: var(--ink) !important;
}}

.brand {{
    display: block;
    position: absolute;
    z-index: 20;
    top: -620px;
    left: 84px;
    pointer-events: none;
}}

.wordmark {{
    font: 900 34px/1 'Nunito Sans', sans-serif;
    letter-spacing: -2.4px;
    color: #171a16;
}}

.brand .wordmark {{
    display: none;
}}

.wordmark span {{
    color: var(--green) !important;
}}

.tagline {{
    margin-top: 7px;
    font-size: 10px;
    font-weight: 800;
    line-height: 1.4;
    letter-spacing: 0.25px;
    text-transform: uppercase;
}}

.filter-title {{
    margin: 6px 0 8px;
    color: #4f4b2d;
    font-size: 11px;
    font-weight: 900;
    letter-spacing: 1.35px;
    text-transform: uppercase;
}}

[data-testid="stSidebar"] label {{
    font-size: 11px !important;
    font-weight: 800 !important;
}}

[data-testid="stSidebar"] [data-baseweb="select"] > div,
[data-testid="stSidebar"] [data-baseweb="input"] > div {{
    background: #fffbe8 !important;
    border: 1px solid #d6ad21 !important;
    border-radius: 6px !important;
    box-shadow: none !important;
}}

[data-testid="stSidebar"] [data-testid="stDateInput"] input {{
    background: #fffbe8 !important;
}}

[data-testid="stSidebarNav"] {{
    margin-top: 105px !important;
    padding: 0 !important;
}}

[data-testid="stSidebarNav"] ul {{
    gap: 5px !important;
    padding: 0 !important;
}}

[data-testid="stSidebarNav"] li {{
    margin: 0 !important;
}}

[data-testid="stSidebarNav"] a {{
    background: #fff8d7 !important;
    border: 1px solid #d6ad21 !important;
    border-radius: 8px !important;
    margin: 0 !important;
    padding: 8px 10px !important;
    transition: all 0.18s ease;
}}

[data-testid="stSidebarNav"] a:hover {{
    background: #fff !important;
    border-color: #0c831f !important;
    transform: translateX(2px);
}}

[data-testid="stSidebarNav"] a[aria-current="page"] {{
    background: #0c831f !important;
    border-color: #0c831f !important;
    box-shadow: 0 3px 8px #0c831f35 !important;
}}

[data-testid="stSidebarNav"] a[aria-current="page"] * {{
    color: #fff !important;
}}

[data-testid="stSidebarNav"] span {{
    font-size: 12px !important;
    font-weight: 800 !important;
}}

.stButton > button,
[data-testid="stDownloadButton"] > button {{
    background: var(--green) !important;
    color: #fff !important;
    border: 0 !important;
    border-radius: 7px !important;
    font-weight: 800 !important;
    box-shadow: 0 4px 10px #0c831f30 !important;
}}

.stButton > button:hover,
[data-testid="stDownloadButton"] > button:hover {{
    background: #086d1a !important;
    color: #fff !important;
}}

.main .block-container {{
    max-width: 1480px;
    padding-top: 2.1rem;
    padding-bottom: 0.25rem;
}}

.topbar {{
    display: flex;
    align-items: center;
    gap: 26px;
    margin: -2.1rem -1rem 22px;
    padding: 17px 28px;
    background: linear-gradient(100deg, #ffd844, #f7cf43 70%, #f8d45a);
    border-bottom: 1px solid #d9b120;
    box-shadow: 0 4px 16px #9c7a1622;
}}

.topbar-logo {{
    min-width: 139px;
    padding-right: 25px;
    border-right: 2px solid #604d1680;
    font: 900 35px/1 'Nunito Sans', sans-serif;
    letter-spacing: -2.5px;
}}

.topbar-logo span {{
    color: #0c831f;
}}

.topbar-copy {{
    flex: 1;
}}

.topbar-copy small {{
    display: block;
    font-size: 10px;
    font-weight: 900;
    letter-spacing: 1.6px;
    text-transform: uppercase;
}}

.topbar-copy strong {{
    display: block;
    margin: 2px 0;
    font: 900 26px/1.08 'Nunito Sans', sans-serif;
    letter-spacing: -1px;
}}

.topbar-copy p {{
    margin: 4px 0 0;
    color: #646041;
    font-size: 12px;
}}

.topbar-meta {{
    display: flex;
    align-items: center;
    gap: 13px;
}}

.orders-pill {{
    background: #fff;
    border-radius: 99px;
    padding: 9px 13px;
    font-size: 11px;
    font-weight: 800;
    box-shadow: 0 2px 8px #7a631d1c;
}}

.orders-pill b {{
    color: #0c831f;
}}

.updated {{
    padding-left: 13px;
    border-left: 1px solid #806a1e;
    font-size: 10px;
    line-height: 1.35;
}}

.updated b {{
    display: block;
    font-size: 12px;
}}

.dashboard-header {{
    display: flex;
    align-items: end;
    justify-content: space-between;
    margin: 0 0 17px;
}}

.eyebrow {{
    color: var(--green);
    font-size: 11px;
    font-weight: 900;
    letter-spacing: 1.55px;
    text-transform: uppercase;
}}

.dashboard-header h1 {{
    margin: 2px 0 3px;
    font: 900 30px/1.1 'Nunito Sans', sans-serif;
    letter-spacing: -1.2px;
}}

.dashboard-header p {{
    margin: 0;
    color: var(--muted);
    font-size: 13px;
}}

.data-badge {{
    align-self: center;
    background: #fff;
    border: 1px solid var(--line);
    border-radius: 99px;
    padding: 8px 12px;
    color: var(--muted);
    font-size: 11px;
    font-weight: 700;
}}

.data-badge b {{
    color: var(--green);
}}

.metric-card {{
    min-height: 104px;
    box-sizing: border-box;
    padding: 17px 18px 14px;
    background: #fff;
    border: 1px solid var(--line);
    border-radius: 13px;
    box-shadow: 0 5px 18px rgba(46, 47, 30, 0.07);
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}}

.metric-card:after {{
    content: '';
    position: absolute;
    inset: 0 auto 0 0;
    width: 5px;
    background: var(--yellow);
}}

.metric-card.green:after {{
    background: var(--green);
}}

.metric-card.blue:after {{
    background: #1687db;
}}

.metric-card.purple:after {{
    background: #7a35c5;
}}

.metric-card.orange:after {{
    background: #d28100;
}}

.metric-label {{
    color: var(--muted);
    font-size: 10px;
    font-weight: 900;
    letter-spacing: 0.9px;
    text-transform: uppercase;
}}

.metric-value {{
    margin: 7px 0 4px;
    font: 900 28px 'Nunito Sans', sans-serif;
    letter-spacing: -0.7px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}}

.metric-value.large {{
    font-size: 32px;
}}

.metric-value.medium {{
    font-size: 26px;
}}

.metric-value.small {{
    font-size: 22px;
}}

.metric-caption {{
    color: var(--green);
    font-size: 10px;
    font-weight: 700;
    margin-top: auto;
}}

.section-label {{
    margin: 24px 0 14px;
    font: 900 16px 'Nunito Sans', sans-serif;
    letter-spacing: -0.25px;
    color: var(--ink);
}}

.chart-heading {{
    margin: 5px 0 -2px 4px;
    font: 900 14px 'Nunito Sans', sans-serif;
    letter-spacing: -0.25px;
    color: var(--ink);
}}

.chart-subtitle {{
    margin: 0 0 4px 4px;
    color: var(--muted);
    font-size: 10px;
}}

.stPlotlyChart {{
    background: #fff;
    border: 1px solid var(--line);
    border-radius: 13px;
    padding: 4px 7px 0;
    box-shadow: 0 5px 18px rgba(46, 47, 30, 0.06);
}}

[data-testid="stDataFrame"] {{
    border: 1px solid var(--line);
    border-radius: 12px;
    overflow: hidden;
}}

.portfolio-note {{
    margin-top: 14px;
    padding: 10px 0 0;
    border-top: 1px solid var(--line);
    color: var(--muted);
    text-align: center;
    font-size: 12px;
}}

.portfolio-note b {{
    color: var(--green);
}}

.insight-card {{
    border-left: 4px solid var(--green);
    padding: 14px 16px;
    background: #f9fdf7;
    border-radius: 8px;
    box-shadow: 0 2px 6px rgba(46, 47, 30, 0.05);
    margin-bottom: 12px;
}}

.insight-card.highlight {{
    background: #fff7e6;
    border-left-color: var(--yellow);
}}

.insight-card strong {{
    color: var(--ink);
    display: block;
    margin-bottom: 4px;
    font-weight: 700;
}}

.insight-card p {{
    margin: 6px 0 0;
    font-size: 12px;
    line-height: 1.5;
}}

/* Navigation page color scheme */
[data-testid="stSidebarNav"] a[href*="Executive_Overview"] {{
    background: #dff6e4 !important;
    border-color: #94d9a2 !important;
}}

[data-testid="stSidebarNav"] a[href*="Executive_Overview"]:before {{
    content: '⌂';
    color: #098333;
}}

[data-testid="stSidebarNav"] a[href*="Sales_Analytics"] {{
    background: #dff0ff !important;
    border-color: #9dccf2 !important;
}}

[data-testid="stSidebarNav"] a[href*="Sales_Analytics"]:before {{
    content: '▥';
    color: #1687db;
}}

[data-testid="stSidebarNav"] a[href*="Customer_Analytics"] {{
    background: #f0e6ff !important;
    border-color: #caa7f0 !important;
}}

[data-testid="stSidebarNav"] a[href*="Customer_Analytics"]:before {{
    content: '♟';
    color: #7a35c5;
}}

[data-testid="stSidebarNav"] a[href*="Product_Analytics"] {{
    background: #fff0d7 !important;
    border-color: #f1c772 !important;
}}

[data-testid="stSidebarNav"] a[href*="Product_Analytics"]:before {{
    content: '◆';
    color: #d28100;
}}

[data-testid="stSidebarNav"] a[href*="Delivery_Analytics"] {{
    background: #ffe4e1 !important;
    border-color: #efaba2 !important;
}}

[data-testid="stSidebarNav"] a[href*="Delivery_Analytics"]:before {{
    content: '▣';
    color: #d0392b;
}}

[data-testid="stSidebarNav"] a[href*="Inventory_Analytics"] {{
    background: #dcf6f0 !important;
    border-color: #93dac9 !important;
}}

[data-testid="stSidebarNav"] a[href*="Inventory_Analytics"]:before {{
    content: '●';
    color: #0b8b72;
}}

[data-testid="stSidebarNav"] a[href*="Marketing_Analytics"] {{
    background: #eee8ff !important;
    border-color: #c4b0f0 !important;
}}

[data-testid="stSidebarNav"] a[href*="Marketing_Analytics"]:before {{
    content: '◖';
    color: #7245c9;
}}

[data-testid="stSidebarNav"] a[href*="Feedback_Analytics"] {{
    background: #dcf8fb !important;
    border-color: #8fdde5 !important;
}}

[data-testid="stSidebarNav"] a[href*="Feedback_Analytics"]:before {{
    content: '●';
    color: #0094a8;
}}

[data-testid="stSidebarNav"] a[href*="Business_Insights"] {{
    background: #ffe5dc !important;
    border-color: #f1afa0 !important;
}}

[data-testid="stSidebarNav"] a[href*="Business_Insights"]:before {{
    content: '✦';
    color: #d94b37;
}}

[data-testid="stSidebarNav"] a:before {{
    display: inline-block;
    width: 19px;
    font-size: 15px;
    margin-right: 6px;
}}

/* Responsive Design */
@media(max-width: 860px) {{
    .topbar {{
        margin: -1rem -0.5rem 16px;
        padding: 14px 16px;
        gap: 12px;
    }}
    
    .topbar-logo {{
        min-width: auto;
        padding: 0;
        border: 0;
        font-size: 28px;
    }}
    
    .topbar-copy strong {{
        font-size: 20px;
    }}
    
    .topbar-copy p,
    .updated {{
        display: none;
    }}
    
    .topbar-meta {{
        margin-left: auto;
    }}
    
    .orders-pill {{
        padding: 7px 9px;
    }}
    
    .metric-value {{
        font-size: 22px;
    }}
    
    .data-badge {{
        display: none;
    }}
}}

@media(max-width: 640px) {{
    .topbar {{
        flex-direction: column;
        align-items: flex-start;
        gap: 8px;
    }}
    
    .topbar-meta {{
        margin-left: 0;
        width: 100%;
        justify-content: space-between;
    }}
    
    .metric-card {{
        min-height: 90px;
        padding: 12px 14px;
    }}
    
    .metric-value {{
        font-size: 20px;
        margin: 4px 0 2px;
    }}
}}
</style>""", unsafe_allow_html=True)
