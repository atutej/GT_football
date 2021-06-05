import pandas as pd
import numpy as np
import nashpy as nash
from engine import GTEngine
from dataloader import FootballData
import argparse

returns_type = ('elp', 'edgd')
parser = argparse.ArgumentParser(description="Nash Equilibrium for Football Tactics")
parser.add_argument("--data", type=str, default="data/data.csv")
parser.add_argument("--rtype", type=str, default='elp', choices=returns_type)

args = parser.parse_args()

data = FootballData(args.data)
eng = GTEngine(data)
eng.calculate_nash_equilibrium(args.rtype)
eng.visualise()