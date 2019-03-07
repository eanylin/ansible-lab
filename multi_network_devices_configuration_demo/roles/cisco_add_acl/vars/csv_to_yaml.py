import yaml
import csv
import sys

csvfile = open('acl_requirements.csv', 'r')
data = csv.reader(csvfile)
result = []

for row_index, row in enumerate(data):
  if row_index == 0:
    headings = []
    for heading_index, heading in enumerate(row):
      fixed_heading = heading.lower().replace(" ", "_").replace("-", "")
      headings.append(fixed_heading)
  else:
    content = {}
    for cell_index, cell in enumerate(row):
      content[headings[cell_index]] = cell
    result.append(content)

result_dict = {'routers': result}

sys.stdout = open('/tmp/output.yaml','wt')
print yaml.dump(result_dict, default_flow_style=False)

sys.stdout.close()
