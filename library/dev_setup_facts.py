#!/usr/bin/python

import subprocess

def main():
    module = AnsibleModule(
        argument_spec = dict(
        ),
        supports_check_mode = False,
    )

    
    facts = {}
    
    facts['dev_setup_facts_loaded'] = True
    
    # get the project root via git (though we should be in dev/)
    project_root = facts['dev_setup_project_root'] = subprocess.check_output(
        ['git', 'rev-parse', '--show-toplevel']
    ).rstrip()
    
    dev_dir = facts['dev_setup_dev_dir'] = os.path.join(project_root, 'dev')
    
    ruby_version_path = os.path.join(project_root, ".ruby-version")
    if os.path.exists(ruby_version_path):
        with open(ruby_version_path) as f:
            facts["dev_setup_ruby_version"] = f.read().rstrip()
    
    
    node_version_path = os.path.join(project_root, ".node-version")
    if os.path.exists(node_version_path):
        with open(node_version_path) as f:
            facts["dev_setup_node_version"] = f.read().rstrip()
    
    gemfile_path = os.path.join(project_root, 'Gemfile')
    facts["dev_setup_gemfile_exists"] = os.path.exists(gemfile_path)
    
    package_json_path = os.path.join(project_root, 'package.json')
    facts["dev_setup_package_json_exists"] = os.path.exists(package_json_path)
    
    module.exit_json(
        changed = False,
        ansible_facts = facts,
    )

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.known_hosts import *

if __name__ == '__main__':
    main()