from typing import Any, Dict, List


def manifest() -> Dict[str, List[Dict[str, Any]]]:
    return {
        "core": [
            {
                "name": "rm.cluster_info",
                "description": "Get ResourceManager cluster info",
                "params": {},
            },
            {
                "name": "rm.scheduler",
                "description": "Get scheduler info",
                "params": {},
            },
            {
                "name": "rm.nodes",
                "description": "List cluster nodes",
                "params": {"state": "Optional node state filter"},
            },
            {
                "name": "rm.apps",
                "description": "List applications",
                "params": {
                    "state": "Filter by app state",
                    "queue": "Filter by queue",
                    "user": "Filter by user",
                    "started_time_begin": "Epoch millis start",
                    "started_time_end": "Epoch millis end",
                },
            },
            {
                "name": "rm.app_details",
                "description": "Get application details",
                "params": {"app_id": "YARN application id"},
            },
            {
                "name": "rm.app_attempts",
                "description": "List attempts for an application",
                "params": {"app_id": "YARN application id"},
            },
            {
                "name": "rm.app_containers",
                "description": "List containers for an app attempt",
                "params": {"app_id": "YARN application id", "attempt_id": "Attempt id"},
            },
            {
                "name": "rm.queue_info",
                "description": "Get queue information",
                "params": {"queue_name": "Queue name"},
            },
        ],
        "optional": [
            {
                "name": "rm.node_apps",
                "description": "List apps on a node",
                "params": {"node_id": "Node id", "state": "Optional state"},
            },
            {
                "name": "ahs.apps",
                "description": "List historical applications",
                "params": {
                    "state": "Filter by app state",
                    "queue": "Filter by queue",
                    "user": "Filter by user",
                    "started_time_begin": "Epoch millis start",
                    "started_time_end": "Epoch millis end",
                },
            },
            {
                "name": "ahs.app_details",
                "description": "Get historical application details",
                "params": {"app_id": "YARN application id"},
            },
            {
                "name": "ahs.app_attempts",
                "description": "List historical attempts",
                "params": {"app_id": "YARN application id"},
            },
            {
                "name": "ahs.app_containers",
                "description": "List historical containers",
                "params": {"app_id": "YARN application id", "attempt_id": "Attempt id"},
            },
        ],
    }
