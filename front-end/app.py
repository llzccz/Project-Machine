import streamlit as st
import requests
#streamlit run .\front-end\app.py
st.markdown("""# Welcome
## We can generate mind maps based on: long text, bilibili video link
""")
long_text = st.text_area('long text to summarize', placeholder="long text")

if st.button('Generate text'):
    url =  'http://127.0.0.1:8000/sum/'
    response = requests.post(url, json={'request': long_text})

    
    if response.status_code == 200:
        data_received = response.json()
        result = data_received['result']
        # 在界面上显示处理后的文本
        #st.write("You entered: ", long_text)
        st.write("处理后的文本:")
                
        st.write(result)
    else:
        st.write("链接超时，请求处理失败,您可以刷新重试")


video_link = st.text_input('your video link', placeholder="bilibili video link")
if st.button('Generate link'):
    url =  'https://localhost/8000/sum/'
    response = requests.post(url, json={'text': video_link})
    st.write("You entered: ", video_link)



