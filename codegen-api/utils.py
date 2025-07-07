import json
import os

def generate_main_tf(user_input):
    cloud = user_input["cloud"]
    project = user_input["project_name"]
    services = user_input["services"]

    # Load mapping.json
    with open("mapping.json") as f:
        mapping = json.load(f)

    lines = []
    lines.append(f'provider "{cloud}" {{\n  region = var.aws_region\n}}\n')

    for svc in services:
        svc_type = svc["type"]
        params = svc["params"]
        module_source = mapping[svc_type][cloud]

        block = f'module "{svc_type}" {{'
        block += f'\n  source = "{module_source}"'
        block += '\n  tags = {\n    "Project" = "' + project + '"\n  }'

        for k, v in params.items():
            if isinstance(v, list):
                block += f'\n  {k} = {json.dumps(v)}'
            else:
                block += f'\n  {k} = "{v}"'
        block += '\n}\n'
        lines.append(block)

    os.makedirs("generated", exist_ok=True)
    with open("generated/main.tf", "w") as f:
        f.write("\n".join(lines))

    return "\n".join(lines)
