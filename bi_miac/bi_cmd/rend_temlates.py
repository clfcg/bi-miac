import jinja2

from bi_miac.configs.base_conf import TEMPLATES_DIR


def render_template(template_name: str, data: dict | None = None):
    if data is None:
        data = {}
    template = _get_template_env().get_template(template_name)
    render = template.render(**data).replace("\n", "")
    render = render.replace("<br>", "\n")
    return render


def _get_template_env():
    template_loader = jinja2.FileSystemLoader(searchpath=TEMPLATES_DIR)
    env = jinja2.Environment(loader=template_loader)
    return env