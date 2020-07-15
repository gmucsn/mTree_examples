from mTree.microeconomic_system.institution import Institution
from mTree.microeconomic_system.directive_decorators import *
from mTree.microeconomic_system.message import Message
import math
import random
import logging

EXPERIMENT = 25


@directive_enabled_class
class BasicInstitution2(Institution):
    def __init__(self):
        self.agents = None

        self.min_item_value = 10
        self.max_item_value = 25

        self.bids_outstanding = None

        self.item_for_auction = None
        self.error_for_auction = None
        self.bids = []

    @directive_decorator("init_institution")
    def init_institution(self, message:Message):
        if self.debug:
            print("Institution 2: received institution init ...")

    @directive_decorator("register_collateral")
    def register_collateral(self, message:Message):
        self.log_experiment_data({"institution_collateral":"collateral request received"})
        
    @directive_decorator("register_for_collateral")
    def register_for_collateral(self, message:Message):
        self.agents = message.get_payload()["agents"]
        for agent in self.agents:
                new_message = Message()  # declare message
                new_message.set_sender(self.myAddress)  # set the sender of message to this actor
                new_message.set_directive("register_for_collateral")
                self.send(agent, new_message)  # receiver_of_message, message


    @directive_decorator("start_experiment")
    def start_experiment(self, message:Message):
        # send instructions and prompt lender for rate_of_return_offer
        if self.debug:
            print("INSTITUTION: Start Experiment")

    @directive_decorator("clear_auction")
    def clear_auction(self, message: Message):
        logging.log(EXPERIMENT, "Institution 2 ready to accept" )
        self.log_experiment_data({"Institution 2":"test"})
        
