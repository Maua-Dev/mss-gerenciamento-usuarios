import json
import os


class ProjConfig:
    PROJ_ROOT_ABS_PATH = os.path.dirname(os.path.abspath(__file__))


    @staticmethod
    def getDeployment():
        return ProjConfig.fromJSON(os.path.join(ProjConfig.PROJ_ROOT_ABS_PATH, 'files', 'deployment.json'))

    @staticmethod
    def getFastapi():
        return ProjConfig.fromJSON(os.path.join(ProjConfig.PROJ_ROOT_ABS_PATH, 'files', 'fastapi.json'))

    @staticmethod
    def fromJSON(path):
        with open(path) as file:
            return json.load(file)
