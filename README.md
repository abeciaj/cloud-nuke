# Cloud-Nuke

## Install

### Download from releases page

1. Download the latest binary for your OS on the [releases page](https://github.com/gruntwork-io/cloud-nuke/releases).
2. Move the binary to a folder on your `PATH`. E.g.: `mv cloud-nuke_darwin_amd64 /usr/local/bin/cloud-nuke`.
3. Add execute permissions to the binary. E.g.: `chmod u+x /usr/local/bin/cloud-nuke`.
4. Test it installed correctly: `cloud-nuke --help`.

### Install via package manager

Note that package managers are third party. The third party cloud-nuke packages may not be updated with the latest
version, but are often close. Please check your version against the latest available on
the [releases page](https://github.com/gruntwork-io/cloud-nuke/releases). If you want the latest version, the
recommended installation option is
to [download from the releases page](https://github.com/gruntwork-io/cloud-nuke/releases).

- **macOS:** You can install cloud-nuke using [Homebrew](https://brew.sh/): `brew install cloud-nuke`.

- **Linux:** Most Linux users can use [Homebrew](https://docs.brew.sh/Homebrew-on-Linux): `brew install cloud-nuke`.

- **Windows:** You can install cloud-nuke using [winget](https://learn.microsoft.com/en-us/windows/package-manager/winget/): `winget install cloud-nuke`

## Usage

Simply running `cloud-nuke aws` will start the process of cleaning up your cloud account. You'll be shown a list of
resources that'll be deleted as well as a prompt to confirm before any deletion actually takes place.

In AWS, to delete only the default resources, run `cloud-nuke defaults-aws`. This will remove the default VPCs in each
region, and will also revoke the ingress and egress rules associated with the default security group in each VPC. Note
that the default security group itself is unable to be deleted. Visit the [official git repository](https://github.com/gruntwork-io/cloud-nuke) for more info.


## Requirements

1. ECR
2. Lambda Function with `AdministratorAccess` permission
3. Docker
   
## Deployment
1. Build and Push the Docker Image
```bash
docker build -t cloud-nuke-lambda .
docker tag cloud-nuke-lambda:latest <your-account-id>.dkr.ecr.<region>.amazonaws.com/cloud-nuke-lambda:latest
docker push <your-account-id>.dkr.ecr.<region>.amazonaws.com/cloud-nuke-lambda:latest
```

2. Create a Lambda Function
 * Use the Docker image as the Lambda runtime.
 * Set environment variables for the region, etc.
3. Test the Function: Invoke the Lambda with a payload
```bash
{
  "region": "us-east-1",
  "resource_type": "ec2"
}
```