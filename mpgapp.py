
import streamlit as st
import pandas as pd

st.set_page_config(page_title="MPG Explorer", layout="wide")
st.title("MPG Explorer")
uploaded_file = st.file_uploader("Upload mpg.csv", type=["csv"])
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.dataframe(df.head(5))
  st.metric("Vehicles", len(df))
  numeric_col = st.selectbox("Filter measurement", options=["mpg", "horsepower", "weight", "acceleration"])
  filter_enabled = st.checkbox("Enable minimum filter", value=False)
  filtered = df.copy()
  if filter_enabled:
    min_val = float(df[numeric_col].min())
    max_val = float(df[numeric_col].max())
    threshold = st.slider("Minimum value", min_value=min_val, max_value=max_val, value=min_val)
    filtered = filtered[filtered[numeric_col] >= threshold]
  st.dataframe(filtered)
  st.metric("Filtered vehicles", filtered.shape[0])
  mpg_series = filtered["mpg"].reset_index(drop=True)
  st.line_chart(mpg_series)
  st.download_button("Download filtered CSV", filtered.to_csv(index=False), file_name="mpg_filtered.csv", mime="text/csv")
