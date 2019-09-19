import base64

from apscheduler.schedulers.blocking import BlockingScheduler
from github import Github

import free_ssr_auto_collector
import viencoding_auto_collector


def get_ssr():
    print('start')
    free_ssr_auto_collector.FreeSSRParse().run()
    viencoding_auto_collector.ViencodingParse().run()
    print('finish')


def encode_ssr():
    print('encode start')
    with open('ssr_list.txt', 'r') as file:
        lines = file.read()
        lines = base64.b64encode(lines.encode('utf-8'))
        lines = lines.decode('utf-8')
        with open('ssr_encode_list.txt', 'w') as encode_file:
            encode_file.write(lines)

    print('encode end')


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


def job():
    get_ssr()
    encode_ssr()


# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', day_of_week='0-6', hour=8, minute=50)
scheduler.start()
