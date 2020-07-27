#!/usr/bin/env python3

from aws_cdk import core

from cdkworkshop.cdkworkshop_stack import CdkworkshopStack

import configparser
config = configparser.ConfigParser()
config.read('config.ini')

app = core.App()
CdkworkshopStack(app, "cdkworkshop", env={'region': config['SETUP']['region']})

app.synth()
