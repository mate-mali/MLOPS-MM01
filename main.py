import argparse
from settings import Settings
from dotenv import load_dotenv
import os
import yaml



def export_envs(environment: str = "dev") -> None:
    if environment == "dev":
        load_dotenv(dotenv_path="config/.env.dev")
    elif environment == "prod":
        load_dotenv(dotenv_path="config/.env.prod")
    elif environment == "test":
        load_dotenv(dotenv_path="config/.env.test")
    else:
        raise ValueError(
            "Invalid environment. Must be one of 'dev', 'prod', or 'test'."
        )

def run_app(environment: str = "dev") -> dict:
    #adapt endpoint for testing purposes
    export_envs(environment)
    settings = Settings()
    y = yaml.safe_load(open(os.getenv("SECRETS_FILE")))
    
    return {
        "APP_NAME": settings.APP_NAME,
        "ENVIRONMENT": settings.ENVIRONMENT,
        "secrets": y
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load environment variables from specified.env file.")
    parser.add_argument("--environment", type=str, default="dev", help="The environment to load (dev, test, prod)")
    args = parser.parse_args()

    export_envs(args.environment) 
    
    settings = Settings()

    y = yaml.safe_load(open(os.getenv("SECRETS_FILE")))
    
    result = run_app(args.environment)
    print("APP_NAME: ", result["APP_NAME"])
    print("ENVIRONMENT: ", result["ENVIRONMENT"])
    print("Secrets: ", result["secrets"])

    
