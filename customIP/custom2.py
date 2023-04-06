#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import re

def run_module():
    module_args = dict(
        ip_address=dict(type='str', required=True),
    )
    result = dict(
        changed=False,
        original_message='',
        message=''
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    ip_address = module.params['ip_address']
    valid_ip_address_regex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    valid_ip = False

    if module.check_mode:
        module.exit_json(**result)

    if re.search(valid_ip_address_regex, ip_address):
        valid_ip = True

    result['valid_ip'] = valid_ip
    result['changed'] = True

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main() 
