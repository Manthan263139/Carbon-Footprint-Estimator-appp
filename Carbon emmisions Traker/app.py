import streamlit as st

EMISSION_FACTORS = {
    "India": {
        "Transportation": 0.14,  # kgCO2/km
        "Electricity": 0.82,     # kgCO2/kWh
        "Diet": 1.23,            # kgCO2/mcal
        "Waste": 0.1             # kgCO2/kg
    }
}

st.set_page_config(layout="wide", page_title="Personal Carbon Calculator")
st.title("Carbon Footprint Estimator App")



# User input
st.subheader("🌎 Your Country")
country = st.selectbox("Select", ["India"])

col1, col2 = st.columns(2)

with col1:
    st.subheader(" 🚗 Daily commute distance (in km)")
    distance = st.slider("Distance", 0.0, 100.0, key="distance_input")

    st.subheader(" 💡 Monthly Electricity consumption (in kwh) ")
    electricity = st.slider("Electricity", 0.0, 1000.0, key="electricity_input")


with col2:
    st.subheader(" 🗑 Waste generated per week (in kg)")
    waste = st.slider("Waste", 0.0, 100.0, key="waste_input")

    st.subheader(" 🍲 No of meals per day  ")
    meals = st.number_input("Meals",0, key="meals_input")




# Normalized the input
if distance > 0:
    distance = distance * 365

if electricity > 0:
    electricity = electricity * 12

if meals > 0:
    meals = meals * 365

if waste > 0:
    waste = waste * 52





# Calculating the Carbon Emmisions 
transporation_emissions=EMISSION_FACTORS[country]['Transportation']*distance 
electricity_emissions=EMISSION_FACTORS[country]['Electricity']*electricity 
diet_emissions=EMISSION_FACTORS[country]['Diet']*meals
waste_emissions=EMISSION_FACTORS[country]['Waste']*waste 


transporation_emissions=round(transporation_emissions/1000,2)
electricity_emissions=round(electricity_emissions/1000,2)
diet_emissions=round(diet_emissions/1000,2)
waste_emissions=round(waste_emissions/1000,2)



# convert emissions to tonnes and round off 2 decimal places
total_emissions=round(
    transporation_emissions+electricity_emissions+diet_emissions+waste_emissions,2
)


if st.button("Calculate CO2 Emissions"):

    st.header("Results")
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Carbon Emissions by Categories")
        st.info(f" 🚗 Transportation: {transporation_emissions} tonnes CO2 per year")
        st.info(f" 💡 Electricity: {electricity_emissions} tonnes CO2 per year")
        st.info(f" 🍲 Diet: {diet_emissions} tonnes CO2 per year")
        st.info(f" 🗑 Waste: {waste_emissions} tonnes CO2 per year")

    with col4:
        st.subheader("Total Carbon Footprint")
        st.info(f"Your Total Carbon footprint is: {total_emissions} tonnes CO2 per year")
        st.warning("""
        India's per capita CO2 emissions are currently around 1.9 tonnes per year, which is significantly lower than the global average of 4.8 tonnes per year
1
. However, with increasing industrialization and urbanization, India's carbon emissions are projected to grow in the coming years. This highlights the need for individuals and communities to take action to reduce their carbon footprint.
        """)









