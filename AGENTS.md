# AGENTS.md

`widget` is a small FastAPI service for widget CRUD.

## Repo Rules

- Use `make` targets as the primary workflow entrypoints
- Use `uv` for dependency management and package execution
- Do not add another task runner or dependency manager unless explicitly requested
- Keep the app lightweight and simple unless the task requires more infrastructure
- Keep tests runnable via `make test`
- Keep build validation runnable via `make build`
