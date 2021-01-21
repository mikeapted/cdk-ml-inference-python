#!/usr/bin/env python3

from aws_cdk import core

from cdk_my_api_python.cdk_my_api_python_stack import CdkMyApiPythonStack


app = core.App()
CdkMyApiPythonStack(app, "cdk-my-api-python")

app.synth()
