import os
import subprocess
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Starting cloud-nuke execution...")
    try:
        # Get region dynamically from the event or use a default
        region = event.get("region", os.environ.get("AWS_REGION", "us-east-1"))
        
        # Get resource type dynamically, default to "s3" if not provided
        resource_type = event.get("resource_type", "s3")
        command = [
            "cloud-nuke",
            "aws",
            "--region", region,
            "--resource-type", resource_type,
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
