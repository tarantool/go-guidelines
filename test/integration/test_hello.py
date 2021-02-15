from utils import run_command_and_get_output


def test_hello(supercli_cmd):
    rc, output = run_command_and_get_output([
        supercli_cmd, 'hello',
    ])
    assert rc == 0
    assert 'Hello, world' in output
