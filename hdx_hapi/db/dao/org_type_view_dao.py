import logging

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.db_org_type_view import OrgTypeView
from hdx_hapi.db.dao.util.util import apply_pagination
from hdx_hapi.endpoints.util.util import PaginationParams

logger = logging.getLogger(__name__)


async def org_types_view_list(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    code: str = None,
    description: str = None,
):
    logger.info(f'org_types_view_list called with params: code={code}, description={description}')

    query = select(OrgTypeView)
    if code:
        query = query.where(OrgTypeView.code == code)
    if description:
        query = query.where(OrgTypeView.description.icontains(description))

    query = apply_pagination(query, pagination_parameters)

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    org_types = result.scalars().all()

    logger.info(f'Retrieved {len(org_types)} rows from the database')

    return org_types
