from jinja2 import Environment, FileSystemLoader
import yaml

with open('bgp_config.yaml') as f:
    bgp = yaml.safe_load(f.read())

neighbors = bgp['R1']['neighbors']
file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)
template = env.get_template('bgp_template.j2')

output = template.render(neighbors=neighbors)

print(output)