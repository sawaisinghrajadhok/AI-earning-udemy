from ex4_end_to_end.src import utils


class PredictPipeline:

    def load_model_file(self):
        file_path = "/home/sawai/PycharmProjects/AI-learning/ex4_end_to_end/src/components/artifact/model.pkl"
        model = utils.load_pkl_file(file_path=file_path)
        return model

    def load_preprocessor_file(self):
        file_path = "/home/sawai/PycharmProjects/AI-learning/ex4_end_to_end/src/components/artifact/preprocessor.pkl"
        preprocessor = utils.load_pkl_file(file_path=file_path)
        return preprocessor
