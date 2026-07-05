import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.title("🚌 All-in-One Bus Tracker")

# Function to save individual bus data safely
def save_data(bus_name, date, income, expense):
    profit = income - expense
    new_row = pd.DataFrame([{
        "Date": date,
        "Bus Name": bus_name,
        "Income": income,
        "Expense": expense,
        "Profit": profit
    }])
    
    file_name = "bus_all_records.csv"
    if os.path.exists(file_name):
        df = pd.read_csv(file_name)
        df = pd.concat([df, new_row], ignore_index=True)
    else:
        df = new_row
    df.to_csv(file_name, index=False)
    st.success(f"✅ {bus_name} ka data successfully save ho gaya!")

# 1. CREATE 4 SEPARATE TABS FOR 4 BUSES
tab1, tab2, tab3, tab4, tab_report = st.tabs(["🚍 Bus 1", "🚍 Bus 2", "🚍 Bus 3", "🚍 Bus 4", "📊 Overall Report"])

# --- BUS 1 PORTAL ---
with tab1:
    st.subheader("Bus 1 Data Entry")
    date1 = st.date_input("Select Date", datetime.now(), key="d1")
    inc1 = st.number_input("Income (₹)", min_value=0.0, step=100.0, key="i1")
    exp1 = st.number_input("Expense (₹)", min_value=0.0, step=100.0, key="e1")
    if st.button("Add Bus 1 Data", key="b1"):
        save_data("Bus 1", date1, inc1, exp1)

# --- BUS 2 PORTAL ---
with tab2:
    st.subheader("Bus 2 Data Entry")
    date2 = st.date_input("Select Date", datetime.now(), key="d2")
    inc2 = st.number_input("Income (₹)", min_value=0.0, step=100.0, key="i2")
    exp2 = st.number_input("Expense (₹)", min_value=0.0, step=100.0, key="e2")
    if st.button("Add Bus 2 Data", key="b2"):
        save_data("Bus 2", date2, inc2, exp2)

# --- BUS 3 PORTAL ---
with tab3:
    st.subheader("Bus 3 Data Entry")
    date3 = st.date_input("Select Date", datetime.now(), key="d3")
    inc3 = st.number_input("Income (₹)", min_value=0.0, step=100.0, key="i3")
    exp3 = st.number_input("Expense (₹)", min_value=0.0, step=100.0, key="e3")
    if st.button("Add Bus 3 Data", key="b3"):
        save_data("Bus 3", date3, inc3, exp3)

# --- BUS 4 PORTAL ---
with tab4:
    st.subheader("Bus 4 Data Entry")
    date4 = st.date_input("Select Date", datetime.now(), key="d4")
    inc4 = st.number_input("Income (₹)", min_value=0.0, step=100.0, key="i4")
    exp4 = st.number_input("Expense (₹)", min_value=0.0, step=100.0, key="e4")
    if st.button("Add Bus 4 Data", key="b4"):
        save_data("Bus 4", date4, inc4, exp4)

# --- OVERALL AUTOMATIC REPORT ---
with tab_report:
    st.subheader("📈 Total Summary & History")
    file_name = "bus_all_records.csv"
    
    if os.path.exists(file_name):
        df_records = pd.read_csv(file_name)
        
        # Live calculations
        t_inc = df_records["Income"].sum()
        t_exp = df_records["Expense"].sum()
        t_prof = df_records["Profit"].sum()
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Income (All Buses)", f"₹{t_inc}")
        col2.metric("Total Expense (All Buses)", f"₹{t_exp}")
        col3.metric("Total Net Profit", f"₹{t_prof}", delta=f"₹{t_prof}")
        
        st.markdown("### 📋 Pura History Record:")
        st.dataframe(df_records, use_container_width=True)
    else:
        st.info("Abhi tak koi data add nahi kiya gaya hai.")
      
