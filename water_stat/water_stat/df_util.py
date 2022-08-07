from os import path
import pandas as pd
import numpy as np

class DFAgent:

    data_folder = '/home/yizaochen/codes/cug_rna/hbond_analysis'
    d_hb_lst = {'state1': ['hb1', 'hb2', 'hb3', 'hb4'],
                'state2': ['hb1', 'hb2', 'hb3', 'hb4'],
                'state3': ['hb1', 'hb2'],
                'state4': ['hb1', 'hb2'],
                'state5': ['hb1', 'hb2']}
    md_lst = [f'md{i}' for i in range(3)]

    def __init__(self, bp_id, state_id):
        self.bp_id = bp_id
        self.state_id = state_id

        self.hb_lst = self.d_hb_lst[self.state_id]
        self.bp_folder = path.join(self.data_folder, self.bp_id)
        self.state_folder = path.join(self.bp_folder, self.state_id)
        self.f_df = path.join(self.state_folder, 'merge.csv')
        self.df = None

    def make_df(self):
        d_result = dict()
        for hb_id in self.hb_lst:
            d_result[hb_id] = self.get_data_lst(hb_id)
        self.df = pd.DataFrame(d_result)
        self.df.to_csv(self.f_df, index=False)

    def read_df(self):
        self.df = pd.read_csv(self.f_df)

    def get_data_lst(self, hb_id):
        data_lst = list()
        for md_id in self.md_lst:
            f_dat = path.join(self.state_folder, md_id, f'{hb_id}.dat')
            data = np.genfromtxt(f_dat, dtype=int)
            data_lst += list(data[:-1, 1])
        return data_lst