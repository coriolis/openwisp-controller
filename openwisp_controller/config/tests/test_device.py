from django.core.exceptions import ValidationError
from django.test import TestCase

from openwisp_users.tests.utils import TestOrganizationMixin

from . import CreateConfigTemplateMixin
from ..models import Config, Device


class TestDevice(CreateConfigTemplateMixin, TestOrganizationMixin, TestCase):
    config_model = Config
    device_model = Device

    def test_device_with_org(self):
        org = self._create_org()
        device = self._create_device(organization=org)
        self.assertEqual(device.organization_id, org.pk)

    def test_device_without_org(self):
        try:
            self._create_device()
        except ValidationError as e:
            self.assertIn('organization', e.message_dict)
            self.assertIn('This field', e.message_dict['organization'][0])
        else:
            self.fail('ValidationError not raised')

    def test_change_org(self):
        org1 = self._create_org()
        device = self._create_device(organization=org1)
        config = self._create_config(device=device)
        self.assertEqual(config.organization_id, org1.pk)
        org2 = self._create_org(name='org2')
        device.organization = org2
        device.full_clean()
        device.save()
        self.assertEqual(device.config.organization_id, org2.pk)
