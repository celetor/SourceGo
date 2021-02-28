import os, requests


def get_file_list(folder_dir: str):
    dir_list = os.listdir(folder_dir)
    f_list = []
    for d in dir_list:
        sub_dir = os.path.join(folder_dir, d)
        if os.path.isfile(sub_dir) and sub_dir.endswith('.json'):
            f_list.append(d)
    return f_list


if __name__ == '__main__':
    work_space = os.environ.get('GITHUB_WORKSPACE')
    source_path = os.path.join(work_space, 'book_source')
    file_list = []
    url_list = []
    if os.path.exists(source_path):
        file_list = get_file_list(source_path)
    for file in file_list:
        url = f'/Celeter/SourceGo@main/book_source/{file}'
        url_list.extend(url)
        print(requests.get(url).text)
