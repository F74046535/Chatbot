from transitions.extensions import GraphMachine

class TocMachine(GraphMachine):
    
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )
    
    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'hello'
        
    def is_leaving_from_state1(self, update):
        text = update.message.text
        return text.lower() == 'no'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'go'
    def is_leaving_from_state2(self, update):
        text = update.message.text
        return text.lower() == 'give up'
    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'a'
    def is_leaving_from_state3(self, update):
        text = update.message.text
        return text.lower() == 'back'
    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == 'b'
    def is_leaving_from_state4(self, update):
        text = update.message.text
        return text.lower() == 'back'
    def is_going_to_state5(self, update):
        text = update.message.text
        return text.lower() == 'yes'
    def is_leaving_from_state5(self, update):
        text = update.message.text
        return text.lower() == 'back'
    def is_going_to_state6(self, update):
        text = update.message.text
        return text.lower() == 'no'
    def is_leaving_from_state6(self, update):
        text = update.message.text
        return text.lower() == 'back'
    def is_going_to_state7(self, update):
        text = update.message.text
        return text.lower() == 'yes'
    def is_leaving_from_state7(self, update):
        text = update.message.text
        return text.lower() == 'back'
    def is_going_to_state8(self, update):
        text = update.message.text
        return text.lower() == 'no'
    def is_leaving_from_state8(self, update):
        text = update.message.text
        return text.lower() == 'back'
    def on_enter_state1(self, update):
        update.message.reply_text("Hi,my name is snoopy. Do you want to go to challenge me?")
        update.message.reply_photo('https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Snoopy_Peanuts.png/200px-Snoopy_Peanuts.png')
        #self.go_back(update)


    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("please choose what you want to challenge?(a),(b)or give up")
        #self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')
   
    def on_enter_state3(self, update):
        update.message.reply_text("Is snoopy's birthday 8/10? yes or no?")
    def on_enter_state4(self, update):
        update.message.reply_text("Hamburger is my favorite food? yes or no?")
    def on_enter_state5(self, update):
        update.message.reply_text("Yes,you are right.")
        update.message.reply_photo('http://wportfolio.wzu.edu.tw/blog/attach/253/44253/62/bf_58068_9318060_88064_clip-art-snoopy-346942.jpg')
    def on_enter_state6(self, update):
        update.message.reply_text("Oops,wrong answer!")
    def on_enter_state7(self, update):
        update.message.reply_text("Oops,wrong answer!My favorite food is pizza.")
    def on_enter_state8(self, update):
        update.message.reply_text("Yes,you are right.My favorite food is pizza.")
        update.message.reply_photo('http://wportfolio.wzu.edu.tw/blog/attach/253/44253/62/bf_58068_9318060_88064_clip-art-snoopy-346942.jpg')
    
