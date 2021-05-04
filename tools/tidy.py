from ruamel.yaml import YAML

yaml = YAML()

files = ('../remoteid/augmented.yaml', '../remoteid/canonical.yaml')
for fname in files:
    try:
        with open(fname, 'r') as f:
            api = yaml.load(f)
        with open(fname, 'w') as f:
            yaml.dump(api, f)
    except IOError:
        pass
