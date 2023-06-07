import streamlit as st
import requests
# import cmd_1
#streamlit run .\front-end\app.py
st.markdown("""# Welcome !  :face_with_cowboy_hat:
## We can generate outline based on: long text, bilibili video link :dizzy:
""")

long_text = st.text_area('long text to summarize', placeholder="long text")

if st.button('Generate text'):
    url =  'http://127.0.0.1:8000/sum/'
    response = requests.post(url, json={'request': long_text})
    if response.status_code == 200:
        data_received = response.json()
        result = data_received['result']
        # 在界面上显示处理后的文本
        st.write("The processed text:")
        st.write(result)
    else:
        st.write("链接超时，请求处理失败,您可以刷新重试")


video_link = st.text_input('your video link(maybe less than 5 min)', placeholder="bilibili video link")
if st.button('Generate link'):
    url =  'http://127.0.0.1:8000/sum_vedio/'
    st.write("You entered: ", video_link)
    # file_name=cmd_1.download_getname(video_link)
    # st.write(file_name)
    response = requests.post(url, json={'request': video_link})

    data_received = response.json()
    result = data_received['result']
   # 在界面上显示处理后的文本
    st.write("The processed text:")
    st.write(result)
    
    # if response.status_code == 200:
    #     data_received = response.json()
    #     result = data_received['result']
    #     # 在界面上显示处理后的文本
    #     st.write("处理后的文本:")
    #     st.write(result)
    # else:
    #     st.write("链接超时，请求处理失败,您可以刷新重试")




