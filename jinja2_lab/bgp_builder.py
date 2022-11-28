from jinja2 import Environment, FileSystemLoader
import yaml

with open('bgp_config.yaml') as f:
    bgp = yaml.safe_load(f.read())

for device in bgp:
    neighbors = bgp[device]['neighbors']
    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)
    template = env.get_template('bgp_template.j2')
    bgp_config = template.render(neighbors=neighbors,local_asn=bgp[device]['local_asn'])
    with open ('{device}_bgp_config.txt'.format(device=device), 'w') as f:
        f.write(bgp_config)
    