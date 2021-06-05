import pandas as pd
import numpy as np


class PayoffTable():
    def __init__(self,h_tactic_dict,a_tactic_dict):

        self.h_tactic_dict = h_tactic_dict
        self.a_tactic_dict = a_tactic_dict

        self.h_space = len(h_tactic_dict)
        self.a_space = len(a_tactic_dict)
        self.H = np.zeros((self.h_space,self.a_space))
        self.A = np.zeros((self.h_space,self.a_space))

    def get_tactic_dicts(self):
        return self.h_tactic_dict, self.a_tactic_dict

    def calculate_payoffs(self,df,returns_type='elp'):
        for i in self.h_tactic_dict:
            h_tactic = self.h_tactic_dict[i]
            for j in self.a_tactic_dict:
                a_tactic = self.a_tactic_dict[j]
                df_sub = df[df["Home Tactic"]==h_tactic]
                df_sub = df_sub[df_sub["Away Tactic"]==a_tactic]
                df_h = df_sub[df_sub["Results"]=='H']
                df_a= df_sub[df_sub["Results"]=='A']
                df_d = df_sub[df_sub["Results"]=='D']

                if(returns_type=='elp'):
                    h_prob = len(df_h)/(len(df_sub) + 1e-8)
                    a_prob = len(df_a)/(len(df_sub) + 1e-8)
                    d_prob = len(df_d)/(len(df_sub) + 1e-8)

                    self.H[i,j] = 3*h_prob + d_prob
                    self.A[i,j] = 3*a_prob + d_prob

                elif(returns_type=='edgd'):
                    r1 = sum(df_h["Diffs"])/(len(df_h) + 1e-8)
                    r2 = sum(df_a["Diffs"])/(len(df_a) + 1e-8)

                    self.H[i,j] = 2*(r1 - r2) + len(df_d)
                    self.A[i,j] = 2*(r2 - r1) + len(df_d)


        return self.H, self.A



