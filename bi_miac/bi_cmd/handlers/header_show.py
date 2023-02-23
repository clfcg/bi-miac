from strictyaml import load, as_document

from bi_miac.configs.base_conf import CONF_HEADER


def show_header_sruct():
    yaml = load(CONF_HEADER.read_text()).data
    yaml = as_document(yaml)
    print(yaml.as_yaml())