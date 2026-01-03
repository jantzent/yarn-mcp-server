from typing import Any, Dict, Optional

import httpx

from app.models import MCPError


class BaseClient:
    def __init__(
        self,
        base_url: str,
        *,
        timeout: float,
        tls_verify: bool,
        retries: int,
        auth: Optional[httpx.Auth] = None,
    ) -> None:
        self._client = httpx.AsyncClient(
            base_url=base_url,
            timeout=httpx.Timeout(timeout),
            verify=tls_verify,
            transport=httpx.AsyncHTTPTransport(retries=retries),
            auth=auth,
        )

    async def close(self) -> None:
        await self._client.aclose()

    async def get(self, path: str, *, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        try:
            response = await self._client.get(path, params=params)
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            raise MCPError(
                message="Upstream request failed",
                status_code=exc.response.status_code,
                context={
                    "url": str(exc.request.url),
                    "response": exc.response.text,
                },
            ) from exc
        except httpx.RequestError as exc:
            raise MCPError(
                message="Upstream request error",
                context={"url": str(exc.request.url), "error": str(exc)},
            ) from exc
        return response.json()
