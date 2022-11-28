import click
from IOSXE import *

ios = IOSXE()

@click.group()
def cli():
    pass

@cli.command()
def get_eigrp():
    click.echo('getting eigrp configuration')

    uri = 'Cisco-IOS-XE-native:native/router/router-eigrp/eigrp/classic-mode'
    response = ios.get_data(uri)
    print(response.text)

@cli.command()
def get_ospf():
    click.echo('getting interface ospf configuration')
    uri = 'Cisco-IOS-XE-native:native/interface/GigabitEthernet=1/ip/Cisco-IOS-XE-ospf:router-ospf/ospf/process-id'
    response = ios.get_data(uri)
    print(response.text)

@cli.command()
@click.option('--process_id', '-pid', default=1, type=click.Choice(['1', '2', '3']))
@click.option('--router_id', '-rid')
def configure_ospf(process_id,router_id):
    uri = 'Cisco-IOS-XE-native:native/router/Cisco-IOS-XE-ospf:router-ospf/ospf/process-id'
    payload = {
    "Cisco-IOS-XE-ospf:process-id": [
        {
        "id": process_id,
        "router-id": router_id
        }
        ]
    }


    response = ios.patch_data(uri=uri,payload=payload)
    print(response)

@cli.command()
@click.option('--interface', '-int')
@click.option('--process_id', '-pid')
@click.option('--area_id', '-aid')
def add_ospf_interface(interface,process_id,area_id):
    payload = {
                "Cisco-IOS-XE-ospf:process-id": [
                    {
                    "id": process_id,
                    "area": [
                        {
                        "area-id": area_id
                        }
                    ]
                    }
                ]
                }
    uri = 'Cisco-IOS-XE-native:native/interface/GigabitEthernet={int}/ip/Cisco-IOS-XE-ospf:router-ospf/ospf/process-id'.format(int=interface)
    response = ios.patch_data(uri=uri,payload=payload)

    print(response)


cli.add_command(get_eigrp)
cli.add_command(get_ospf)
cli.add_command(configure_ospf)
cli.add_command(add_ospf_interface)




if __name__ == '__main__':
    cli()