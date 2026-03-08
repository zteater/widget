You are updating an existing pull request in this repository based on human review feedback.

Use the issue title and body for the linked issue if available, the pull request title and body, the pull request comments, the pull request review comments, and the pull request reviews together as the full conversation context.
Prefer the latest clarified intent from the review thread.
Use the provided repository context as the source of truth for file names and current contents.

Requirements:
- Make the smallest complete implementation that addresses the feedback.
- Preserve the existing stack, conventions, and workflow already present in the repository.
- If tests need to be updated to cover the change, include them.
- Only modify files that already exist unless creating a new file is clearly necessary.
- Do not invent files, commands, or workflows that are not present in the provided repository context.
- Return only JSON. Do not wrap it in markdown fences. Do not include any prose before or after it.

Return exactly this shape:
{
  "edits": [
    {
      "path": "relative/path/from/repo/root",
      "action": "write",
      "content": "full final file contents"
    }
  ]
}

Rules for the JSON response:
- `edits` must be an array.
- Use `action: "write"` for both updates and new files.
- Each `content` value must contain the full final file contents for that path, not a diff.
- Omit unchanged files.
- If no code changes are needed, return `{"edits":[]}`.
