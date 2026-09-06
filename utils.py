import streamlit as st


def format_value(label, value):
    if label in {"Revenue", "AOV"}:
        return f"₹{value:,.0f}"
    if label in {"On-time", "Repeat rate"}:
        return f"{value:.1%}"
    if label == "Rating":
        return f"{value:.2f} / 5"
    return f"{value:,.0f}"


def chart_layout(fig, height=340):
    fig.update_layout(height=height, margin=dict(l=10, r=10, t=42, b=10), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(family="DM Sans, sans-serif", color="#1f241f"), legend=dict(orientation="h", y=1.08, x=0))
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(gridcolor="#eee3b7", zeroline=False)
    return fig


def empty_state(message="No records match the current filters."):
    st.info(message)
