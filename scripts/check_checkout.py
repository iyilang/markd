#!/usr/bin/env python3
"""Check byte-exact inputs with Git's Windows autocrlf setting."""

import pathlib
import subprocess
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
FILES = (
    "spec/fixtures/spec.txt",
    "spec/fixtures/smart_punct.txt",
    "spec/fixtures/regression.txt",
    "markd/h_t_m_l_entities/entities.iyi",
)


def git(*args: str) -> bytes:
    return subprocess.check_output(("git", *args), cwd=ROOT)


def main() -> None:
    attrs = git("check-attr", "text", "--", *FILES).decode("utf-8").splitlines()
    expected = [f"{path}: text: unset" for path in FILES]
    if attrs != expected:
        raise SystemExit(f"byte-exact paths must have -text: {attrs!r}")
    with tempfile.TemporaryDirectory(prefix="markd-checkout-") as directory:
        prefix = pathlib.Path(directory).as_posix() + "/"
        git("-c", "core.autocrlf=true", "checkout-index", f"--prefix={prefix}", "--", *FILES)
        for name in FILES:
            original = git("cat-file", "blob", f"HEAD:{name}")
            working = (ROOT / name).read_bytes()
            simulated = (pathlib.Path(directory) / name).read_bytes()
            if working != original or simulated != original:
                raise SystemExit(f"checkout changed bytes: {name}")
    print(f"{len(FILES)} byte-exact files match Git blobs with core.autocrlf=true")


if __name__ == "__main__":
    main()
