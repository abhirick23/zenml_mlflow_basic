from zenml import pipeline
from steps.data_ingestion import ingest_df
from steps.clean_data import clean_df
from steps.model_train import train_model
from steps.evaluation import evaluate_model



@pipeline()
def training_pipeline(data_path: str):
    df = ingest_df(data_path)
    X_train,X_test,y_train,y_test = clean_df(df)
    model = train_model(X_train,X_test,y_train,y_test)
    r2_score,rmse = evaluate_model(model,X_test,y_test)