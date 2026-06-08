"""I2I bottle connector — share patterns with the fleet"""
import json
import os
import time
import uuid

VESSEL_DIR = os.path.expanduser("~/.openclaw/workspace/i2i-vessel")
HARBOR = os.path.join(VESSEL_DIR, "harbor")

def send_pattern_bottle(agent_id: str, pattern: str, source: str = "rhythmica"):
    os.makedirs(HARBOR, exist_ok=True)
    bottle = {
        "id": f"{source}-{uuid.uuid4().hex[:8]}",
        "type": "DELIVERABLE",
        "source": source,
        "target": agent_id,
        "payload": {"pattern": pattern},
        "timestamp": int(time.time() * 1000)
    }
    path = os.path.join(HARBOR, f"{int(time.time()*1000)}-rhythm-pattern-{uuid.uuid4().hex[:6]}.json")
    with open(path, 'w') as f:
        json.dump(bottle, f)
    return path
