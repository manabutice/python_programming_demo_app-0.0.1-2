"""Utils to display to be returned to the user on the console."""
import os
import string
import termcolor


def get_template_dir_path():
    """Return the path of the template's directory."""
    template_dir_path = None
    try:
        import settings
        if settings.TEMPLATE_PATH:
            template_dir_path = settings.TEMPLATE_PATH
    except ImportError:
        pass

    if not template_dir_path:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        template_dir_path = os.path.join(base_dir, 'templates')

    return template_dir_path


class NoTemplateError(Exception):
    """No Template Error"""


def find_template(temp_file):
    """Find the template file in the given location."""
    template_dir_path = get_template_dir_path()
    temp_file_path = os.path.join(template_dir_path, temp_file)
    if not os.path.exists(temp_file_path):
        raise NoTemplateError(f'Could not find {temp_file}')
    return temp_file_path


def get_template(template_file_path, color=None):
    """Read the template and return a string.Template with optional color."""
    template_path = find_template(template_file_path)
    with open(template_path, 'r', encoding='utf-8') as f:
        contents = f.read().rstrip(os.linesep)

    # テンプレートに装飾を追加（枠線）
    decorated = (
        "=" * 60 + os.linesep +
        contents + os.linesep +
        "=" * 60 + os.linesep
    )

    # 色を付ける
    if color:
        decorated = termcolor.colored(decorated, color)

    return string.Template(decorated)
