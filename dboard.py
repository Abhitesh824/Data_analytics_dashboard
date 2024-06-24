from data import Data
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title = "Jobs_data", layout = "wide")
st.title("Welcome!")

data = Data()

data_sources = ['linkedin', 'glassdoor', 'zip_recruiter', 'indeed']
linkedin_jobs = data.df.groupby('site')[data.df[data.df['site'] == 'linkedin']].count()
glassdoor_jobs = data.df['site'].isin(['glassdoor']).count()
zip_recruiter_jobs = data.df['site'].isin(['zip_recruiter']).count()
indeed_jobs = data.df['site'].isin(['indeed']).count()

st.write("Data sources and amount")
col1, col2, col3 = st.columns([0.3, 0.3, 0.4])
col4, col5, col6 = st.columns([0.3, 0.3, 0.4])

# printing the df
with col1:
    st.metric(label="Linkedin", value=linkedin_jobs, delta=None)

with col2:
    st.metric(label="Glassdoor", value=glassdoor_jobs, delta=None)

with col4:
    st.metric(label="Zip_recruiter", value=zip_recruiter_jobs, delta=None)

with col5:
    st.metric(label="Indeed", value=indeed_jobs, delta=None)



with col3, col6:
    graph = px.pie(data.df[0:], names='site', 
                   color_discrete_sequence=px.colors.qualitative.G10, hole=0.5)
    st.plotly_chart(graph, use_container_width=True)


with col4:
    site_choice = st.multiselect(label = "Sites", options=['linkedin', 'glassdoor', 'zip_recruiter', 'indeed'])
    if site_choice:
        new_df = data.df[data.df['site'].isin(site_choice)]
    else:
        new_df = pd.DataFrame(columns=['company', 'max_amount'])




