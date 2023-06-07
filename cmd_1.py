import re
import subprocess

def extract_file_type(output):
    # 使用正则表达式匹配文件类型
    pattern = r'\[([^\]]+)\]'
    match = re.search(pattern, output)
    
    # 提取文件类型
    if match:
        file_type = match.group(1).lower()
        if file_type == 'm4a':
            file_type = '.m4a'
        else:
            file_type = '.' + file_type
        return file_type
    
    return None

def download_audio(url:str):
    command = r'BBDown\BBDown.exe --audio-only '+url
    subprocess.call(command, shell=True)
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout.strip()

    # 提取视频标题
    title_index = output.find('视频标题: ')
    if title_index != -1:
        title_end_index = output.find('\n', title_index)
        if title_end_index != -1:
            video_title = output[title_index + len('视频标题: '):title_end_index]

    # 提取文件类型
    file_type_index = output.find('[音频] ')
    if file_type_index != -1:
        file_type_end_index = output.find('\n', file_type_index )
        if file_type_end_index != -1:
            file_type = extract_file_type(output[file_type_index + len('[音频]'):file_type_end_index].strip())
        else:
            file_type = None
    else:
        file_type = None

    # 组合视频标题和文件类型
    if video_title and file_type:
        result = f'{video_title}{file_type}'
        return result

    return None

# 调用函数进行下载并获取文件名
def download_getname(url:str):
    print(url)
    file_name = download_audio(url)
    if file_name:
       return file_name
    else:
       print('无法获取文件名')
    

