import json

def generate_main_tf(user_input):
    cloud = user_input["cloud"]
    project = user_input["project_name"]
    services = user_input["services"]

    # Load mapping.json
    with open("mapping.json") as f:
        mapping = json.load(f)

    lines = []

    # Add provider block
    lines.append('provider "{}" {{\n  region = var.aws_region\n}}\n'.format(cloud))

    # Loop over services
    for svc in services:
        svc_type = svc["type"]
        params = svc["params"]

        module_source = mapping[svc_type][cloud]

        module_block = f'module "{svc_type}" {{'
        module_block += f'\n  source = "{module_source}"'

        # Add project tag as default
        module_block += '\n  tags = {{\n    "Project" = "' + project + '"\n  }}'

        for key, value in params.items():
            if isinstance(value, list):
                module_block += f'\n  {key} = {json.dumps(value)}'
            else:
                module_block += f'\n  {key} = "{value}"'

        module_block += '\n}\n'

        lines.append(module_block)

    # Write to file
    with open("generated/main.tf", "w") as f:
        f.write("\n".join(lines))

    return {"status": "success", "details": "main.tf generated"}
