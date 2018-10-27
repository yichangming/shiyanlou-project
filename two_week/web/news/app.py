from flask import Flask,render_template
from flask import redirect,url_for
import os
import json

app = Flask(__name__)


def file_name(file_dir,file_rear):   
    L=[]   
    for root, dirs, files in os.walk(file_dir):  
        for f in files:
            if os.path.splitext(f)[1] == file_rear:
                L.append(os.path.join(root,f))
    return L

def get_files_dir():
    pwd = os.getcwd()
    father_path=os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")
    file_path = os.path.join(father_path,'files')
    return file_path

@app.route('/')
def index():
    files_dir_path = get_files_dir()
    all_json_files = file_name(files_dir_path,'.json')
    title_list = []
    for jf in all_json_files:
        with open(jf) as f:
            data = json.load(f)
            for key,value in data.items():
                if key == 'title':
                    title_list.append(value)
    return render_template('index.html', file_title=title_list)
    # 显示文章名称的列表
    # 也就是 /home/shiyanlou/files/ 目录下所有 json 文件中的 `title` 信息列表

@app.route('/files/<filename>')
def file(filename):
    files_dir_path = get_files_dir()
    filenames = filename+'.json'
    file_path = os.path.join(files_dir_path, filenames)
    content = ''
    if os.path.exists(file_path) == True:
        with open(file_path) as f:
            #data = json.load(f)
            #for key,value in data.items():
            #    if key == 'content':
            #    content = value
    #if content !='':
            return render_template('file.html', file_content=f)
    #else:
    return render_template('404.html')
    # 读取并显示 filename.json 中的文章内容
    # 例如 filename='helloshiyanlou' 的时候显示 helloshiyanlou.json 中的内容
    # 如果 filename 不存在，则显示包含字符串 `shiyanlou 404` 404 错误页面

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run()
