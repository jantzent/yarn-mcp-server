from fastapi import FastAPI
from fastmcp import FastMCP

from app.config import AppConfig, load_config
from app.mcp.manifest import manifest
from app.mcp.registry import ToolRegistry, build_registry, register_tools

mcp = FastMCP("YARN MCP Server")
app = mcp.app


@app.on_event("startup")
async def startup() -> None:
    config = load_config()
    app.state.config = config
    app.state.registry = build_registry(config)
    register_tools(mcp, app.state.registry)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/mcp/manifest")
async def mcp_manifest() -> dict:
    return manifest()


@app.get("/mcp/tools")
async def mcp_tools() -> dict[str, list[str]]:
    registry: ToolRegistry = app.state.registry
    return {"tools": sorted(registry.tools().keys())}


def create_app(config: AppConfig) -> FastAPI:
    mcp_instance = FastMCP("YARN MCP Server")
    app_instance = mcp_instance.app
    app_instance.state.config = config
    app_instance.state.registry = build_registry(config)
    register_tools(mcp_instance, app_instance.state.registry)
    app_instance.include_router(app.router)
    return app_instance
