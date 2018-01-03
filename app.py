import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine

API_TOKEN ='320755843:AAE8rUjqp3eSX_nKeNPkr6ilBvKgwi1NxbU'
WEBHOOK_URL ='https://75579bc8.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)


machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
        'state3',
        'state4',
        'state5',
        'state6',
        'state7',
        'state8'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state5',
            'conditions': 'is_going_to_state5'
        },
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state6',
            'conditions': 'is_going_to_state6'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state4',
            'conditions': 'is_going_to_state4'
        },
        {
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'state7',
            'conditions': 'is_going_to_state7'
        },
        {
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'state8',
            'conditions': 'is_going_to_state8'
        },
        {
            'trigger': 'go_back',
            'source': 'state1',
            'dest': 'user',
            'conditions': 'is_leaving_from_state1'
        },
        {
            'trigger': 'go_back',
            'source': 'state2',
            'dest': 'state1',
            'conditions': 'is_leaving_from_state2'
        },
         {
            'trigger': 'go_back',
            'source': 'state3',
            'dest': 'state1',
            'conditions': 'is_leaving_from_state3'
        },
         {
            'trigger': 'go_back',
            'source': 'state4',
            'dest': 'state1',
            'conditions': 'is_leaving_from_state4'
        },
        {
            'trigger': 'advance',
            'source': 'state5',
            'dest': 'state2',
            'conditions': 'is_leaving_from_state5'
        },
         {
            'trigger': 'advance',
            'source': 'state6',
            'dest': 'state2',
            'conditions': 'is_leaving_from_state6'
        },
        {
            'trigger': 'advance',
            'source': 'state7',
            'dest': 'state2',
            'conditions': 'is_leaving_from_state7'
        },
        {
            'trigger': 'advance',
            'source': 'state8',
            'dest': 'state2',
            'conditions': 'is_leaving_from_state8'
        },
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)
def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))

@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    machine.go_back(update)
    return 'ok'

if __name__ == "__main__":
    _set_webhook()
    app.run(host='0.0.0.0', port=5000) 
