# autoware.ai

Colcon Workspace for Autoware.AI

## Usage

```sh
cd ~
git clone https://github.com/kenji-miyake/autoware.ai.git
cd autoware.ai
mkdir -p src
vcs import src < autoware.ai.repos
python3 repos2workspace autoware.ai.repos # (Optional) Generate .code-workspace for VSCode
code repos.code-workspace
```
