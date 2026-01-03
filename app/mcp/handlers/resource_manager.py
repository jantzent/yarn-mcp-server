from typing import Any, Dict

from app.clients.resource_manager import ResourceManagerClient
from app.models import AppIdParams, AppListParams, NodeAppsParams, QueueInfoParams


class ResourceManagerHandler:
    def __init__(self, client: ResourceManagerClient) -> None:
        self._client = client

    async def cluster_info(self) -> Dict[str, Any]:
        return await self._client.cluster_info()

    async def scheduler(self) -> Dict[str, Any]:
        return await self._client.scheduler()

    async def nodes(self, state: str | None = None) -> Dict[str, Any]:
        return await self._client.nodes(state=state)

    async def node_apps(self, params: NodeAppsParams) -> Dict[str, Any]:
        return await self._client.node_apps(params.node_id, state=params.state)

    async def apps(self, params: AppListParams) -> Dict[str, Any]:
        return await self._client.apps(params=params.model_dump(exclude_none=True))

    async def app_details(self, params: AppIdParams) -> Dict[str, Any]:
        return await self._client.app(params.app_id)

    async def app_attempts(self, params: AppIdParams) -> Dict[str, Any]:
        return await self._client.app_attempts(params.app_id)

    async def app_containers(self, params: AppIdParams, attempt_id: str) -> Dict[str, Any]:
        return await self._client.app_containers(params.app_id, attempt_id)

    async def queue_info(self, params: QueueInfoParams) -> Dict[str, Any]:
        return await self._client.queue_info(params.queue_name)
