from slacker import Slacker
import slack_config

slack_token = slack_config.token
slack = Slacker(slack_token)

markdown_text = '''
This message is plain.
*This message is bold.*
'This message is code.'
_This message is italic._
~This message is strike.~
'''

attach_dict = {
    'color'         : '#ff0000',
    'author_name'   : 'INVESTAR',
    'author_link'   : 'github.com/yeonhodev',
    'title'         : '오늘의 증시 KOSPI',
    'title_link'    : 'http://finance.naver.com/sise/sise_index.nhn?code=KOSPI',
    'text'          : '2,326.13 △11.89 (+0.51%)',
    'image_url'     : 'https://ssl.pstatic.net/imgstock/chart3/day/KOSPI.png'
}

attach_list = [attach_dict]
slack.chat.post_message(channel="#general", text=markdown_text, attachments=attach_list)