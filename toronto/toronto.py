import boto3
import click

session = boto3.Session(profile_name='toronto')
ec2 = session.resource('ec2')

def filter_instances(project):
    instances = []

    if project:
        filters = [{'PName': 'tag:Project', 'Values':[project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()   
    return instances

@click.group()
def instances():
    """Commands for instances"""


@instances.command('list')
@click.option('--project', default=None,
    help = "only instances for project (tag Project:<name>) ")
def ListAllInstances(project):
    "This is doc string : Lists all instances"
    instances = filter_instances(project)

    if project:
        filters = [{'PName': 'tag:Project', 'Values':[project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()        

    for i in ec2.instances.all():
        tags = { t['Key']: t['Value'] for t in i.tags or [] }
        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name,
            tags.get('Project', '<no project>')
        )))
    
@instances.command('stop')
@click.option('--project', default=None,
    help='Only instances for project')
def stop_instances(project):
    "Stop EC2 instanes"

    instances = filter_instances(project)

    for i in instances:
        print("Stopping {0}...".format(i.id))
        i.stop()

@instances.command('start')
@click.option('--project', default=None,
    help='Only instances for project')
def start_instances(project):
    "Start EC2 instanes"

    instances = filter_instances(project)

    for i in instances:
        print("Starting {0}...".format(i.id))
        i.start()


    
        
if __name__ == '__main__':
    instances()
    
