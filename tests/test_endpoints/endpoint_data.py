from datetime import date

from hapi_schema.utils.enums import (
    CommodityCategory,
    DisabledMarker,
    EventType,
    Gender,
    PopulationGroup,
    PopulationStatus,
    PriceFlag,
    PriceType,
    RiskClass,
    IPCPhase,
    IPCType,
)

from hdx_hapi.endpoints.util.util import AdminLevel

endpoint_data = {
    '/api/v1/metadata/admin1': {
        'query_parameters': {
            'id': 2,
            'location_ref': 1,
            'code': 'FoO-001',
            'name': 'Province 01',
            'location_code': 'FoO',
            'location_name': 'Foolandia',
            # 'reference_period_start_min': '2020-01-01T00:00:00',
            # 'reference_period_start_max': '2024-01-01T00:00:00',
        },
        'expected_fields': [
            'id',
            'location_ref',
            'code',
            'name',
            'from_cods',
            'location_code',
            'location_name',
            'reference_period_start',
            'reference_period_end',
        ],
    },
    '/api/v1/metadata/admin2': {
        'query_parameters': {
            'id': 4,
            'admin1_ref': 2,
            'code': 'FoO-001-A',
            'name': 'District A',
            'location_ref': 1,
            'admin1_code': 'FOo-001',
            'admin1_name': 'Province 01',
            'location_code': 'FOo',
            'location_name': 'Foolandia',
            # 'reference_period_start_min': '2020-01-01T00:00:00',
            # 'reference_period_start_max': '2024-01-01T00:00:00',
        },
        'expected_fields': [
            'id',
            'admin1_ref',
            'code',
            'name',
            'from_cods',
            'location_ref',
            'admin1_code',
            'admin1_name',
            'location_code',
            'location_name',
            'reference_period_start',
            'reference_period_end',
        ],
    },
    '/api/v1/metadata/data-availability': {
        'query_parameters': {
            'category': 'coordination-context',
            'subcategory': 'conflict-event',
            'location_code': 'FOO',
            'location_name': 'Foolandia',
            'admin1_code': 'FOO-001',
            'admin1_name': 'Province 01',
            'admin2_code': 'FOO-001-A',
            'admin2_name': 'District A',
            'update_date_min': date(2022, 6, 1),
            'update_date_max': date(2023, 6, 3),
        },
        'expected_fields': [
            'category',
            'subcategory',
            'location_code',
            'location_name',
            'admin1_code',
            'admin1_name',
            'admin2_code',
            'admin2_name',
            'hapi_updated_date',
        ],
    },
    '/api/v1/metadata/dataset': {
        'query_parameters': {
            'dataset_hdx_id': '90deb235-1bf5-4bae-b231-3393222c2d01',
            'dataset_hdx_title': 'Dataset #1',
            'hdx_provider_stub': 'pRoViDeR01',
            'hdx_provider_name': 'Provider #1',
        },
        'expected_fields': [
            'dataset_hdx_id',
            'dataset_hdx_stub',
            'dataset_hdx_title',
            'hdx_provider_stub',
            'hdx_provider_name',
            'hdx_link',  # computed field
            'hdx_api_link',  # computed field
            'provider_hdx_link',  # computed field
            'provider_hdx_api_link',  # computed field
        ],
    },
    '/api/v1/metadata/location': {
        'query_parameters': {
            'id': 1,
            'code': 'foo',
            'name': 'Foolandia',
            'has_hrp': True,
            'in_gho': True,
            # 'reference_period_start_min': '2020-01-01T00:00:00',
            # 'reference_period_start_max': '2024-01-01T00:00:00',
        },
        'expected_fields': [
            'id',
            'code',
            'name',
            'has_hrp',
            'in_gho',
            'from_cods',
            'reference_period_start',
            'reference_period_end',
        ],
    },
    '/api/v1/coordination-context/conflict-event': {
        'query_parameters': {
            'event_type': EventType.POLITICAL_VIOLENCE.value,
            'location_ref': 1,
            'location_code': 'foo',
            'location_name': 'Foolandia',
            'has_hrp': True,
            'in_gho': True,
            'admin1_ref': 2,
            'admin1_code': 'foo-001',
            'admin1_name': 'province',
            'provider_admin1_name': 'Provider admin1 name 4',
            'admin2_ref': 4,
            'admin2_code': 'foo-001-a',
            'admin2_name': 'district',
            'provider_admin2_name': 'Provider admin2 name 4',
        },
        'expected_fields': [
            'event_type',
            'events',
            'fatalities',
            'resource_hdx_id',
            'location_ref',
            'location_code',
            'location_name',
            'admin1_ref',
            'admin1_code',
            'admin1_name',
            'provider_admin1_name',
            'admin2_ref',
            'admin2_code',
            'admin2_name',
            'provider_admin2_name',
            'reference_period_start',
            'reference_period_end',
        ],
    },
    '/api/v1/coordination-context/funding': {
        'query_parameters': {
            'appeal_code': 'hfoo24',
            'appeal_type': 'hRp',
            'location_code': 'foo',
            'location_name': 'Foolandia',
            'has_hrp': True,
            'in_gho': True,
            # 'reference_period_start_min': '2020-01-01T00:00:00',
            # 'reference_period_start_max': '2024-01-01T00:00:00',
        },
        'expected_fields': [
            'resource_hdx_id',
            'appeal_code',
            'appeal_name',
            'appeal_type',
            'requirements_usd',
            'funding_usd',
            'funding_pct',
            'location_ref',
            'location_code',
            'location_name',
            'reference_period_start',
            'reference_period_end',
        ],
    },
    '/api/v1/coordination-context/operational-presence': {
        'query_parameters': {
            'org_acronym': 'oRG01',
            'org_name': 'Organisation 1',
            'sector_code': 'Shl',
            'sector_name': 'Emergency Shelter and NFI',
            'location_ref': 1,
            'location_code': 'foo',
            'location_name': 'Foolandia',
            'has_hrp': True,
            'in_gho': True,
            'admin1_ref': 2,
            'admin1_code': 'foo-001',
            'admin1_name': 'province',
            'provider_admin1_name': 'Provider admin1 name 2',
            'admin1_is_unspecified': False,
            'admin2_ref': 2,
            'admin2_code': 'foo-001-xxx',
            'admin2_name': 'Unspecified',
            'provider_admin2_name': 'Provider admin2 name 2',
            'admin2_is_unspecified': True,
            # 'reference_period_start_min': '2020-01-01T00:00:00',
            # 'reference_period_start_max': '2024-01-01T00:00:00',
        },
        'expected_fields': [
            'sector_code',
            'resource_hdx_id',
            'org_acronym',
            'org_name',
            'org_type_code',
            'org_type_description',
            'sector_name',
            'location_ref',
            'location_code',
            'location_name',
            'reference_period_start',
            'reference_period_end',
            'admin1_ref',
            'admin1_code',
            'admin1_name',
            'provider_admin1_name',
            'admin2_ref',
            'admin2_code',
            'admin2_name',
            'provider_admin2_name',
        ],
    },
    '/api/v1/metadata/org': {
        'query_parameters': {
            'acronym': 'Org01',
            'name': 'Organisation 1',
            'org_type_code': '433',
            'org_type_description': 'Dono',  # Donor
        },
        'expected_fields': ['acronym', 'name', 'org_type_code', 'org_type_description'],
    },
    '/api/v1/metadata/org-type': {
        'query_parameters': {
            'code': '431',
            'name': 'Academic / Research',
        },
        'expected_fields': ['code', 'description'],
    },
    '/api/v1/population-social/population': {
        'query_parameters': {
            'admin2_ref': 1,
            'gender': Gender.NONBINARY.value,
            'age_range': '10-14',
            'min_age': 10,
            'max_age': 14,
            'population_min': 0,
            'population_max': 10000000,
            #'reference_period_start_min': '2020-01-01T00:00:00',
            #'reference_period_end_max': '2024-01-01T00:00:00',
            'location_code': 'fOO',
            'location_name': 'Foolandia',
            'location_ref': 1,
            'has_hrp': True,
            'in_gho': True,
            'admin1_code': 'FOO-xxx',
            'admin1_name': 'Unspecified',
            'provider_admin1_name': 'Provider admin1 name 1',
            'admin1_is_unspecified': False,
            'admin2_code': 'FOO-xxx-XXX',
            'admin2_name': 'Unspecified',
            'provider_admin2_name': 'Provider admin2 name 1',
            'admin2_is_unspecified': True,
        },
        'expected_fields': [
            'resource_hdx_id',
            'admin2_ref',
            'gender',
            'age_range',
            'min_age',
            'max_age',
            'population',
            'reference_period_start',
            'reference_period_end',
            'location_ref',
            'location_code',
            'location_name',
            'admin1_ref',
            'admin1_code',
            'admin1_name',
            'provider_admin1_name',
            'admin2_code',
            'admin2_name',
            'provider_admin2_name',
        ],
    },
    '/api/v1/population-social/poverty-rate': {
        'query_parameters': {
            'provider_admin1_name': 'Province 01',
            'mpi_min': 0.01,
            'mpi_max': 0.9,
            # 'reference_period_start_min': '2020-01-01T00:00:00',
            # 'reference_period_end_max': '2024-01-01T00:00:00',
            'location_code': 'fOO',
            'location_name': 'Foolandia',
            'has_hrp': True,
            'in_gho': True,
        },
        'expected_fields': [
            'resource_hdx_id',
            'provider_admin1_name',
            'mpi',
            'headcount_ratio',
            'intensity_of_deprivation',
            'vulnerable_to_poverty',
            'in_severe_poverty',
            'reference_period_start',
            'reference_period_end',
            'location_code',
            'location_name',
            'location_ref',
        ],
    },
    '/api/v1/food/food-security': {
        'query_parameters': {
            'admin2_ref': 1,
            'ipc_phase': IPCPhase.PHASE_1.value,
            'ipc_type': IPCType.CURRENT.value,
            'location_ref': 1,
            'location_code': 'fOO',
            'location_name': 'Foolandia',
            'has_hrp': True,
            'in_gho': True,
            'admin1_code': 'FOO-xxx',
            'admin1_name': 'Unspecified',
            'provider_admin1_name': 'Provider admin1 name 1',
            # 'admin1_is_unspecified': True,
            'admin2_code': 'FOO-xxx-XXX',
            'admin2_name': 'Unspecified',
            'provider_admin2_name': 'Provider admin2 name 1',
            # 'admin2_is_unspecified': True,
            'admin_level': AdminLevel.ZERO.value,
            # 'reference_period_start': date(2023, 6, 1),
            # 'reference_period_end': date(2023, 6, 2),
        },
        'expected_fields': [
            'resource_hdx_id',
            'admin2_ref',
            'ipc_phase',
            'ipc_type',
            'population_in_phase',
            'population_fraction_in_phase',
            'reference_period_start',
            'reference_period_end',
            'location_code',
            'location_name',
            'admin1_code',
            'admin1_name',
            'provider_admin1_name',
            'location_ref',
            'admin2_code',
            'admin2_name',
            'provider_admin2_name',
            'admin1_ref',
        ],
    },
    '/api/v1/food/food-price': {
        'query_parameters': {
            'market_code': '002',
            'market_name': 'market',
            'commodity_code': '001',
            'commodity_name': 'commodity',
            'commodity_category': CommodityCategory.VEGETABLES_FRUITS.value,
            'price_flag': PriceFlag.AGGREGATE.value,
            'price_type': PriceType.WHOLESALE.value,
            'price_min': '200.1',
            'price_max': '200.3',
            'location_ref': 1,
            'location_code': 'fOO',
            'location_name': 'Foolandia',
            'has_hrp': True,
            'in_gho': True,
            'admin1_ref': 1,
            'admin1_code': 'FOO-xxx',
            'admin1_name': 'Unspecified',
            'provider_admin1_name': 'Provider admin1 name 1',
            'admin2_ref': 1,
            'admin2_code': 'FOO-xxx-XXX',
            'admin2_name': 'Unspecified',
            'provider_admin2_name': 'Provider admin2 name 1',
            'admin_level': AdminLevel.ZERO.value,
        },
        'expected_fields': [
            'resource_hdx_id',
            'market_code',
            'market_name',
            'commodity_code',
            'commodity_name',
            'commodity_category',
            'price_flag',
            'price_type',
            'price',
            'unit',
            'currency_code',
            'lat',
            'lon',
            'reference_period_start',
            'reference_period_end',
            'location_ref',
            'location_code',
            'location_name',
            'admin1_ref',
            'admin1_code',
            'admin1_name',
            'provider_admin1_name',
            'admin2_ref',
            'admin2_code',
            'admin2_name',
            'provider_admin2_name',
        ],
    },
    '/api/v1/coordination-context/national-risk': {
        'query_parameters': {
            'risk_class': RiskClass.HIGH.value,
            'global_rank_min': 5,
            'global_rank_max': 7,
            'overall_risk_min': 6,
            'overall_risk_max': 10,
            'hazard_exposure_risk_min': 6,
            'hazard_exposure_risk_max': 10,
            'vulnerability_risk_min': 5,
            'vulnerability_risk_max': 10,
            'coping_capacity_risk_min': 6.1,
            'coping_capacity_risk_max': 10.1,
            # 'reference_period_start_min': '2020-01-01T00:00:00',
            # 'reference_period_start_max': '2024-01-11T00:00:00',
            # 'reference_period_end_min': '2023-01-01T00:00:00',
            # 'reference_period_end_max': '2025-01-01T00:00:00',
            'location_code': 'fOO',
            'location_name': 'Foolandia',
            'has_hrp': True,
            'in_gho': True,
        },
        'expected_fields': [
            'risk_class',
            'global_rank',
            'overall_risk',
            'hazard_exposure_risk',
            'vulnerability_risk',
            'coping_capacity_risk',
            'meta_missing_indicators_pct',
            'meta_avg_recentness_years',
            'reference_period_start',
            'reference_period_end',
            'resource_hdx_id',
            'location_code',
            'location_name',
            'location_ref',
        ],
    },
    '/api/v1/affected-people/humanitarian-needs': {
        'query_parameters': {
            'admin2_ref': 2,
            'gender': Gender.ALL.value,
            'age_range': 'ALL',
            'disabled_marker': DisabledMarker.YES.value,
            'sector_code': 'EDU',
            'population_group': PopulationGroup.REFUGEES.value,
            'population_status': PopulationStatus.AFFECTED.value,
            # 'reference_period_start_min': '2020-01-01T00:00:00',
            # 'reference_period_start_max': '2026-01-01T00:00:00',
            'sector_name': 'Education',
            'location_code': 'foo',
            'location_name': 'Foolandia',
            'location_ref': 1,
            'has_hrp': True,
            'in_gho': True,
            'admin1_code': 'FOO-001',
            'admin1_name': 'Province 01',
            'provider_admin1_name': 'Provider admin1 name 2',
            'admin2_code': 'foo-001-XXX',
            'admin2_name': 'Unspecified',
            'provider_admin2_name': 'Provider admin2 name 2',
            'admin1_ref': 2,
        },
        'expected_fields': [
            'resource_hdx_id',
            'admin2_ref',
            'gender',
            'age_range',
            'min_age',
            'max_age',
            'disabled_marker',
            'sector_code',
            'population_group',
            'population_status',
            'population',
            'reference_period_start',
            'reference_period_end',
            'sector_name',
            'location_code',
            'location_name',
            'location_ref',
            'admin1_code',
            'admin1_name',
            'provider_admin1_name',
            'admin2_code',
            'admin2_name',
            'provider_admin2_name',
            'admin1_ref',
        ],
    },
    '/api/v1/affected-people/refugees': {
        'query_parameters': {
            'population_group': PopulationGroup.REFUGEES.value,
            'gender': Gender.ALL.value,
            'age_range': 'ALL',
            # 'reference_period_start_min': '2020-01-01T00:00:00',
            # 'reference_period_start_max': '2026-01-01T00:00:00',
            'origin_location_code': 'foo',
            'origin_location_name': 'Foolandia',
            'origin_has_hrp': True,
            'origin_in_gho': True,
            'asylum_location_code': 'foo',
            'asylum_location_name': 'Foolandia',
            'asylum_has_hrp': True,
            'asylum_in_gho': True,
        },
        'expected_fields': [
            'resource_hdx_id',
            'origin_location_ref',
            'asylum_location_ref',
            'population_group',
            'gender',
            'age_range',
            'min_age',
            'max_age',
            'population',
            'reference_period_start',
            'reference_period_end',
            'origin_location_name',
            'origin_location_code',
            'asylum_location_name',
            'asylum_location_code',
        ],
    },
    '/api/v1/affected-people/returnees': {
        'query_parameters': {
            'population_group': PopulationGroup.REFUGEES.value,
            'gender': Gender.ALL.value,
            'age_range': 'ALL',
            # 'reference_period_start_min': '2020-01-01T00:00:00',
            # 'reference_period_start_max': '2026-01-01T00:00:00',
            'origin_location_code': 'foo',
            'origin_location_name': 'Foolandia',
            'origin_has_hrp': True,
            'origin_in_gho': True,
            'asylum_location_code': 'foo',
            'asylum_location_name': 'Foolandia',
            'asylum_has_hrp': True,
            'asylum_in_gho': True,
        },
        'expected_fields': [
            'resource_hdx_id',
            'origin_location_ref',
            'asylum_location_ref',
            'population_group',
            'gender',
            'age_range',
            'min_age',
            'max_age',
            'population',
            'reference_period_start',
            'reference_period_end',
            'origin_location_name',
            'origin_location_code',
            'asylum_location_name',
            'asylum_location_code',
        ],
    },
    # ('17acb541-9431-409a-80a8-50eda7e8ebab', 1, 'BA', 1, 50, '2023-01-01 00:00:00', NULL)
    '/api/v1/affected-people/idps': {
        'query_parameters': {
            'admin2_ref': 1,
            'provider_admin1_name': 'Provider admin1 name 1',
            'provider_admin2_name': 'Provider admin2 name 2',
            'location_ref': 1,
            'location_code': 'fOO',
            'location_name': 'Foolandia',
            'has_hrp': True,
            'in_gho': True,
            'admin1_ref': 1,
            'admin1_code': 'FOO-xxx',
            'admin1_name': 'Unspecified',
            'admin2_code': 'FOO-xxx-XXX',
            'admin2_name': 'Unspecified',
        },
        'expected_fields': [
            'resource_hdx_id',
            'admin2_ref',
            'provider_admin1_name',
            'provider_admin2_name',
            'reporting_round',
            'assessment_type',
            'operation',
            'population',
            'reference_period_start',
            'reference_period_end',
            'location_code',
            'location_name',
            'location_ref',
            'admin1_code',
            'admin1_name',
            'admin2_code',
            'admin2_name',
            'admin1_ref',
        ],
    },
    '/api/v1/metadata/resource': {
        'query_parameters': {
            'resource_hdx_id': '17acb541-9431-409a-80a8-50eda7e8ebab',
            'name': 'resource-01.csv',
            'format': 'csv',
            'update_date_min': date(2023, 6, 1),
            'update_date_max': date(2023, 6, 3),
            'is_hxl': True,
            'hapi_updated_date': date(2023, 6, 2),
            'dataset_hdx_stub': 'dataset01',
            'dataset_hdx_title': 'Dataset #1',
            'dataset_hdx_provider_stub': 'pRoViDeR01',
            'dataset_hdx_provider_name': 'Provider #1',
        },
        'expected_fields': [
            'resource_hdx_id',
            'dataset_hdx_id',
            'name',
            'format',
            'update_date',
            'is_hxl',
            'download_url',
            'hapi_updated_date',
            'dataset_hdx_stub',
            'dataset_hdx_title',
            'dataset_hdx_provider_stub',
            'dataset_hdx_provider_name',
            'hdx_link',  # computed field
            'hdx_api_link',  # computed field
            'dataset_hdx_link',  # computed field
            'dataset_hdx_api_link',  # computed field
            'provider_hdx_link',  # computed field
            'provider_hdx_api_link',  # computed field
        ],
    },
    '/api/v1/metadata/sector': {
        'query_parameters': {
            'code': 'Pro',
            'name': 'Protection',  # Protection
        },
        'expected_fields': ['code', 'name'],
    },
    '/api/v1/metadata/currency': {
        'query_parameters': {
            'code': 'usD',
        },
        'expected_fields': ['code', 'name'],
    },
    '/api/v1/metadata/wfp-commodity': {
        'query_parameters': {
            'code': '001',
            'name': 'commodity',
            'category': CommodityCategory.VEGETABLES_FRUITS.value,
        },
        'expected_fields': ['code', 'name', 'category'],
    },
    '/api/v1/metadata/wfp-market': {
        'query_parameters': {
            'code': '001',
            'name': 'Market #1',
            'location_ref': 1,
            'location_code': 'foo',
            'location_name': 'Foolandia',
            'has_hrp': True,
            'in_gho': True,
            'admin1_ref': 2,
            'admin1_code': 'foo-001',
            'admin1_name': 'province',
            'provider_admin1_name': 'Provider admin1 name 4',
            'admin2_ref': 4,
            'admin2_code': 'foo-001-a',
            'admin2_name': 'district',
            'provider_admin2_name': 'Provider admin2 name 4',
        },
        'expected_fields': [
            'code',
            'name',
            'lat',
            'lon',
            'location_ref',
            'location_code',
            'location_name',
            'admin1_ref',
            'admin1_code',
            'admin1_name',
            'provider_admin1_name',
            'admin2_ref',
            'admin2_code',
            'admin2_name',
            'provider_admin2_name',
        ],
    },
    '/api/encode_app_identifier': {
        'query_parameters': {
            'application': 'web_application_1',
            'email': 'info@example.com',
        },
        'expected_fields': ['encoded_app_identifier'],
    },
}
