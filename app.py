from fastapi import FastAPI
from main_graph import build_graph
from models.request import WorkflowRequest

app= FastAPI()
workflow = build_graph()
@app.post("/run-workflow")
def run_workflow(request: WorkflowRequest):
    try:
        input_state={
            "client_request": request.client_request,
            "plan":[],
            "data":{},
            "validated": False,
            "approved": False,
            "result": "",
            "error": None

            
        }
        return workflow.invoke(input_state)
    

    except Exception as e:
        return {
            "error": "workflow execution failed",
            "details": str(e)
            
        }