from pathlib import Path
import shutil

for rst_file in Path("source").rglob("*.rst"):
    if ".api." in rst_file.name:
        test = Path(rst_file).read_text()
        test = test.replace(":show-inheritance:", ":show-inheritance:\n    :imported-members:")
        test = test.replace(".api.", ".")
        test = test.replace("\\.api\\.", "\\.")
        with open(rst_file, "w") as f:
            f.write(test)