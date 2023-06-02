import streamlit as st

st.markdown("""# Welcome
## We can generate mind maps based on: long text, bilibili video link
""")

video_link = st.text_input('your video link', placeholder="bilibili video link")
long_text = st.text_area('long text to summarize', placeholder="long text")


if st.button('Generate'):
    if long_text:
        st.write("You entered: ", long_text)
    else:
        st.write("You entered: ", video_link)
