## update to standalone

module "cloud_nuke_lambda" {
  source = "terraform-aws-modules/lambda/aws"

  function_name = "aws-cloud-nuke-lambda"
  description   = "My awesome lambda function"

  create_package = false

  image_uri    = "920373027066.dkr.ecr.us-east-2.amazonaws.com/cloud-lambda:cloud-nuke-lambda-v2"
  package_type = "Image"

	timeout = 300
}

# Admin role
resource "aws_iam_role_policy_attachment" "lambda_admin_policy" {
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
  role       = "aws-cloud-nuke-lambda"
	depends_on = [ module.cloud_nuke_lambda ]
}