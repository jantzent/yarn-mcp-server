from typing import Any, Callable, Dict

from fastmcp import FastMCP

from app.auth import build_auth
from app.clients.history_server import HistoryServerClient
from app.clients.resource_manager import ResourceManagerClient
from app.config import AppConfig
from app.mcp.handlers import HistoryServerHandler, ResourceManagerHandler


ToolHandler = Callable[..., Any]


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: Dict[str, ToolHandler] = {}

    def register(self, name: str, handler: ToolHandler) -> None:
        self._tools[name] = handler

    def tools(self) -> Dict[str, ToolHandler]:
        return dict(self._tools)


def build_registry(config: AppConfig) -> ToolRegistry:
    registry = ToolRegistry()
    auth = build_auth(config)

    rm_client = ResourceManagerClient(
        config.rm_url,
        timeout=config.timeout,
        tls_verify=config.tls_verify,
        retries=config.retries,
        auth=auth,
    )
    rm_handler = ResourceManagerHandler(rm_client)

    registry.register("rm.cluster_info", rm_handler.cluster_info)
    registry.register("rm.scheduler", rm_handler.scheduler)
    registry.register("rm.nodes", rm_handler.nodes)
    registry.register("rm.node_apps", rm_handler.node_apps)
    registry.register("rm.apps", rm_handler.apps)
    registry.register("rm.app_details", rm_handler.app_details)
    registry.register("rm.app_attempts", rm_handler.app_attempts)
    registry.register("rm.app_containers", rm_handler.app_containers)
    registry.register("rm.queue_info", rm_handler.queue_info)

    if config.ahs_url:
        ahs_client = HistoryServerClient(
            config.ahs_url,
            timeout=config.timeout,
            tls_verify=config.tls_verify,
            retries=config.retries,
            auth=auth,
        )
        ahs_handler = HistoryServerHandler(ahs_client)

        registry.register("ahs.apps", ahs_handler.apps)
        registry.register("ahs.app_details", ahs_handler.app_details)
        registry.register("ahs.app_attempts", ahs_handler.app_attempts)
        registry.register("ahs.app_containers", ahs_handler.app_containers)

    return registry


def register_tools(mcp: FastMCP, registry: ToolRegistry) -> None:
    for name, handler in registry.tools().items():
        mcp.tool(name=name)(handler)
