from mTree.microeconomic_system.directive_decorators import *
from mTree.microeconomic_system.message import Message
from mTree.microeconomic_system.agent import Agent
import logging
import random

EXPERIMENT = 25


@directive_enabled_class
class BasicAgent(Agent):
    def __init__(self):
        self.endowment = None
        self.institution = None
        self.item_for_bidding = None
        self.win_rate = 0

    @directive_decorator("init_agent")
    def init_agent(self, message: Message):
        if self.debug:
            print("BORROWER: Borrower initiated")

    @directive_decorator("auction_result")
    def auction_result(self, message: Message):
        #logging.log(EXPERIMENT, "Agent received item for bid %s", message.get_payload())
        if message.get_payload()["status"] == "winner":
            if "win_rate" not in self.agent_memory.keys():
                self.agent_memory["win_rate"] = 0
            self.agent_memory["win_rate"] = self.agent_memory["win_rate"] + 1 
        elif message.get_payload()["status"] == "loser":
            if "loss_rate" not in self.agent_memory.keys():
                self.agent_memory["loss_rate"] = 0
            self.agent_memory["loss_rate"] = self.agent_memory["loss_rate"] + 1 


    @directive_decorator("set_endowment")
    def set_endowment(self, message: Message):
        self.endowment = message.get_payload()["endowment"]

    @directive_decorator("item_for_bidding")
    def item_for_bidding(self, message: Message):
        self.min_value = message.get_payload()["min_value"]
        self.max_value = message.get_payload()["max_value"]
        self.institution = message.get_sender()
        logging.log(EXPERIMENT, "Agent received item for bid %s - %s", str(self.min_value), str(self.max_value) )
        self.make_bid()

    def make_bid(self):
        self.mtree_properties
        new_message = Message()  # declare message
        new_message.set_sender(self.myAddress)  # set the sender of message to this actor
        new_message.set_directive("bid_for_item")
        bid_value = self.min_value
        print(self.agent_memory)
        if "loss_rate" in self.agent_memory.keys():
            if self.agent_memory["loss_rate"] > 0:
                bid_value = bid_value + self.agent_memory["loss_rate"]
        
        
        new_message.set_payload({"bid": bid_value})
        self.send(self.institution, new_message)  # receiver_of_message, message
