import pandas as pd

class DataFrameAgent:

    d_hb_lst = {'state1': ['hb1', 'hb2', 'hb3', 'hb4'],
                'state2': ['hb1', 'hb2', 'hb3', 'hb4'],
                'state3': ['hb1', 'hb2'],
                'state4': ['hb1', 'hb2'],
                'state5': ['hb1', 'hb2']}

    def __init__(self, bp_id, state_id):
        self.bp_id = bp_id
        self.state_id = state_id

