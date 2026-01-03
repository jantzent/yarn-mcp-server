import os
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class AppConfig:
    rm_url: str
    ahs_url: Optional[str]
    auth_mode: str
    kerberos_service: str
    tls_verify: bool
    timeout: float
    retries: int = 2


true_values = {"1", "true", "yes", "on"}


def load_config() -> AppConfig:
    rm_url = os.getenv("YARN_RM_URL", "").strip()
    if not rm_url:
        raise ValueError("YARN_RM_URL is required")
    ahs_url = os.getenv("YARN_AHS_URL", "").strip() or None
    auth_mode = os.getenv("YARN_AUTH_MODE", "none").strip()
    kerberos_service = os.getenv("YARN_KERBEROS_SERVICE", "HTTP").strip()
    tls_verify = os.getenv("YARN_TLS_VERIFY", "true").strip().lower() in true_values
    timeout = float(os.getenv("YARN_TIMEOUT", "10"))
    return AppConfig(
        rm_url=rm_url,
        ahs_url=ahs_url,
        auth_mode=auth_mode,
        kerberos_service=kerberos_service,
        tls_verify=tls_verify,
        timeout=timeout,
    )
