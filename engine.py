from __future__ import unicode_literals, print_function
import pandas as pd
import numpy as np
import nashpy as nash
from payoff import PayoffTable

from prompt_toolkit import print_formatted_text, HTML

class GTEngine():
    def __init__(self, data):
        self.payoff_table = None
        self.data = data
        self.eqs = None

    def calculate_nash_equilibrium(self,returns_type='elp'):
        df, h_tactic_dict, a_tactic_dict = self.data.get_data()
        self.payoff_table = PayoffTable(h_tactic_dict,a_tactic_dict)
        H, A = self.payoff_table.calculate_payoffs(df,returns_type)

        ftbl = nash.Game(H,A)
        self.eqs = ftbl.support_enumeration()


    def visualise(self):
        eqs = list(self.eqs)

        h_tactic_dict, a_tactic_dict = self.payoff_table.get_tactic_dicts()
        print("<u>Strategy for HOME TEAM:</u>")
        print ("{:<30} {:<30}".format('Strategy', 'Mixed Probs',))
        for idx,eq in enumerate(list(eqs[0][0])):
            print ("{:<30} {:<30}".format(h_tactic_dict[idx],eq))
        print("<u>Strategy for AWAY TEAM:</u>")
        print ("{:<30} {:<30}".format('Strategy', 'Mixed Probs',))
        for idx,eq in enumerate(list(eqs[0][1])):
            print ("{:<30} {:<30}".format(a_tactic_dict[idx],eq))
        