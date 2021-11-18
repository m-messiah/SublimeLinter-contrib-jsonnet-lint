from SublimeLinter.lint import Linter  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter


class JSONNetLint(Linter):
    cmd = 'jsonnet-lint ${file_on_disk}'
    name = 'jsonnet-lint'
    regex = r'(?P<filename>.*):(?P<line>[1-9][0-9]*):(?P<col>[1-9][0-9]*)-(?P<end_col>[1-9][0-9]*): (?P<message>.*)'
    multiline = False
    defaults = {
        'selector': 'source.jsonnet'
    }
