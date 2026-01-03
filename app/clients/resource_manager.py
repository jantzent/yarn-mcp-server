from typing import Any, Dict, Optional

from app.clients.base import BaseClient


class ResourceManagerClient(BaseClient):
    async def cluster_info(self) -> Dict[str, Any]:
        return await self.get("/ws/v1/cluster/info")

    async def scheduler(self) -> Dict[str, Any]:
        return await self.get("/ws/v1/cluster/scheduler")

    async def nodes(self, *, state: Optional[str] = None) -> Dict[str, Any]:
        params = {"state": state} if state else None
        return await self.get("/ws/v1/cluster/nodes", params=params)

    async def node_apps(self, node_id: str, *, state: Optional[str] = None) -> Dict[str, Any]:
        params = {"state": state} if state else None
        return await self.get(f"/ws/v1/cluster/nodes/{node_id}/apps", params=params)

    async def apps(self, *, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return await self.get("/ws/v1/cluster/apps", params=params)

    async def app(self, app_id: str) -> Dict[str, Any]:
        return await self.get(f"/ws/v1/cluster/apps/{app_id}")

    async def app_attempts(self, app_id: str) -> Dict[str, Any]:
        return await self.get(f"/ws/v1/cluster/apps/{app_id}/appattempts")

    async def app_containers(self, app_id: str, attempt_id: str) -> Dict[str, Any]:
        return await self.get(
            f"/ws/v1/cluster/apps/{app_id}/appattempts/{attempt_id}/containers"
        )

    async def queue_info(self, queue_name: str) -> Dict[str, Any]:
        return await self.get(f"/ws/v1/cluster/scheduler/queues/{queue_name}")
