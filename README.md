# Project-Machine

## 配置
1.[安装BBDOWN插件](https://github.com/nilaoda/BBDown "bilibili视频命令行下载器")（感谢这个小众又高效的插件），或者解压仓库中BBDown压缩包，里面是同样的内容

2.最外层目录中的BBDown.exe路径复制至cmd_1文件中第21行 ```command = r'BBDown\BBDown.exe --audio-only '+url```

3.解压仓库中ffmpeg压缩包（如果你没有ffmpeg的话），将bin目录下的ffmpeg路径添加至环境变量，例如 ```E:\ffmpeg-N-103197-gbff7d662d7-win64-gpl\ffmpeg-N-103197-gbff7d662d7-win64-gpl\bin```

4.如果出现openai的连接问题，你需要检查你的科学上网方式，或者你需要申请一个openai的[apikey](https://openai.com/),log in进入OpenAI platform，点击右上角你的头像,VIEW Apikeys

5.streamlit，fastapi，uvicorn相关库文件与openai库文件可以通过pip下载

6.如果你的网络连接不稳定可能或导致过长的文本以及视频无法转录或者总结

配置过程通常boring and annoying。但是感谢你的配合与提出问题。Merci，Thankyou，谢谢 :smile:
## Project
### Get inspired

- https://www.tensorflow.org/js/demos
- https://streamlit.io/gallery
- https://shiny.rstudio.com/gallery/
- https://github.com/MarcSkovMadsen/awesome-streamlit
- Alternatives to streamlit:
    - https://anvil.works/articles/4-alternatives-streamlit
- https://huggingface.co/

### Implementation

Your machine learning web application can be based on streamlit, flask, next.js, tensorflow.js or any other framework. It should be deployed on the cloud (Tencent/Alibaba/Google/Microsoft Cloud).

You can use chatgpt or gpt4, if you have the API key.

You can use AI APIs from Baidu/Tencent/Alibaba/Amazon/Google etc., for example:
- https://cloud.tencent.com/product/ai-class

Apply for a domain name if necessary, e.g. [http://an-interesting-ml-app.com](http://an-interesting-ml-app.com).

As an alternative, a WeChat miniprogram is OK as well.

Use emojis or fontawesome/bootstrap icons where appropriate (How can we deliver messages without emojis! Impossible mission!).

You code should be open-sourced and hosted on GitHub.

### What's expected of your video
- Length of video \>= 20 min
- You video should include those contents:
    - General presentation
    - Where do you get inspirations from for coming up with the idea of your project
    - How to use your ML Web app
    - How did you implement your app
    - How did you deploy your app
    - How CI/CD/GitHub Actions/WebHook plays a role in your deployment
- If possible, make it fun (Because life is good). 
- If possible, make it fancy (Because you are young). 
- If applicable, include an ethics analysis of your project in the video.
- If applicable, include an social impact analysis of your project  in the video.
- If applicable, include an market analysis of your project  in the video.
- If applicable, include an ecology analysis of your project  in the video.
- And yes, your video should be presented in English. 

### Submission of your work

1. Create a folder, in which you put:
    - the video
    - the source code
    - a txt/markdown file indicating 
        - what's the task of each team member
        - the estimated workload/contribution percentage of each team member 
    - a txt/markdown file indicating 
        - the URL of your GitHub repository for hosting your code
        - prof will check the commit history of your GitHub repo to see how each team member is contributing  
1. Zip the folder
1. Upload the zip file to Google Drive
1. Send the sharing link to the prof, by PRIVATE WeChat or by Email
    - Therefore, in the WeChat/Email message, there are no attached files, just an Google Drive URL.

For each team, just one submission of the work is necessary, by one member of your team.

Deadline for submission:
- The second Friday of the 14 days of Exam Weeks of SHU, 23:59.

### For best projects
- Best projects might be hosted on [http://lunde.top](http://lunde.top), to inspire future projects.
- Best projects' videos will be included on Lunde Chen's bilibili channel.
- Lunde Chen might invite you to participate in innovation competitions with your projects.

