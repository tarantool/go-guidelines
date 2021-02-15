import py
import pytest
import os
import subprocess
import tempfile


def get_tmpdir(request):
    tmpdir = py.path.local(tempfile.mkdtemp())
    request.addfinalizer(lambda: tmpdir.remove(rec=1))
    return str(tmpdir)


@pytest.fixture(scope='session')
def session_tmpdir(request):
    return get_tmpdir(request)


@pytest.fixture(scope="session")
def supercli_cmd(request, session_tmpdir):
    cli_base_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
    cli_path = os.path.join(session_tmpdir, 'supercli')

    cli_build_cmd = ['mage', '-v', 'build']

    build_env = os.environ.copy()
    build_env["CLIEXE"] = cli_path

    process = subprocess.run(cli_build_cmd, cwd=cli_base_path, env=build_env)
    assert process.returncode == 0, 'Failed to build supercli executable'

    return cli_path
