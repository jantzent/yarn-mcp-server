from __future__ import annotations

from typing import Optional

import httpx

from app.config import AppConfig


def build_auth(config: AppConfig) -> Optional[httpx.Auth]:
    mode = config.auth_mode.strip().lower()
    if mode in {"", "none"}:
        return None
    if mode == "kerberos":
        from httpx_gssapi import HTTPSPNEGOAuth

        return HTTPSPNEGOAuth(service=config.kerberos_service)
    raise ValueError(f"Unsupported auth mode: {config.auth_mode}")
