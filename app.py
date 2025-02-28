import streamlit as st
from pint import UnitRegistry


st.markdown("""
<style>

.stSidebar {
    background-color: #2980b9;
    color: #50352c;
}
.title {
    font-size: 48px;
    font-weight: bold;
    background: linear-gradient(45deg, #ff0066, #ffcc00, #33cc33,rgb(27, 14, 209), #9933ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 20px;    
    }
.author {
    font-size: 20px;
    font-weight: bold;
    background: linear-gradient(45deg, #ff0066, #ffcc00, #33cc33,rgb(27, 14, 209), #9933ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 20px;    
    }
.success {
    background-color: white;
    font-size: 1rem;
    font-weight: bold;
    text-align: center;
    color: green !important;
    margin-bottom: 20px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# multicolored title
st.markdown('<h1 class="title">Unit Converter ( USING PINT)</h1>', unsafe_allow_html=True)

# Initialize the unit registry for conversions
ureg = UnitRegistry()

# Coversion categories and corresponding units
conversion_categories = {
    "Length": ["meter", "kilometer", "mile", "foot", "inch"],
    "Mass": ["gram", "kilogram", "pound", "ounce"],
    "Temperature": ["degC", "degF", "kelvin"],
    "Volume": ["liter", "milliliter", "gallon", "cubic_meter"]
}

# Sidebar 
st.sidebar.markdown("<h1 style='text-align:center; font-size:20px; font-weight:bold; color:white;'>Unit Conversion Options</h1>",unsafe_allow_html=True)

# Select conversion category
category = st.sidebar.selectbox("Select Conversion Category", list(conversion_categories.keys()))

# Retrieve the relevant units for the selected category
units = conversion_categories[category]

# Input fields 
value = st.sidebar.number_input("Enter Value", value=1.0, format="%.4f")
from_unit = st.sidebar.selectbox("From Unit", units, key="from_unit")
to_unit = st.sidebar.selectbox("To Unit", units, key="to_unit")

# Conversion button
if st.sidebar.button("Convert"):
    try:
        quantity = ureg.Quantity(value, from_unit)
        converted = quantity.to(to_unit)
        st.sidebar.markdown("<h2 class='success'>Conversion successful</h2>",unsafe_allow_html=True)
        st.sidebar.write(f"**<div style='text-align:center;color:white; font-size:16px;'>{value} {from_unit} equals {converted.magnitude:.4f} {to_unit}</div>**",unsafe_allow_html=True)        
        st.write("<h3 style='text-align: center; color: white;background: linear-gradient(45deg, #ff0066, #ffcc00, #33cc33,rgb(27, 14, 209), #9933ff); border-radius: 20px;'>Conversion Result</h3>", unsafe_allow_html=True)
        st.write(f"**<div style='text-align:center;color:green; font-size:20px; font-weight:bold;'>{value} {from_unit} equals {converted.magnitude:.4f} {to_unit}</div>**",unsafe_allow_html=True)
    except Exception as e:
        st.sidebar.error(f"Conversion Error: {e}")
        
st.markdown("<br><br><br><br>", unsafe_allow_html=True)

# Footer
st.markdown("---")

st.markdown("""
        Designed with ❤️ by <h1 class="author">Amjad Afzal Ahmed</h1>
        \nUnit converter created using [pint](https://pint.readthedocs.io/en/stable/) library to handle unit conversions accurately.

""", unsafe_allow_html=True)
