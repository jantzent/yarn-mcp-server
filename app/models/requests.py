from typing import Optional

from pydantic import BaseModel, Field


class AppListParams(BaseModel):
    state: Optional[str] = Field(default=None, description="Filter by app state")
    queue: Optional[str] = Field(default=None, description="Filter by queue")
    user: Optional[str] = Field(default=None, description="Filter by user")
    started_time_begin: Optional[int] = Field(
        default=None, description="Epoch millis for start time begin"
    )
    started_time_end: Optional[int] = Field(
        default=None, description="Epoch millis for start time end"
    )


class NodeAppsParams(BaseModel):
    node_id: str = Field(description="Node ID or hostname")
    state: Optional[str] = Field(default=None, description="Filter by app state")


class QueueInfoParams(BaseModel):
    queue_name: str = Field(description="Queue name")


class AppIdParams(BaseModel):
    app_id: str = Field(description="YARN application id")


class AttemptIdParams(BaseModel):
    app_id: str = Field(description="YARN application id")
    attempt_id: str = Field(description="Attempt id")


class ContainerIdParams(BaseModel):
    app_id: str = Field(description="YARN application id")
    attempt_id: str = Field(description="Attempt id")
    container_id: str = Field(description="Container id")
