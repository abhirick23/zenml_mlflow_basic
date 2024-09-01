from pipelines.training_pipeline import training_pipeline

from zenml.client import Client

if __name__ == "__main__":
    
    print(Client().active_stack.experiment_tracker.get_tracking_uri())
    
    training_pipeline(data_path="C:\Created\Learn\MLops_again_cause_me_dumb\Customer_data\data\olist_customers_dataset.csv")
    
    