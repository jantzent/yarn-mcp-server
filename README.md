# yarn-mcp-server
An MCP (Model Context Protocol) server that provides a unified, LLM-friendly interface to Apache YARN, wrapping the ResourceManager and Application History Server REST APIs for cluster introspection, application monitoring, and job history access.

## Configuration
Set environment variables before starting the service:

- `YARN_RM_URL` (required): ResourceManager base URL, e.g. `https://rm.example.com:8088`.
- `YARN_AHS_URL` (optional): Application History Server base URL. If unset, AHS tools are disabled.
- `YARN_AUTH_MODE`: Auth mode (`none` or `kerberos`).
- `YARN_KERBEROS_SERVICE`: Kerberos service name for SPNEGO (default: `HTTP`).
- `YARN_TLS_VERIFY`: `true`/`false` to control TLS verification (default: `true`).
- `YARN_TIMEOUT`: Request timeout in seconds (default: `10`).

## Development with uv
This project uses `uv` for package management. Example setup:

```bash
uv venv
uv pip install -e .
```

## Docker
Build the image:

```bash
docker build -t yarn-mcp-server .
```

Run the server (pass configuration via env vars):

```bash
docker run --rm -p 8080:8080 \
  -e YARN_RM_URL=https://rm.example.com:8088 \
  -e YARN_AHS_URL=https://ahs.example.com:8188 \
  -e YARN_AUTH_MODE=kerberos \
  -e YARN_TLS_VERIFY=true \
  yarn-mcp-server
```

## FastMCP
The server uses the FastMCP framework to expose MCP tools. Dependencies are pinned to `fastmcp<3` to avoid upcoming breaking changes.

## MCP Tool Coverage
Core tools map to key ResourceManager APIs; optional tools include node-level details and AHS history endpoints. See `app/mcp/manifest.py` for the authoritative tool catalog and parameters.

## Testing Strategy (outline)
- Unit tests: handlers and client error mapping (simulate upstream HTTP errors and verify MCP error context).
- Integration tests: mock upstream YARN servers with `pytest-httpserver` or `httpx` mocks to validate request/response translation.
- Contract checks: validate manifest schemas and tool registration coverage versus handler definitions.
