from flask import Flask, request
import requests
from queue import Queue
import setu


# CQ docs at https://docs.go-cqhttp.org/cqcode/


app=Flask(__name__)
MAX_MES_ID_Q_SIZE=10
message_id_queue=Queue(maxsize=MAX_MES_ID_Q_SIZE)     # message_id queue stores recent message ids to prevent redundant message received
message_id_queue_set=set()

@app.route('/', methods=["Post"])
def post_data():
    data=request.get_json()
    if  data['post_type']=='meta_event' and data['meta_event_type']=='heartbeat':   # ignores heartbeat event
        return 'OK'
    message_id=data['message_id']
    if message_id in message_id_queue_set:      # ignores redundant message
        return 'OK'
    if message_id_queue.qsize()==MAX_MES_ID_Q_SIZE:
        message_id_queue_set.remove(message_id_queue.get())
    message_id_queue.put(message_id)
    message_id_queue_set.add(message_id)

    for k, v in data.items():
        print(k, v)
    # print('===============')
    message=data['message']
    if message =='bd':
        send('[CQ:share,url=http://baidu.com,title=百度]')
    elif message=='rep':
        time=data['time']
        id=data['message_id']
        send(f'[CQ:reply,id={id}]test reply')
    elif message=='色图':
        send(setu.get_setu())
    else:
        send(message)
    return 'OK'



def send(message):
    url=r'http://127.0.0.1:5700/send_msg'
    # data=request.get_json()
    params={
        'message_type ':'private',
        'user_id':1482516617,
        'message':message
    }
    requests.get(url, params=params)


def get_setu():
    try:
        request_url='http://www.dmoe.cc/random.php'
        params = {'return': 'json'}
        imgurl=requests.get(request_url, params=params).json()['imgurl']
        return f'[CQ:image,file={imgurl}]'
    except:
        return '色图寄了'


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5701)