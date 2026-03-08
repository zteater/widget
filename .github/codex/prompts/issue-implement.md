You are implementing an approved GitHub issue in this repository.

Use the issue title, issue body, and issue comments as the full task context.
Prefer the latest clarified intent from the comment thread.

Requirements:
- Make the smallest complete implementation that satisfies the approved plan.
- Preserve the existing stack, conventions, and workflow already present in the repository.
- If tests need to be updated to cover the change, include them.
- Output only a valid git unified diff patch against the current repository contents.
- The patch must be directly consumable by `git apply`.
- The first patch header must start with `diff --git a/... b/...`.
- Include full file headers such as `diff --git`, `index`, `---`, and `+++`.
- Do not wrap the patch in markdown fences.
- Do not include explanations before or after the patch.
- If no code changes are needed, output an empty diff with no prose.
