from typing import TypedDict, List, Optional
class WorkflowState(TypedDict):
    client_request: str
    plan : List[str]
    data : dict
    validated : bool
    approved : bool
    result : str
    error : Optional[str]
    