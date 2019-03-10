#!/usr/bin/python

# Copyright: (c) 2019, Anthony Lin <anthony.jclin@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}


from ansible.module_utils.basic import AnsibleModule

import yaml
import csv
import sys

def csv_to_yaml(filename):
    csvfile = open(filename, 'r')
    data = csv.reader(csvfile)
    key_value_result = []

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
        key_value_result.append(content)

    return {'nodes': key_value_result}


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        name=dict(type='str', required=True)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # change is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        csv_file='',
        stdout=''
    )

    # The AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Initialize result_dict
    result_dict = {}

    # Convert csv file to YAML
    result_dict = csv_to_yaml(module.params.get('name'))

    # If the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        return result

    # Update result
    result['csv_file'] = module.params['name']
    result['yaml_output'] = result_dict

    # Check if csv file parsing is successful
    if result_dict:
        result['changed'] = True
    else:
        module.fail_json(msg='CSV Parsing Failed!', **result)

    # In the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
