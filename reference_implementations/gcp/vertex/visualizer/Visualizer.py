import seaborn
from model_training.trainer.data_preprocessing import PreprocessingPipeline
from model_training.trainer import data_const
from sklearn.metrics import roc_curve
import numpy as np

class Visualizer:
    def __init__(self):
        """

        """
        self.prep_pipe = PreprocessingPipeline(folder_data = "data/PAMAP2_Dataset/", subject_ID="subject102",activity_type = "Protocol")


    def get_data_labels(self):
        """

        :return:
        """
        X_train, X_validation, y_train, y_validation = self.prep_pipe.constitute_dataset(loop_back=90,overlap=0,n_samples_anomaly=50,n_samples_normal=200)
        return X_train, X_validation, y_train, y_validation


    def get_prediction(self):
        """
        :return:
        """
        self.X_train, self.X_validation, self.y_train, self.y_validation = self.get_data_labels()
        self.predictions = self.X_validation
        self.truth = self.X_train[:len(self.predictions)]

    def calculate_error(self):
        """

        :return:
        """
        self.get_prediction()
        self.error = []
        for i in range (len(self.predictions)):
            self.error.append(np.sum(np.square(self.predictions[i] - self.truth[i])))

    def get_equal_error_rate(self):
        """

        :return:
        """
        self.calculate_error()
        self.labels = [0 if self.y_validation[i] not in [4,12,13,24] else 1 for i in range(len(self.y_validation))]
        fpr, tpr, thresholds = roc_curve(self.labels, self.error)
        far = fpr  # FAR = False Positive Rate
        frr = 1 - tpr  # FRR = 1 - True Positive Rate
        eer_threshold = thresholds[np.nanargmin(np.abs(far - frr))]
        eer = far[np.nanargmin(np.abs(far - frr))]
        self.plot_eer()

    def plot_eer(self,eer_threshold,normal_error,anomaly_error):
        """

        :return:
        """
        plt.figure(figsize=(10, 6))
        plt.hist(normal_error, bins=50, alpha=0.5, label='Normal labels', color='b')
        plt.hist(anomaly_error, bins=50, alpha=0.5, label='Anomaly Labels', color='r')
        plt.axvline(eer_threshold, color='k', linestyle='--', label=f'Equal Error rate: {eer_threshold:.4f}')
        plt.title('Distrinution of error per test sample')
        plt.xlabel('Error distribution')
        plt.ylabel('Density')
        plt.legend()
        plt.show()



    def show_predictions(self):
        """

        :return:
        """

        return None


if __name__ == '__main__':
    visu = Visualizer()
    visu.get_equal_error_rate()