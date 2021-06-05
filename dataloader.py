import pandas as pd
import numpy as np


class FootballData():
    def __init__(self,data_path):

        df = pd.read_csv("Datos_HT.csv",sep=';')

        df = df[df["Home Tactic"].notna()]
        df = df[df["Away Tactic"].notna()]

        home_tactics = list(pd.unique(df["Home Tactic"]))
        away_tactics = list(pd.unique(df["Away Tactic"]))

        results = []
        diffs = []
        for idx,row in df.iterrows():
            diff = row["Home Goals"] - row["Away Goals"]
            if diff>0:
                result='H'
                results.append(result)
            elif diff==0:
                result='D'
                results.append(result)
            else:
                result='A'
                results.append(result)
            diffs.append(np.abs(diff))
        df["Results"] = results
        df["Diffs"] = diffs

        h_tactic_dict = {}
        a_tactic_dict = {}
        for i,h_tactic in enumerate(home_tactics):
            h_tactic_dict[i] = h_tactic
        for j,a_tactic in enumerate(away_tactics):
            a_tactic_dict[j] = a_tactic

        self.df = df
        self.h_tactic_dict = h_tactic_dict
        self.a_tactic_dict = a_tactic_dict

    def get_data(self):
        return self.df, self.h_tactic_dict, self.a_tactic_dict

