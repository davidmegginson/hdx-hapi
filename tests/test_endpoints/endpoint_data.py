from datetime import date

from hapi_schema.utils.enums import RiskClass, IPCPhase, IPCType

endpoint_data = {
    '/api/v1/metadata/admin1': {
        'query_parameters': {
            'code': 'FoO-001',
            'name': 'Province 01',
            'location_code': 'FoO',
            'location_name': 'Foolandia',
            'reference_period_start_min': '2020-01-01T00:00:00',
            'reference_period_start_max': '2024-01-01T00:00:00',
        },
        'expected_fields': [
            'code',
            'name',
            'location_code',
            'location_name',
            'reference_period_start',
            'reference_period_end',
        ],
    },
    '/api/v1/metadata/admin2': {
        'query_parameters': {
            'code': 'FoO-001-A',
            'name': 'District A',
            'admin1_code': 'FOo-001',
            'admin1_name': 'Province 01',
            'location_code': 'FOo',
            'location_name': 'Foolandia',
            'reference_period_start_min': '2020-01-01T00:00:00',
            'reference_period_start_max': '2024-01-01T00:00:00',
        },
        'expected_fields': [
            'code',
            'name',
            'admin1_code',
            'admin1_name',
            'location_code',
            'location_name',
            'reference_period_start',
            'reference_period_end',
        ],
    },
    '/api/v1/metadata/dataset': {
        'query_parameters': {
            'hdx_id': '90deb235-1bf5-4bae-b231-3393222c2d01',
            'title': 'Dataset #1',
            'hdx_provider_stub': 'pRoViDeR01',
            'hdx_provider_name': 'Provider #1',
        },
        'expected_fields': [
            'hdx_id',
            'hdx_stub',
            'title',
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
            'code': 'foo',
            'name': 'Foolandia',
            'reference_period_start_min': '2020-01-01T00:00:00',
            'reference_period_start_max': '2024-01-01T00:00:00',
        },
        'expected_fields': [
            'code',
            'name',
            'reference_period_start',
            'reference_period_end',
        ],
    },
    '/api/v1/coordination-context/conflict-event': {
        'query_parameters': {
            'event_type': 'political_violence',
            'location_ref': 1,
            'location_code': 'foo',
            'location_name': 'Foolandia',
            'admin1_ref': 2,
            'admin1_code': 'foo-001',
            'admin1_name': 'province',
            'admin2_ref': 4,
            'admin2_code': 'foo-001-a',
            'admin2_name': 'district',
            'reference_period_start_min': '2024-01-01T00:00:00',
            'reference_period_start_max': '2024-01-02T00:00:00',
            'reference_period_end_min': '2024-01-30T00:00:00',
            'reference_period_end_max': '2024-02-01T00:00:00',
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
            'admin2_ref',
            'admin2_code',
            'admin2_name',
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
            'reference_period_start_min': '2020-01-01T00:00:00',
            'reference_period_start_max': '2024-01-01T00:00:00',
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
            'admin1_ref': 2,
            'admin1_code': 'foo-001',
            'admin1_name': 'province',
            'admin1_is_unspecified': False,
            'admin2_ref': 2,
            'admin2_code': 'foo-001-xxx',
            'admin2_name': 'Unspecified',
            'admin2_is_unspecified': True,
            'reference_period_start_min': '2020-01-01T00:00:00',
            'reference_period_start_max': '2024-01-01T00:00:00',
        },
        'expected_fields': [
            'sector_code',
            'resource_hdx_id',
            'org_acronym',
            'org_name',
            'org_type_code',
            'sector_name',
            'location_ref',
            'location_code',
            'location_name',
            'reference_period_start',
            'reference_period_end',
            'admin1_ref',
            'admin1_code',
            'admin1_name',
            'admin2_ref',
            'admin2_code',
            'admin2_name',
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
    '/api/v1/metadata/org_type': {
        'query_parameters': {
            'code': '431',
            'name': 'Academic / Research',
        },
        'expected_fields': ['code', 'description'],
    },
    '/api/v1/population-social/population': {
        'query_parameters': {
            'admin2_ref': 1,
            'gender': 'x',
            'age_range': '10-14',
            'min_age': 10,
            'max_age': 14,
            'population': 1000000,
            'reference_period_start': date(2023, 6, 1),
            'reference_period_end': date(2023, 6, 2),
            'location_code': 'fOO',
            'location_name': 'Foolandia',
            'admin1_code': 'FOO-xxx',
            'admin1_is_unspecified': False,
            'admin2_code': 'FOO-xxx-XXX',
            'admin2_name': 'Unspecified',
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
            'admin2_code',
            'admin2_name',
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
            'admin1_code': 'FOO-xxx',
            'admin1_is_unspecified': True,
            'admin2_code': 'FOO-xxx-XXX',
            'admin2_name': 'Unspecified',
            'admin2_is_unspecified': True,
            'reference_period_start': date(2023, 6, 1),
            'reference_period_end': date(2023, 6, 2),
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
            'location_ref',
            'admin2_code',
            'admin2_name',
            'admin1_ref',
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
            'reference_period_start_min': '2020-01-01T00:00:00',
            'reference_period_start_max': '2024-01-11T00:00:00',
            'reference_period_end_min': '2023-01-01T00:00:00',
            'reference_period_end_max': '2025-01-01T00:00:00',
            'location_code': 'fOO',
            'location_name': 'Foolandia',
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
        ],
    },
    '/api/v1/affected-people/humanitarian-needs': {
        'query_parameters': {
            'admin2_ref': 2,
            'gender': '*',
            'age_range': 'ALL',
            'min_age': 0,
            'max_age': 99,
            'disabled_marker': 'y',
            'sector_code': 'EDU',
            'population_group': 'REF',
            'population_status': 'AFF',
            'reference_period_start_min': '2020-01-01T00:00:00',
            'reference_period_start_max': '2026-01-01T00:00:00',
            'sector_name': 'Education',
            'location_code': 'foo',
            'location_name': 'Foolandia',
            'location_ref': 1,
            'admin1_code': 'FOO-001',
            'admin1_name': 'Province 01',
            'admin2_code': 'foo-001-XXX',
            'admin2_name': 'Unspecified',
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
            'admin2_code',
            'admin2_name',
            'admin1_ref',
        ],
    },
    '/api/v1/affected-people/refugees': {
        'query_parameters': {
            'population_group': 'REF',
            'gender': '*',
            'age_range': 'ALL',
            'min_age': 0,
            'max_age': 99,
            'reference_period_start_min': '2020-01-01T00:00:00',
            'reference_period_start_max': '2026-01-01T00:00:00',
            'origin_location_code': 'foo',
            'origin_location_name': 'Foolandia',
            'asylum_location_code': 'foo',
            'asylum_location_name': 'Foolandia',
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
            'origin_location_code',
            'origin_location_name',
            'asylum_location_code',
            'asylum_location_name',
        ],
    },
    '/api/v1/metadata/resource': {
        'query_parameters': {
            'hdx_id': '17acb541-9431-409a-80a8-50eda7e8ebab',
            'name': 'resource-01.csv',
            'format': 'csv',
            'update_date_min': date(2023, 6, 1),
            'update_date_max': date(2023, 6, 3),
            'is_hxl': True,
            'hapi_updated_date': date(2023, 6, 2),
            'dataset_hdx_stub': 'dataset01',
            'dataset_title': 'Dataset #1',
            'dataset_hdx_provider_stub': 'pRoViDeR01',
            'dataset_hdx_provider_name': 'Provider #1',
        },
        'expected_fields': [
            'hdx_id',
            'dataset_hdx_id',
            'name',
            'format',
            'update_date',
            'is_hxl',
            'download_url',
            'hapi_updated_date',
            'dataset_hdx_stub',
            'dataset_title',
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
    '/api/encode_app_identifier': {
        'query_parameters': {
            'application': 'web_application_1',
            'email': 'info@example.com',
        },
        'expected_fields': ['encoded_app_identifier'],
    },
}
