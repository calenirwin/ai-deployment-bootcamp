import os

import pandas as pd
import numpy as np
from data_const import *
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import seaborn as sns


class PreprocessingPipeline:
    def __init__(self,folder_data,subject_ID,activity_type):
        self.folder_data = folder_data
        self.subject_ID = subject_ID
        self.activity_type = activity_type


    def read_dat_file(self):
        """

        :param file:
        :return:
        """
        self.file = self.folder_data + self.activity_type + '/' + self.subject_ID + ".dat"
        self.df = pd.read_csv(self.file, sep=' ',header = None,names = COLUMNS_DATASET)
        self.filter_features()

    def read_specific_file(self,file):
        """

        :param file:
        :return:
        """
        file = self.folder_data + self.activity_type + '/' + file
        self.df = pd.read_csv(file, sep=' ',header = None,names = COLUMNS_DATASET)
        #self.filter_features()

    def get_list_subjectid(self):
        """

        :return:
        """
        folder = self.folder_data + self.activity_type
        self.list_subjects = sorted(os.listdir(folder))
        return self.list_subjects


    def get_activity_information(self):
        """

        :return:
        """
        plt.hist(self.dataset["Activity ID"])
        plt.show()

    def prepare_sequence(self):
        """

        :return:
        """
        sequence = None 
        return sequence

    def na_value_information(self):
        """

        :return:
        """
        return None

    def filter_features(self):
        """
        This functions will extract relevant features from dataframe of different subjects
        :return:
        """
        self.df = self.df[OVERALL_FEATURES+SELECTED_LABELS]


    def add_subject_ID(self,subject_id):
        """
        This function assign a set of tabular data a subject ID
        :param subject_id:
        :return:
        """
        self.df["Subject ID"] = subject_id


    def gather_data(self,loop_back,overlap):
        """

        :return:
        """
        dataset = {}
        for i in range(len(self.get_list_subjectid())):
            if i ==0 :
                self.read_specific_file(self.list_subjects[i])
                #self.add_subject_ID(self.list_subjects[i])
                self.filter_features()
                dataset[self.list_subjects[i]] = self.create_chunks(loop_back,overlap)
                #print(len(dataset[self.list_subjects[i]][2]))
            else :
                self.read_specific_file(self.list_subjects[i])
                #self.add_subject_ID(self.list_subjects[i])
                self.filter_features()
                dataset[self.list_subjects[i]] = self.create_chunks(loop_back,overlap)
                #self.dataset = pd.concat([self.dataset,self.df])

        #self.filter_features()
        return dataset


    def activity_done_by_subjects(self):
        """

        :return:
        """
        return None

    def create_chunks(self,loop_back,overlap):
        """

        """
        sorted_dataset = {}
        ite = 0
        not_unique = 0
        n_iteration = len(self.df)//(loop_back-overlap)
        for i in range(0,n_iteration):
            ite+=1
            chunk = self.df.iloc[(loop_back-overlap)*i:(loop_back-overlap)*i+loop_back]
            if not chunk.isnull().values.any():
                if len(chunk['Activity ID'].unique()) == 1 :
                    if chunk["Activity ID"].unique()[0] not in sorted_dataset.keys():
                        sorted_dataset[chunk["Activity ID"].unique()[0]] = []
                    sorted_dataset[chunk["Activity ID"].unique()[0]].append(chunk.values)
                else :
                    not_unique +=1

        print("n_iteration" , ite)
        print("not_unique",not_unique)
        for k,v in sorted_dataset.items():
            if k in ANOMALY_ID :
                print(len(sorted_dataset[k]))
        return sorted_dataset


    def constitute_dataset(self,loop_back,overlap,n_samples_normal,n_samples_anomaly):
        """
        From the data gathered, we will create a balanced dataset, with at most n samples of activity per subject per activity
        """
        dataset = self.gather_data(loop_back=loop_back,overlap=overlap)
        normal_data = []
        anomaly_data = []
        n_sample=  {}
        for subject,v in dataset.items():
            n_sample [subject] = {}
            for activity,v2, in v.items():
                if activity in ANOMALY_ID :
                    anomaly_data.extend(v2[:n_samples_anomaly])
                    n_sample[subject][activity] = len(anomaly_data)
                else :
                    normal_data.extend(v2[:n_samples_normal])
                    n_sample[subject][activity] = len(normal_data)

        X_train, X_test, y_train, y_test = train_test_split(np.asarray(normal_data)[:,:,:27], np.asarray(normal_data)[:,0,27], test_size=0.10, random_state=42)
        X_anomaly = np.asarray(anomaly_data)[:,:,:27]
        y_anomaly = np.asarray(anomaly_data)[:,0,27]
        X_validation = np.concatenate((X_test,X_anomaly))
        y_validation = np.concatenate((y_test,y_anomaly))
        #plt.figure(figsize = (20,15))
        #sns.histplot(y_anomaly,kde = True,bins = 4)
        #sns.histplot(y_test,kde = True)
        #plt.show()
        return X_train,X_validation,y_train,y_validation



if __name__ == "__main__":
    folder_data = "data/PAMAP2_Dataset/"
    subject_ID = "subject102"
    activity_type = "Protocol"
    data_prep = Data_processing(folder_data,subject_ID=subject_ID,activity_type=activity_type)
    #data_prep.gather_data(loop_back=90,overlap=10)
    data_prep.constitute_dataset(loop_back=90,overlap=0,n_samples_anomaly=50,n_samples_normal=200)
    #data_prep.get_activity_information()
    #data_prep.filter_features()
    #data_prep.add_subject_ID(subject_id=subject_ID)
    #data.dropna(inplace=True)
