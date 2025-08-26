import streamlit as st
import pandas as pd


st.set_page_config(page_title="Demo App", page_icon="📊", layout="wide")


st.title("📊 Streamlit Demo")
st.caption("Hello, world — minimal example")


@st.cache_data(ttl="10m")
def load_data():
    return pd.DataFrame({"x": range(10), "y": [v**2 for v in range(10)]})


# Stateless transform; result is cached per unique args
@st.cache_data(ttl="10m")
def filter_data(df: pd.DataFrame, threshold: int):
    return df[df["y"] >= threshold]


df = load_data()
th = st.slider("y threshold", 0, 81, 16)
filtered = filter_data(df, th)


st.line_chart(filtered, x="x", y="y")
st.dataframe(filtered, use_container_width=True)
