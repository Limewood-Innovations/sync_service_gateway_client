# coding: utf-8

"""
    sync-service-api-gateway

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sync_service_api_gateway.models.ih_notification_close_create import IHNotificationCloseCreate

class TestIHNotificationCloseCreate(unittest.TestCase):
    """IHNotificationCloseCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IHNotificationCloseCreate:
        """Test IHNotificationCloseCreate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IHNotificationCloseCreate`
        """
        model = IHNotificationCloseCreate()
        if include_optional:
            return IHNotificationCloseCreate(
                jira_ticket_number = '',
                notif_number = 56
            )
        else:
            return IHNotificationCloseCreate(
                jira_ticket_number = '',
                notif_number = 56,
        )
        """

    def testIHNotificationCloseCreate(self):
        """Test IHNotificationCloseCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
