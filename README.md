This repo is a quick demo for [release-please](https://github.com/googleapis/release-please) working with [Poetry](https://python-poetry.org/) and [GitHub Actions](https://github.com/features/actions).
  * Any commit or merged PR automatically creates or updates a PR like #4.
  * The PR updates [CHANGELOG.md](CHANGELOG.md) with a list of all the commits based on [convential commits spec](https://www.conventionalcommits.org/).
  * The PR bumps the version in [pyproject.toml](pyproject.toml).
    * If all the commits are fixes, you get a patch version bump.
    * If there are new features, you get a minor version bump.
    * If there are breaknig changes, you get a major version bump.
  * More actions are triggered when the PR merges:
    * A new tag is created for the version.
    * A new GitHub [release](https://github.com/kichik/poetry-release-please-example/releases/tag/v0.1.3) is created with the changelog.
    * Our custom publishing code [executes](https://github.com/kichik/poetry-release-please-example/runs/5635748968?check_suite_focus=true).
    * "Publishing" code: https://github.com/kichik/poetry-release-please-example/blob/7225e4e3d96cda0b5c3540fedf067129cb9698b2/.github/workflows/release-please.yml#L15-L26
