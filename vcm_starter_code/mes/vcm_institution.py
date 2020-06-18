from mTree.microeconomic_system.institution import Institution
from mTree.microeconomic_system.directive_decorators import *
from mTree.microeconomic_system.message import Message
import math
import random
import logging

EXPERIMENT = 25


@directive_enabled_class
class VCMInstitution(Institution):
    def __init__(self):
        pass

    @directive_decorator("init_institution")
    def init_institution(self, message:Message):
        if self.debug:
            print("Institution: received institution init ...")
