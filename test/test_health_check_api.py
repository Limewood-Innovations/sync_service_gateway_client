# coding: utf-8

"""
    sync-service-api-gateway

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sync_service_api_gateway.api.health_check_api import HealthCheckApi


class TestHealthCheckApi(unittest.TestCase):
    """HealthCheckApi unit test stubs"""

    def setUp(self) -> None:
        self.api = HealthCheckApi()

    def tearDown(self) -> None:
        pass

    def test_health_check_pong(self) -> None:
        """Test case for health_check_pong

        Pong
        """
        pass


if __name__ == '__main__':
    unittest.main()
