from os import path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class PlotAgent:
    state_lst = [f'state{i}' for i in range(1,6)]
    data_folder = '/home/yizaochen/codes/cug_rna/hbond_analysis'
    total_frame = 30000

    def __init__(self, bp_id):
        self.bp_id = bp_id
        self.x_array = np.arange(5)
        self.y_array = self.get_y_array()

    def plot_main(self, figsize):
        fig, ax = plt.subplots(figsize=figsize)
        ax.bar(self.x_array, self.y_array, width=0.8)
        ax.set_xticks(self.x_array)
        ax.set_xticklabels(self.state_lst)
        ax.set_ylabel("Frequency")
        ax.set_ylim(0, 0.69)
        return fig, ax

    def get_y_array(self):
        y_lst = list()
        for state_id in self.state_lst:
            self.f_df = path.join(self.data_folder, self.bp_id, state_id, 'merge.csv')
            df = pd.read_csv(self.f_df)
            if state_id in ['state1', 'state2']:
                mask = df.gt(0).sum(axis=1) >= 3
            else:
                mask = df.gt(0).sum(axis=1) == 2
            y_lst.append( float(df[mask].shape[0]) / self.total_frame)
        return np.array(y_lst)