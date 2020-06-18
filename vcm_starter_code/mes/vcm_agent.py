from mTree.microeconomic_system.directive_decorators import *
from mTree.microeconomic_system.message import Message
from mTree.microeconomic_system.agent import Agent
import logging
import random

EXPERIMENT = 25


@directive_enabled_class
class VCMAgent(Agent):
    def __init__(self):
        self.endowment = None
        self.institution = None
        self.item_for_bidding = None

    @directive_decorator("init_agent")
    def init_agent(self, message: Message):
        if self.debug:
            print("BORROWER: Borrower initiated")
