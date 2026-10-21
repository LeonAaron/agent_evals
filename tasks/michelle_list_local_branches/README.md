# List local branches eval

The sandbox contains a Git repository with four local branches and two remote-tracking refs.
The agent saves the local branch names to a text file so the verifier can inspect the result.
The checks accept any order and reject missing names, duplicates, current-branch markers, or remote names.

`instruction.md` is the agent facing task. `environment/` builds its starting filesystem, `solution/solve.sh` is the reference solution, and `tests/` grades the result.
Tests and the solution are kept outside the starting image.

From the repository root, with Docker running:

```sh
uv run --locked harbor run --path tasks/michelle_list_local_branches --agent oracle --env docker
uv run --locked harbor run --path tasks/michelle_list_local_branches --agent nop --env docker
```

Expected rewards: oracle **1**, no-op baseline **0** (the output file is absent).
The verifier runs pytest and writes `/logs/verifier/reward.txt`.
