import argparse
import yaml
import json
import sys
from pathlib import Path


def repos2workspace(repos_file, workspace_file):
    with open(repos_file, "r") as f:
        repos = yaml.load(f, Loader=yaml.SafeLoader)

    paths = [f"src/{path}" for path in repos["repositories"]]
    folders = [{"path": "."}]

    workspace = {
        "folders": folders,
        "settings": {
            "files.watcherExclude": {
                "**/.git/**": True,
                "**/log/**": True,
                "**/build/**": True,
                "**/install/**": True
            },
            "scm.alwaysShowProviders": True,
            "scm.alwaysShowActions": True,
            "git.alwaysSignOff": True,
            "git.ignoredRepositories": [str(repos_file.parent.absolute())],
            "git.scanRepositories": paths,
            "python.autoComplete.extraPaths": [
                "/opt/ros/melodic/lib/python2.7/dist-packages"
            ],
        }
    }

    with open(workspace_file, "w") as f:
        json.dump(workspace, f, indent=2, sort_keys=False)


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("repos_file", type=Path)
    parser.add_argument("--workspace-file", type=Path,
                        default=Path("./autoware.ai.code-workspace"))
    ns = parser.parse_args(args)

    repos2workspace(ns.repos_file, ns.workspace_file)


if __name__ == "__main__":
    main(sys.argv[1:])
