from mTree.microeconomic_system.environment import Environment
from mTree.microeconomic_system.directive_decorators import *
from mTree.microeconomic_system.message import Message
from mTree.components.property_types import MTreeBoolProperty, MTreeIntProperty, MTreeRealProperty, MTreeSetProperty
from mTree.microeconomic_system.property_decorators import *
import logging
import random
EXPERIMENT = 25

@directive_enabled_class
class VCMEnvironment(Environment):
    def __init__(self):
        pass

    @directive_decorator("start_environment") 
    def start_environment(self, message:Message):
        logging.log(EXPERIMENT, "Environment start...")
        self.initialize_agents()
   

    def initialize_agents(self):
        for agent in self.agents:
            new_message = Message()  
            new_message.set_sender(self)  
            new_message.set_directive("<INSERT DIRECTIVE NAME>")  
            new_message.set_payload({"<PAYLOAD>": "<PAYLOAD VALUE>"})
            self.send(agent[0], new_message )
