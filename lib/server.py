"""FastAPI service: fleet agent state → TidalCycles patterns"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pattern_engine import vector_to_pattern, vector_to_euclidean, vector_to_fast
import uvicorn

app = FastAPI(title="Rhythmica — Fleet Rhythm Officer")

class AgentState(BaseModel):
    agent_id: str
    ternary_vector: list[int]
    name: str = "agent"

@app.post("/pattern")
def generate_pattern(state: AgentState):
    try:
        pattern = vector_to_pattern(state.ternary_vector, state.name)
        euclidean = vector_to_euclidean(state.ternary_vector)
        speed = vector_to_fast(state.ternary_vector)
        return {
            "status": "ok",
            "agent": state.agent_id,
            "pattern": pattern,
            "euclidean": euclidean,
            "speed_mod": speed,
            "tidal_code": f'd1 $ {speed} $ {pattern}'
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok", "service": "rhythmica"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3002)
