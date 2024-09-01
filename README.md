# ZenML MLflow Basic Example

This repository demonstrates the integration of ZenML with MLflow for model management and deployment. ZenML is an open-source MLOps framework that simplifies the process of managing machine learning pipelines, while MLflow provides tools for tracking experiments, packaging models, and deploying them.

## Usage

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/abhirick23/zenml_mlflow_basic.git
    cd zenml_mlflow_basic
    ```

2. **Set Up a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Required Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Deployment Script:**

    Execute the following command to start the MLflow deployment server in blocking mode:

    ```bash
    python run_deployment.py --config deploy
    ```

5. **Verify the Service:**

    Check the console output for the URL and status of the MLflow prediction server. This server will be running in blocking mode, so the script will wait until the server is stopped.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
