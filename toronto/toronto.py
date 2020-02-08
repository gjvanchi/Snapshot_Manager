import boto3
import click

session = boto3.Session(profile_name='toronto')
ec2 = session.resource('ec2')

@click.command()
def ListAllInstances():
    "This is doc string : Lists all instances"
    for i in ec2.instances.all():
        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name
        )))
        
        
if __name__ == '__main__':
    ListAllInstances()    
    
