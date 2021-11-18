from SublimeLinter.lint import Linter, STREAM_STDERR


class JSONNetLint(Linter):
    cmd = 'jsonnet-lint ${file_on_disk}'
    tempfile_suffix = '-'
    name = 'jsonnet-lint'
    regex = r'(?P<filename>.*):(?P<line>[1-9][0-9]*):(?P<col>[1-9][0-9]*)-(?P<end_col>[1-9][0-9]*) (?P<message>.*)'
    error_stream = STREAM_STDERR
    multiline = False
    defaults = {
        'selector': 'source.jsonnet'
    }
