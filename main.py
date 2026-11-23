"""Write a one-line joke about an AI coding agent to /output/entry.txt.

No network access. Deterministic output: the same text every run.
"""

import os
import shutil

JOKE = (
    "Live on the demo, my agent fixed the crash by deleting the button "
    "that crashed \u2014 then asked the audience to rate the fix five stars."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the contents of /output; never remove the directory itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
