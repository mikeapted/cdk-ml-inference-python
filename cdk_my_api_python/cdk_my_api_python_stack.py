from aws_cdk import (
    aws_lambda as _lambda,
    aws_apigatewayv2 as apigv2,
    aws_apigatewayv2_integrations as apigv2int,
    core,
)
import os

class CdkMyApiPythonStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_api_function = _lambda.DockerImageFunction(self, 'MyApiFunction',
            code = _lambda.DockerImageCode.from_image_asset('../src'),
            timeout = core.duration.seconds(30),
            memory_size = 2048
        )

        my_default_integration = apigv2int.LambdaProxyIntegration(
            handler = my_api_function
        )

        my_http_api = apigv2.HttpApi(self, 'MyApi',
            default_integration = my_default_integration
        )

        core.CfnOutput(self, 'MyApiUrl',
            value = my_http_api.api_endpoint
        )
        
        core.CfnOutput(self, 'MyApiFnLogGroup',
            value = my_api_function.log_group.log_group_name
        )
