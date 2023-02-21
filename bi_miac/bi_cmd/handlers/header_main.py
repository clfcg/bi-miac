from bi_miac.bi_cmd.rend_temlates import render_template


def show_commands():
    template = render_template("header_commands.j2")
    print(template)