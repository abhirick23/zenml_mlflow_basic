from zenml.steps import BaseParameters

class ModelNmeConfig(BaseParameters):
    model_name: str = "LinearRegression"