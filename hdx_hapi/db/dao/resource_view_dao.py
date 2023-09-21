from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.db_resource_view import ResourceView
from hdx_hapi.db.dao.util.util import apply_pagination

async def resources_view_list(
    pagination_parameters: Dict,
    db: AsyncSession,
    hdx_id: str = None,
    format: str = None,
    is_hxl: bool = None,
    dataset_title: str = None,
    dataset_provider_code: str = None,
    dataset_provider_name: str = None,
):

    query = select(ResourceView)
    if hdx_id:
        query = query.where(ResourceView.hdx_id == hdx_id)
    if format:
        query = query.where(ResourceView.format == format)
    if is_hxl is not None:
        query = query.where(ResourceView.is_hxl == is_hxl)
    if dataset_title:
        query = query.where(ResourceView.dataset_title == dataset_title)
    if dataset_provider_code:
        query = query.where(ResourceView.dataset_provider_code == dataset_provider_code)
    if dataset_provider_name:
        query = query.where(ResourceView.dataset_provider_name == dataset_provider_name)

    query = apply_pagination(query, pagination_parameters)

    result = await db.execute(query)
    resources = result.scalars().all()
    return resources