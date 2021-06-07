#!/usr/bin/env node
import * as cdk from '@aws-cdk/core';
import { WorkshopCdkStack } from '../lib/workshop_cdk-stack';
const envUSA = { account: '928410310665', region: 'us-east-1' };

const app = new cdk.App();
new WorkshopCdkStack(app, 'WorkshopCdkStack',{env: envUSA});
