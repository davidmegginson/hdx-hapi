import logging

from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.db_operational_presence_view import OperationalPresenceView
from hdx_hapi.db.dao.util.util import apply_pagination


logger = logging.getLogger(__name__)

async def operational_presences_view_list(
    pagination_parameters: Dict,
    db: AsyncSession,
    org_ref: int = None,
    dataset_hdx_id: str = None,
    dataset_hdx_stub: str = None,
    sector_name: str = None,
    dataset_provider_code: str = None,
    org_acronym: str = None,
    org_name: str = None,
    location_code: str = None,
    location_name: str = None,
    admin1_code: str = None,
    admin1_name: str = None,
    admin2_code: str = None,
    admin2_name: str = None,
    admin1_is_unspecified: bool = None,
    admin2_is_unspecified: bool = None,

):

    logger.info(f'operational_presences_view_list called with params: org_ref={org_ref}, location_name={location_name}')

    query = select(OperationalPresenceView)
    if org_ref:
        query = query.where(OperationalPresenceView.org_ref == org_ref)
    if sector_name:
        query = query.where(OperationalPresenceView.sector_name == sector_name)
    if dataset_hdx_id:
        query = query.where(OperationalPresenceView.dataset_hdx_id == dataset_hdx_id)
    if dataset_hdx_stub:
        query = query.where(OperationalPresenceView.dataset_hdx_stub == dataset_hdx_stub)
    if dataset_provider_code:
        query = query.where(OperationalPresenceView.dataset_provider_code == dataset_provider_code)
    if org_acronym:
        query = query.where(OperationalPresenceView.org_acronym == org_acronym)
    if org_name:
        query = query.where(OperationalPresenceView.org_name == org_name)
    if location_code:
        query = query.where(OperationalPresenceView.location_code == location_code)
    if location_name:
        query = query.where(OperationalPresenceView.location_name == location_name)
    if admin1_code:
        query = query.where(OperationalPresenceView.admin1_code == admin1_code)
    if admin1_name:
        query = query.where(OperationalPresenceView.admin1_name == admin1_name)
    if admin2_code:
        query = query.where(OperationalPresenceView.admin2_code == admin2_code)
    if admin2_name:
        query = query.where(OperationalPresenceView.admin2_name == admin2_name)
    if admin1_is_unspecified is not None:
        query = query.where(OperationalPresenceView.admin1_is_unspecified == admin1_is_unspecified)
    if admin2_is_unspecified is not None:
        query = query.where(OperationalPresenceView.admin2_is_unspecified == admin2_is_unspecified)
    


    query = apply_pagination(query, pagination_parameters)

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    operational_presences = result.scalars().all()

    logger.info(f'Retrieved {len(operational_presences)} rows from the database')

    return operational_presences