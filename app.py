#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_demo.cdk_demo_stack import CdkDemoStack


app = cdk.App()
CdkDemoStack(app, "CdkDemoStack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    #env=cdk.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

# https://docs.aws.amazon.com/cdk/v2/guide/tagging.html
# tags = [["SDLC", "Prod"],
#         ["CostCenter","0123456789"]]

# for tag in tags:
#     key = tag[0]
#     value = tag[1]
#     cdk.Tags.of(app).add(key, value)

app.synth()
