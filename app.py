import streamlit as st 
import os

st.title('Secrets Example')

secrets = st.secrets

more_stuff = st.secrets['more_stuff']

print('st.secrets will store everything entered in secrets.toml in a dictionary')
print(f'{secrets} + "\n')

api_key = os.getenv('API_KEY')
print(f'API_KEY is an environment variable: {api_key}')
