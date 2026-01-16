from pydantic import BaseModel
class WorkflowRequest(BaseModel):
    client_request:str