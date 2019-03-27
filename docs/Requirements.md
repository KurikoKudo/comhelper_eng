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
| @comhelper Please create an issue of _Requirements ver4_ |  hub create issue -m ' _Requirements ver4_ ' |

