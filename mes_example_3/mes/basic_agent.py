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

    @directive_decorator("init_agent")
    def init_agent(self, message: Message):
        if self.debug:
            print("BORROWER: Borrower initiated")

    @directive_decorator("auction_result")
    def auction_result(self, message: Message):
        logging.log(EXPERIMENT, "Agent received item for bid %s", message.get_payload())
        new_message = Message()  # declare message
        new_message.set_sender(self.myAddress)  # set the sender of message to this actor
        new_message.set_directive("register_collateral")
        new_message.set_payload({"bid": self.min_value})
        self.send(self.collateral_institution, new_message)  # receiver_of_message, message


    @directive_decorator("register_for_collateral")
    def register_for_collateral(self, message: Message):
        self.collateral_institution = message.get_sender()

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
        print("Making a bid... Total Endowment: ", self.endowment)
        self.mtree_properties
        new_message = Message()  # declare message
        new_message.set_sender(self.myAddress)  # set the sender of message to this actor
        new_message.set_directive("bid_for_item")
        new_message.set_payload({"bid": self.min_value})
        self.send(self.institution, new_message)  # receiver_of_message, message
