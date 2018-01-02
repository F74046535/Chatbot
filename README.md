# Chatbot

# Finite state machine
![Image of fsm](https://github.com/F74046535/Chatbot/blob/master/show_fsm.JPG)

# Usage
The initial state is set to `user`.

This is a chatbot which is used to talk to the snoopy dog .

* user:
        * Input:"hello"
                * Reply:"Hi,my name is snoopy. Do you want to go to challenge me?"
                * Input:"go"
                         * Reply:"please choose what you want to challenge?(a),(b)or give up"
                         * Input:"a"
                                   * Reply:"Is snoopy's birthday 8/10? yes or no?"
                                   * Input:"yes"
                                           * Reply: "Yes,you are right."
                                   * Input:"no"
                                           * Reply: "Oops,wrong answer!"
                         * Input:"b"
                                   * Reply:"Hamburger is my favorite food? yes or no?"
                                   * Input:"yes"
                                           * Reply: "Oops,wrong answer!My favorite food is pizza."
                                   * Input:"no"
                                           * Reply: "Yes,you are right.My favorite food is pizza."
                         * Input:"give up"
                                   * Reply:"Hi,my name is snoopy. Do you want to go to challenge me?"(go_back to sate1)

