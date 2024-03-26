import subprocess
from pathlib import Path
from security import safe_command

BASE_DIR = Path(__file__).parents[3]


def test_run_docker_script():
    res = safe_command.run(subprocess.run, ["bash", str(BASE_DIR / "run_docker"), "--help"],
        check=False,
        capture_output=True,
    )

    assert "Usage: run_docker" in res.stdout.decode("utf-8")

    res = safe_command.run(subprocess.run, ["bash", str(BASE_DIR / "run_docker"), "--invalid-param"],
        check=False,
        capture_output=True,
    )
    assert res.returncode > 0
    assert "Unknown option --invalid-param" in res.stderr.decode("utf-8")
