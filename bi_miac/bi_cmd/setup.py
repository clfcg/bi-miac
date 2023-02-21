from pathlib import Path

from bi_miac.configs.base_conf import CONF_DIR
from bi_miac.bi_cmd.rend_temlates import render_template
from bi_miac.bi_cmd.handlers import *


if not Path(CONF_DIR, "header.yaml").is_file():
    Path(CONF_DIR, "header.yaml").touch()
if not Path(CONF_DIR, "reports.yaml").is_file():
    Path(CONF_DIR, "reports.yaml").touch()


header_commands = {
    "show": show_commands,
    "add-full": add_full_header,
    "back": "back",
}


def action(com, dict, default="COMMAND NOT FOUND"):
        if com in dict:
            return dict[com]
        else:
            return default


print(render_template("greetings.j2"))

kw = ""
while kw.lower() != "exit":
    kw = input("bi: ")
    if kw.lower() == "header":
        while kw.lower() != "back":
            kw = input("bi/header: ")
            out = action(kw, header_commands)
            out()