from fastapi import APIRouter, Header, Query, Body, Request, Response
from typing import Dict, List, Optional
import logging
from pydantic import BaseModel

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/dummy",
    tags=["dummy"],
    responses={404: {"description": "Not found"}},
)

# Pydantic models for request/response
class DummyRequest(BaseModel):
    name: str
    value: int
    tags: List[str] = []

class DummyResponse(BaseModel):
    message: str
    request_info: Dict
    status: str = "success"

async def log_request_info(request: Request, body: Optional[Dict] = None):
    """Helper function to log request information"""
    headers = dict(request.headers)
    query_params = dict(request.query_params)
    
    logger.info(
        f"\n--- Request Info ---\n"
        f"Method: {request.method}\n"
        f"URL: {request.url}\n"
        f"Headers: {headers}\n"
        f"Query Params: {query_params}\n"
        f"Body: {body}\n"
        f"------------------"
    )
    
    return {
        "headers": headers,
        "query_params": query_params,
        "body": body
    }

@router.get(
    "",
    response_model=DummyResponse,
    summary="Dummy GET endpoint",
    description="Example of GET with query parameters"
)
async def dummy_get(
    request: Request,
    name: str = Query(..., description="Name parameter"),
    age: Optional[int] = Query(None, description="Age parameter"),
    x_custom_header: Optional[str] = Header(None, description="Custom header")
) -> DummyResponse:
    """
    Dummy GET endpoint that demonstrates query parameters and headers.
    """
    request_info = await log_request_info(request)
    return DummyResponse(
        message=f"GET request for {name}",
        request_info=request_info
    )

@router.post(
    "",
    response_model=DummyResponse,
    summary="Dummy POST endpoint",
    description="Example of POST with JSON body"
)
async def dummy_post(
    request: Request,
    data: DummyRequest = Body(..., description="Request body"),
) -> DummyResponse:
    """
    Dummy POST endpoint that demonstrates body parsing.
    """
    request_info = await log_request_info(request, data.dict())
    return DummyResponse(
        message=f"Created resource for {data.name}",
        request_info=request_info
    )

@router.put(
    "/{item_id}",
    response_model=DummyResponse,
    summary="Dummy PUT endpoint",
    description="Example of PUT with path parameter and body"
)
async def dummy_put(
    request: Request,
    item_id: int,
    data: DummyRequest = Body(..., description="Request body"),
) -> DummyResponse:
    """
    Dummy PUT endpoint that demonstrates path parameters and body parsing.
    """
    request_info = await log_request_info(request, data.dict())
    return DummyResponse(
        message=f"Updated item {item_id} with name {data.name}",
        request_info=request_info
    )

@router.patch(
    "/{item_id}",
    response_model=DummyResponse,
    summary="Dummy PATCH endpoint",
    description="Example of PATCH with partial updates"
)
async def dummy_patch(
    request: Request,
    item_id: int,
    data: Dict = Body(..., description="Partial request body"),
) -> DummyResponse:
    """
    Dummy PATCH endpoint that demonstrates partial updates.
    """
    request_info = await log_request_info(request, data)
    return DummyResponse(
        message=f"Partially updated item {item_id}",
        request_info=request_info
    )

@router.delete(
    "/{item_id}",
    response_model=DummyResponse,
    summary="Dummy DELETE endpoint",
    description="Example of DELETE with path parameter"
)
async def dummy_delete(
    request: Request,
    item_id: int,
    force: bool = Query(False, description="Force deletion"),
) -> DummyResponse:
    """
    Dummy DELETE endpoint that demonstrates path parameters.
    """
    request_info = await log_request_info(request)
    return DummyResponse(
        message=f"Deleted item {item_id} (force={force})",
        request_info=request_info
    )

@router.options(
    "",
    response_model=DummyResponse,
    summary="Dummy OPTIONS endpoint",
    description="Example of OPTIONS request"
)
async def dummy_options(
    request: Request,
    response: Response,
) -> DummyResponse:
    """
    Dummy OPTIONS endpoint that demonstrates OPTIONS handling.
    """
    response.headers["Allow"] = "GET, POST, PUT, PATCH, DELETE, OPTIONS"
    request_info = await log_request_info(request)
    return DummyResponse(
        message="Supported methods",
        request_info=request_info
    ) 