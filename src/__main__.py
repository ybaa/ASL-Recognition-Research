from src.imagesOperations.ImagesCollectionLoader import ConcateHorizontalAndVertical, DevideImagesForTrainingAndTesting
from src.machineLearning.LearningManager import LearningManager

if __name__ == '__main__':

    learning_Manager = LearningManager(testing=False, c_in=1, gamma_in='auto', decision='ovo')
    gaussianParams = {
        'doGaussian': True,
        'sigma': 1,
        'output': None,
        'mode': 'nearest',
        'cval': 0,
        'multichannel': None,
        'preserve_range': False,
        'truncate': 4.0
    }
    laplaceParams = {
        'doLaplace': True,
        'ksize': 4,
        'mask': None
    }
    images = ConcateHorizontalAndVertical("images/sma", gaussianParams, laplaceParams)
    
    trainingSet, testingSet = DevideImagesForTrainingAndTesting(images, 0.7)

    # __Testing_learning_parameters__(trainingSet, testingSet)

    learning_Manager.__Learning__(trainingSet)

    learning_Manager.__Tests__(testingSet)
