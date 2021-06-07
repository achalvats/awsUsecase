
import * as ec2 from '@aws-cdk/aws-ec2';
import * as s3 from '@aws-cdk/aws-s3';
import * as cdk from '@aws-cdk/core';

export class WorkshopCdkStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const bucketS3 = new s3.Bucket(this, 'MyFirstBucket');
    const Itype = new ec2.InstanceType("t2.micro")
    const ami= new ec2.LookupMachineImage({name:'ubuntu/images/hvm-ssd/ubuntu-xenial-16.04-amd64-server-20170307',
                    owners:['099720109477']
    })
    // in ec2.LookupMachineImage we use new keyword as we are intializing the methoed where as in below two we are not using new as we are calling them
    const amznLinux =  ec2.MachineImage.latestAmazonLinux({
      generation: ec2.AmazonLinuxGeneration.AMAZON_LINUX,
      edition: ec2.AmazonLinuxEdition.STANDARD,
      virtualization: ec2.AmazonLinuxVirt.HVM,
      storage: ec2.AmazonLinuxStorage.GENERAL_PURPOSE,
      cpuType: ec2.AmazonLinuxCpuType.X86_64,
    });
    const Ivpc = ec2.Vpc.fromLookup(this,"vpc",{isDefault: true})
    
    const ec2Instance = new ec2.Instance(this, "ec2Instance", {instanceType:Itype, machineImage: amznLinux, vpc: Ivpc}) 

  }
}
