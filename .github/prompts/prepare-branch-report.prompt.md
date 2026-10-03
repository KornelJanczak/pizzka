---
name: prepare-branch-report
description: "Prepare a factual report for pushing the current FastAPI or full-stack work to a Git branch."
agent: agent
---

Prepare a push-readiness report for the current branch. Inspect the repository state before making any changes.

Include:

1. Current branch, likely base branch, and whether the working tree is clean.
2. A concise summary of changed files and user-visible or API behavior.
3. FastAPI endpoints, schemas, migrations, and configuration changes when present.
4. Required Python and Node versions, install/start commands, and environment variables.
5. Validation commands actually run, with pass/fail results and important failure details.
6. Checks for secrets, `.env` files, generated artifacts, and untracked files.
7. A short list of remaining blockers before pushing.
8. A suggested branch-push sequence, but do not commit, push, reset, or discard changes unless explicitly requested.

Use repository documentation and command output as evidence. Mark unknown values as `Unknown` and never invent a PR, test result, branch base, endpoint, or environment variable. Keep the final report concise and suitable for sharing in a pull request or team update.
