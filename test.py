import base64

from github import Github

import free_ssr_auto_collector
import viencoding_auto_collector


# 输出时间
def job():
    get_ssr()
    encode_ssr()
    git_update()


def get_ssr():
    free_ssr_auto_collector.FreeSSRParse().run()
    viencoding_auto_collector.ViencodingParse().run()


def git_update():
    username = ''
    password = ''
    g = Github(username, password)
    repo = g.get_repo('sepyeight/SSRCollector')
    if repo.get_contents(''):
        contents = repo.get_contents("ssr_encode_list.txt", ref='test')
        repo.delete_file(contents.path, "remove test", contents.sha, branch="test")
    with open('ssr_encode_list.txt', 'r') as file:
        content = file.read()
    repo.create_file("ssr_encode_list.txt", 'test', content,
                     branch="test")


def encode_ssr():
    print('encode')
    with open('ssr_list.txt', 'r') as file:
        lines = file.read()
        lines = base64.b64encode(lines.encode('utf-8'))
        lines = lines.decode('utf-8')
        with open('ssr_encode_list.txt', 'w') as encode_file:
            encode_file.write(lines)


if __name__ == '__main__':
    job()
