import os
import subprocess
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Starting cloud-nuke execution...")
    try:
        region = os.getenv("AWS_REGION", "us-east-1")
        command = [
            "cloud-nuke",
            "aws",
            "--region", region,
            "--resource-type", event.get("resource_type", "s3"),
            "--force"
        ]
        logger.info(f"Executing command: {' '.join(command)}")
        result = subprocess.run(command, capture_output=True, text=True)
        logger.info(f"Command output: {result.stdout}")
        if result.returncode == 0:
            return {"statusCode": 200, "body": "Successfully nuked resources"}
        else:
            logger.error(f"Error during execution: {result.stderr}")
            return {"statusCode": 500, "body": "Error nuking resources"}
    except Exception as e:
        logger.exception("Exception occurred during execution")
        return {"statusCode": 500, "body": f"Exception: {str(e)}"}
