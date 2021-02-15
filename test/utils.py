import subprocess


def run_command_and_get_output(cmd, cwd=None, env=None):
    process = subprocess.Popen(
        cmd,
        env=env,
        cwd=cwd,
        stderr=subprocess.STDOUT,
        stdout=subprocess.PIPE
    )

    stdout, _ = process.communicate()
    stdout = stdout.decode('utf-8')

    # This print is here to make running tests with -s flag more verbose
    print(stdout)

    return process.returncode, stdout
