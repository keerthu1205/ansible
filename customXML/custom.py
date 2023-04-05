from ansible.module_utils.basic import AnsibleModule
import xml.etree.ElementTree as ET

def run_module():
    module_args = dict(
        xml_file=dict(type='str', required=True),
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

    xml_file = module.params['xml_file']

    if module.check_mode:
        module.exit_json(**result)

    tree = ET.parse(xml_file)
    root = tree.getroot()

    food_price_list = []

    for item in root.iter('food'):
        food_name = item.find('name').text
        price = item.find('price').text
        food_price_list.append({"name": food_name, "price": price})

    result['food_price_list'] = food_price_list
    result['changed'] = True

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
