#!/usr/bin/python

# Copyright: (c) 2021, Anthony Lin <anthony.jclin@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

import subprocess
import os
import os.path

from ansible.module_utils.basic import AnsibleModule

def run_module():
    # Define available arguments/parameters
    fields = dict(
        wfly_home=dict(type='str', required=True),
        components=dict(type='list', aliases=['subsystems'], required=False, elements='dict',
                        options=dict(
                            cluster_mode=dict(type='list', required=False, elements='dict', options=dict(
                                enabled=dict(type='bool', required=True),
                                file_directory=dict(
                                    type='str', required=False, default='/tmp')))))
    )

    module = AnsibleModule(argument_spec=fields)

    # Define variables
    data = module.params
    required_config_files = ['jgroup', 'modcluster', 'socket']
    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    # Execute jcliff command
    if data['components'][0]['cluster_mode'][0]['enabled']:
        for i in required_config_files:
            try:
                jcliff_extra_command_line = [data['wfly_home'] + "/bin/jboss-cli.sh",
                                             "--file=" +
                                             data['components'][0]['cluster_mode'][0]['file_directory'] +
                                             '/' + i + '.cli']

                result['message'] = subprocess.check_output(jcliff_extra_command_line,
                                                            stderr=subprocess.STDOUT,
                                                            shell=False,
                                                            env=os.environ)
                result['changed']=True

            except subprocess.CalledProcessError as jcliffexc:
                error = jcliffexc.output.decode()
                module.fail_json(msg=error, **result)
    else:
        result = dict(
            changed=False,
            message='As cluster_mode was set to false, cluster set up is not required'
        )

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
