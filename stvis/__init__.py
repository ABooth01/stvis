import streamlit.components.v1 as components
import streamlit as st
import random

num = random.randint(0,99999)

if 'key' not in st.session_state:
    st.session_state['key'] = num

num1 = st.session_state['key']

def pv_static(fig,name=num1+'graph'):
    h1=fig.height
    h1=int(h1.replace('px',''))
    w1=fig.width
    w1=int(w1.replace('px',''))
    fig.write_html(name+'.html')
    components.html(
     fig.html,height=h1+30, width=w1+30
          )
    return
