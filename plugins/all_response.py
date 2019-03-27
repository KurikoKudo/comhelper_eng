# coding: utf-8

from slackbot.bot import respond_to
from requests import get

from .download import download
from .create_issue import create_issue
from .discussion import discussion, loop
from .create_pullrequest import create_pullrequest
from .check_users import check_all_users_by_slack
from .commit import commit
from slackbot_settings import USER_TOKEN, WORKING_DIRECTORY


@respond_to('Please show ')
def mention_download(message):
    """
    成果物ダウンロードコマンド用関数
    """
    doc_name = message.body['text'].lstrip('Please show ')
    download(message.channel, doc_name)

    message.send('I have posted ' + doc_name)


@respond_to('Please create an issue of')
def mention_issue(message):
    """
    Issue作成コマンド用関数
    """
    issue_title = message.body['text'].lstrip('Please create an issue of')

    issue_link = create_issue(issue_title)
    message.send(issue_link)


@respond_to('Please create a PullRequest of')
def mention_pr(message):
    """
    プルリクエスト作成コマンド用関数
    """
    pr_title = message.body['text'].lstrip('Please create a PullRequest of')

    pr_link = create_pullrequest(pr_title)
    message.send(pr_link)


@respond_to('Please check users information')
def mention_user(message):
    """
    ユーザー情報確認コマンド用関数
    """
    users = check_all_users_by_slack()
    message.send(users)
    message.send('上記のメンバーでユーザー情報を更新したよ！')


@respond_to('Please start discussions on ')
def mention_discussion(message):
    """
    議論コマンド用関数
    """
    discussion_title = message.body['text'].lstrip('Please start discussions on ')
    discussion_process_ready = discussion(discussion_title)

    if discussion_process_ready:
        message.send('Please start discussions!')
        loop_return = loop()

        message.send(loop_return)

    else:
        message.send('すでに議論が開始されているようです...\n終了してから議論を行なってください！')


@respond_to('Please commit')
def mention_commit(message):
    """
    コミットコマンド用関数
    """
    message_body = message.body
    path = WORKING_DIRECTORY + '/docs/'

    #　ファイルが添付されているかどうか確認
    if 'files' in message_body.keys():
        file_names = []
        for file in message_body['files']:
            file_names.append(file['name'])

            # ファイルが提供されているURLを取得
            url_private = file['url_private']

            f = open(path + file['name'], mode='w', encoding='utf-8')

            # URLからファイルを取得
            resp = get(url_private, headers={'Authorization': 'Bearer %s' % USER_TOKEN}, stream=True)

            # 取得したファイルで既存ファイルを上書き
            f.write(resp.text)

            f.close()

        message.send('I commit editing of')
        for file_name in file_names:
            message.send(file_name)

    commit_return = commit()

    message.send(commit_return)









