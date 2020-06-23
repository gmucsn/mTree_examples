from mTree.microeconomic_system.institution import Institution
from mTree.microeconomic_system.directive_decorators import *
from mTree.microeconomic_system.message import Message
import math
import random
import logging

EXPERIMENT = 25


@directive_enabled_class
class BasicInstitution(Institution):
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
            print("Institution: received institution init ...")

    @directive_decorator("start_experiment")
    def start_experiment(self, message:Message):
        # send instructions and prompt lender for rate_of_return_offer
        if self.debug:
            print("INSTITUTION: Start Experiment")

    @directive_decorator("start_auction")
    def start_auction(self, message:Message):
        if self.mtree_properties["num_auctions"] > 0:
            self.mtree_properties["num_auctions"] = self.mtree_properties["num_auctions"] - 1
            print("INSTITUTION: Starting Auction")
            self.agents = message.get_payload()["agents"]
            self.bids = []
            self.bids_outstanding = len(self.agents)
            self.item_for_auction = random.randint(self.min_item_value, self.max_item_value)
            for agent in self.agents:
                new_message = Message()  # declare message
                new_message.set_sender(self)  # set the sender of message to this actor
                new_message.set_directive("item_for_bidding")
                new_message.set_payload({"min_value": self.min_item_value, "max_value": self.max_item_value})
                self.send(agent[0], new_message)  # receiver_of_message, message

    @directive_decorator("accept_bid")
    def accept_bid(self, message:Message):
        # send instructions and prompt lender for rate_of_return_offer
        if self.debug:
            print("INSTITUTION: Start Experiment")

    def complete_auction(self):
        logging.log(EXPERIMENT, "Institution closing auction")

        bids = sorted(self.bids, key=lambda elem: elem[0] ,reverse=True)

        winner = bids.pop(0)
        logging.log(EXPERIMENT, "Institution auction Winner: %s -> %s -> all bids -> %s", str(winner), self.item_for_auction, bids)
        new_message = Message()  # declare message
        new_message.set_sender(self)  # set the sender of message to this actor
        new_message.set_directive("auction_result")
        new_message.set_payload({"status": "winner", "real_value": self.item_for_auction})

        self.send(winner[1].myAddress, new_message)  # receiver_of_message, message

        for agent in bids:
            new_message = Message()  # declare message
            new_message.set_sender(self)  # set the sender of message to this actor
            new_message.set_directive("auction_result")
            new_message.set_payload({"status": "loser"})
            self.send(agent[1].myAddress, new_message)  # receiver_of_message, message

        new_message = Message()  # declare message
        new_message.set_sender(self)  # set the sender of message to this actor
        new_message.set_directive("start_auction")
        new_message.set_payload({"agents": self.agents})
        self.send(self.myAddress, new_message)  # receiver_of_message, message

    @directive_decorator("bid_for_item")
    def accept_bid(self, message: Message):
        bidder = message.get_sender()
        bid = message.get_payload()["bid"]
        self.bids.append((bid, bidder))
        self.bids_outstanding -= 1
        if self.bids_outstanding == 0:
            self.complete_auction()

