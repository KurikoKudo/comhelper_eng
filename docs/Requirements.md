# Requirements specification version 1


# List of commands
＊ _Italic style_ is used by changing to arbitrary string.

## "download an artifact" command 

Post a markdown file of arbitrary artifact to slack.

| Instruction to slackbot | send command by comhelper |
| --- | --- |
| @comhelper Please show _Requirements_ |  git pull origin master |


## "create an issue" command  

Create an issue with any title and post the link of the created issue to slack

| Instruction to slackbot | send command by comhelper |
| --- | --- |
| @bot _仕様書第4版_ のIssueを作成して |  hub create issue -m ' _仕様書第4版_ ' |

## 議論開始コマンド  

_任意のコミットタイトル(該当issueがある場合は先頭に#番号を！)_ をつけ、  
これ以降のメッセージをcommit.txtに「名前:メッセージ」の形式で追記していく。

| slackbot への指示 | bot によるコマンド発行  |
| --- | --- |
| @bot _#3 ログイン機能_ の議論を開始 |  echo _#3 ログイン機能_ > commit.txt |

議論終了コマンドがくるまで  
echo _name:message_ >> commit.txt  
を続ける  
**議論が終了されていない時はエラーを返す**


## 議論終了コマンド
議論開始コマンドが発行されてからのslackのやりとりをコミットメッセージとして  
コミットし、同時にpushも行う  

| slackbot への指示 | bot によるコマンド発行  |
| --- | --- |
| @bot 議論を終了 | git commit --allow-empty -F commit.txt |

--allow-empty オプションによって差分がなくてもコミット可能  
**議論が開始されていない時はエラーを返す**

## PullRequest 作成コマンド  

_任意のタイトル_ でプルリクエストを作成

| slackbot への指示 | bot によるコマンド発行  |
| --- | --- |
| @bot _仕様書第4版_ のプルリクを作成して | hub pull-request -m ' _仕様書第4版_ ' |


# 議論した内容をもとに編集する
**差分が表示される**