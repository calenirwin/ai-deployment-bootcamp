import os

import pandas as pd
import numpy as np
from data_const import *
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


class PreprocessingPipeline:
    def __init__(self, folder_data, subject_ID, activity_type):
        self.folder_data = folder_data
        self.subject_ID = subject_ID
        self.activity_type = activity_type

        self.file = ""
        self.df = None
        self.list_subjects = []

    def read_dat_file(self):
        self.file = self.folder_data + activity_type + '/' + self.subject_ID + ".dat"
        self.df = pd.read_csv(self.file, sep=' ',header = None,names = COLUMNS_DATASET)
        self.filter_features()

    def read_specific_file(self, file):
        file = self.folder_data + self.activity_type + '/' + file
        self.df = pd.read_csv(file, sep=' ', header=None, names=COLUMNS_DATASET)
        #self.filter_features()

    def get_list_subjectid(self):
        folder = self.folder_data + self.activity_type
        self.list_subjects = sorted(os.listdir(folder))
        return self.list_subjects

    def get_activity_information(self):
        plt.hist(self.dataset["Activity ID"])
        plt.show()

    def prepare_sequence(self):
        sequence = None 
        return sequence

    def na_value_information(self):
        return None

    def filter_features(self):
        """
        This functions will extract relevant features from dataframe of different subjects
        :return:
        """
        self.df = self.df[OVERALL_FEATURES+SELECTED_LABELS]

    def add_subject_ID(self, subject_id):
        """
        This function assign a set of tabular data a subject ID
        :param subject_id:
        :return:
        """
        self.df["Subject ID"] = subject_id

    def gather_data(self, loop_back: object, overlap: object) -> object:
        data_dict = {}

        for i in range(len(self.get_list_subjectid())):
            if i == 0:
                self.read_specific_file(self.list_subjects[i])
                #self.add_subject_ID(self.list_subjects[i])
                self.filter_features()
                data_dict[self.list_subjects[i]] = self.create_chunks(loop_back, overlap)
                #print(len(dataset[self.list_subjects[i]][2]))
            else:
                self.read_specific_file(self.list_subjects[i])
                #self.add_subject_ID(self.list_subjects[i])
                self.filter_features()
                data_dict[self.list_subjects[i]] = self.create_chunks(loop_back, overlap)
                #self.dataset = pd.concat([self.dataset,self.df])

        all_samples = [arr for subdict in data_dict.values()
                       for sublist in subdict.values()
                       for arr in sublist]
        dataset = np.stack(all_samples)
        return data_dict, dataset

    def activity_done_by_subjects(self):
        return None

    def create_chunks(self, loop_back, overlap):
        sorted_dataset = {}
        ite = 0
        not_unique = 0
        for i in range(0, len(self.df), loop_back-overlap):
            ite += 1
            chunk = self.df.iloc[(loop_back-overlap)*i:(loop_back-overlap) * i + loop_back]
            if len(chunk['Activity ID'].unique()) == 1:
                if chunk["Activity ID"].unique()[0] not in sorted_dataset.keys():
                    sorted_dataset[chunk["Activity ID"].unique()[0]] = []
                sorted_dataset[chunk["Activity ID"].unique()[0]].append(chunk.values)
            else:
                not_unique += 1
        print("n_iteration", ite)
        print("not_unique", not_unique)
        
        for k, v in sorted_dataset.items():
            print(len(sorted_dataset[k]))

        return sorted_dataset


if __name__ == "__main__":
    folder_data = "data/"
    subject_ID = "subject102"
    activity_type = "Protocol"
    data_prep = PreprocessingPipeline(folder_data, subject_ID=subject_ID, activity_type=activity_type)
    data_prep.gather_data(loop_back=90, overlap=30)
    #data_prep.get_activity_information()
    #data_prep.filter_features()
    #data_prep.add_subject_ID(subject_id=subject_ID)
    #data.dropna(inplace=True)