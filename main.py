from datetime import datetime

import yaml
from git import Repo

FILE_TO_COMMIT_NAME: str = 'logger.yaml'


def update_file_to_commit():
    # read file contents to figure out how many times we commited.
    with open(FILE_TO_COMMIT_NAME, 'r') as file:
        YAML_FILE = {
            'UPDATE_TIMES': int(yaml.safe_load(file)['UPDATE_TIMES']) + 1,
            'LAST_UPDATE': datetime.now().strftime("%A %B %d %Y at %X%p")
        }
    # Write new contents to file to be commited.
    with open(FILE_TO_COMMIT_NAME, 'w') as file:
        yaml.dump(YAML_FILE, file, default_flow_style=False, sort_keys=True)
    return YAML_FILE


def commit_repository(YAML_FILE):
    repo = Repo('.')
    repo.index.add([FILE_TO_COMMIT_NAME])
    repo.index.commit(f'docs(logger): update `UPDATE_TIMES` to {YAML_FILE["UPDATE_TIMES"]}')
    # repo.index.commit(f'Updated {YAML_FILE["UPDATE_TIMES"]} times. Last update was on {YAML_FILE["LAST_UPDATE"]}.')
    origin = repo.remote('origin')
    origin.push()


if __name__ == '__main__':
    commit_repository(update_file_to_commit())
