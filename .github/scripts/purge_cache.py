import os, requests


def get_file_list(folder_dir: str):
    dir_list = os.listdir(folder_dir)
    file_list = []
    folder_list = []
    for d in dir_list:
        sub_dir = os.path.join(folder_dir, d)
        if os.path.isfile(sub_dir):
            file_list.append(d)
        else:
            folder_list.append(d)
    for d in folder_list:
        sub_dir = os.path.join(folder_dir, d)
        f_list = os.listdir(sub_dir)
        for f in f_list:
           if os.path.isfile(os.path.join(sub_dir, f)): 
                file_list.append(f'{d}/{f}')      
    return file_list


if __name__ == '__main__':
    work_space = os.environ.get('GITHUB_WORKSPACE')
    source_path = os.path.join(work_space, 'book_source')
    folder_list = []
    url_list = []
    if os.path.exists(source_path):
        for file in get_file_list(source_path):
            url = f'/Celeter/SourceGo@main/book_source/{file}'
            print(url)
  
