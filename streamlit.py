import streamlit as st 
import pandas as pd 
import time

st.title('Title')

st.header('Header')

st.subheader('Sub Header')

st.caption('Caption')

sample_code = '''
this is code
'''

st.code(sample_code, language='python')

st.text('오늘은 2024년 1월입니다.')
st.text('올해 이틀 일함.')


#################################
dataframe = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})


st.title('데이터프레임 튜토리얼')
st.dataframe(dataframe, use_container_width=False)

st.table(dataframe)

with st.sidebar:
    with st.echo():
        st.write('This code will be printed to the sidebar.')

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")
