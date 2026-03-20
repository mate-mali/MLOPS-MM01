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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load environment variables from specified.env file.")
    parser.add_argument("--environment", type=str, default="dev", help="The environment to load (dev, test, prod)")
    args = parser.parse_args()

    export_envs(args.environment) 
    
    settings = Settings()

    y = yaml.safe_load(open(os.getenv("SECRETS_FILE")))
    
    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("Secrets: ", y)
