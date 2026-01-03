from typing import Any, Dict, Optional

from app.clients.base import BaseClient


class HistoryServerClient(BaseClient):
    async def apps(self, *, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return await self.get("/ws/v1/applicationhistory/apps", params=params)

    async def app(self, app_id: str) -> Dict[str, Any]:
        return await self.get(f"/ws/v1/applicationhistory/apps/{app_id}")

    async def app_attempts(self, app_id: str) -> Dict[str, Any]:
        return await self.get(f"/ws/v1/applicationhistory/apps/{app_id}/appattempts")

    async def app_containers(self, app_id: str, attempt_id: str) -> Dict[str, Any]:
        return await self.get(
            f"/ws/v1/applicationhistory/apps/{app_id}/appattempts/{attempt_id}/containers"
        )
