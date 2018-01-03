# Chatbot

# Finite state machine
![Image of fsm](https://github.com/F74046535/Chatbot/blob/master/show_fsm.JPG)

# Usage
The initial state is set to `user`.

This is a chatbot which is used to talk to the snoopy dog .

# Run
run app.py

* user
       
         * Input:  "hello"
                   * Reply:"Hi,my name is snoopy. Do you want to go to challenge me?"(state1)
                   * Input:  "go"
                         * Reply:"please choose what you want to challenge?(a),(b)or give up"(state2)
                         * Input:"a"
                                   * Reply:"Is snoopy's birthday 8/10? yes or no?"(state3)
                                   * Input:"yes"
                                           * Reply: "Yes,you are right."(state5)
                                   * Input:"no"
                                           * Reply: "Oops,wrong answer!"(state6)
                         * Input:"b"
                                   * Reply:"Hamburger is my favorite food? yes or no?"(state4)
                                   * Input:"yes"
                                           * Reply: "Oops,wrong answer!My favorite food is pizza."(state7)
                                   * Input:"no"
                                           * Reply: "Yes,you are right.My favorite food is pizza."(state8)
                         * Input:"give up"
                                   * Reply:"Hi,my name is snoopy. Do you want to go to challenge me?"(go_back to sate1)

## Author
[F74046535](https://github.com/F74046535)
                 
              
