from mTree.microeconomic_system.environment import Environment
from mTree.microeconomic_system.directive_decorators import *
from mTree.microeconomic_system.message import Message
from mTree.components.property_types import MTreeBoolProperty, MTreeIntProperty, MTreeRealProperty, MTreeSetProperty
from mTree.microeconomic_system.property_decorators import *
import logging
import random
EXPERIMENT = 25

@directive_enabled_class
class BasicEnvironment(Environment):
    def __init__(self):
        self.num_auctions = 10

    @directive_decorator("start_environment") # TODO schema
    def start_environment(self, message:Message):
        logging.log(EXPERIMENT, "Environment start...")
        self.provide_endowment()
        self.start_auction()

    def start_auction(self):
        new_message = Message()  # declare message
        new_message.set_sender(self)  # set the sender of message to this actor
        new_message.set_directive("start_auction")
        new_message.set_payload({"agents": self.agents})
        self.send(self.institutions[0], new_message)  # receiver_of_message, message

    def provide_endowment(self):
        endowment = self.mtree_properties["agent_endowment"]
        for agent in self.agents:
            new_message = Message()  # declare message
            new_message.set_sender(self)  # set the sender of message to this actor
            new_message.set_directive("set_endowment")  # Set the directive (refer to 3. Make Messages) - has to match reciever decorator
            new_message.set_payload({"endowment": endowment})
            self.send(agent[0], new_message )  # receiver_of_message, message
