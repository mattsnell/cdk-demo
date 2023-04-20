from aws_cdk import (
    Stack,
    Tags,
    aws_ec2 as ec2,
    aws_s3 as s3,
    aws_apigateway as apigw,
    aws_lambda as _lambda,
)
from constructs import Construct


class CdkDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Vpc creates a VPC that spans a whole region.

        # It will automatically divide the provided VPC CIDR range, and create
        # public and private subnets per Availability Zone. Network routing
        # for the public subnets will be configured to allow outbound access
        # directly via an Internet Gateway. Network routing for the private
        # subnets will be configured to allow outbound access via a set of
        # resilient NAT Gateways (one per AZ).

        # https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.Vpc.html

        vpc = ec2.Vpc(
            self,
            "cdk-vpc"
        )

        ######################################################################

        # That was too easy, I need to change the VPC CIDR, and I need
        # isolated subnets for my RDS databases

        # vpc_custom = ec2.Vpc(
        #     self,
        #     "cdk-vpc",
        #     ip_addresses=ec2.IpAddresses.cidr("172.20.0.0/16"),
        #     subnet_configuration=[
        #         ec2.SubnetConfiguration(
        #             name="public",
        #             subnet_type=ec2.SubnetType.PUBLIC
        #         ),
        #         ec2.SubnetConfiguration(
        #             name="private",
        #             subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
        #         ),
        #         ec2.SubnetConfiguration(
        #             name="isolated",
        #             subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
        #         )
        #     ]
        # )

        ######################################################################

        # S3 bucket with its own specific tag
        # https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html

        # bucket = s3.Bucket(
        #     self,
        #     "cdk-bucket",
        #     block_public_access=s3.BlockPublicAccess.BLOCK_ALL
        # )
        # Tags.of(bucket).add("Random", "Tag")

        ######################################################################

        # API Gateway REST API with AWS Lambda as the backend integration
        # https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway-readme.html
        # https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda-readme.html

        # Specifies Python 3.9 and function code from ./assets/lambda.py

        # lambda_function = _lambda.Function(
        #     self,
        #     "cdk-function",
        #     runtime=_lambda.Runtime.PYTHON_3_9,
        #     code=_lambda.Code.from_asset("assets"),
        #     handler="lambda.handler",
        # )

        # apigw.LambdaRestApi(
        #     self,
        #     "cdk-api",
        #     handler=lambda_function,
        # )
