# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from thuin.urban.dataimport.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of thuin.urban.dataimport into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if thuin.urban.dataimport is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('thuin.urban.dataimport'))

    def test_uninstall(self):
        """Test if thuin.urban.dataimport is cleanly uninstalled."""
        self.installer.uninstallProducts(['thuin.urban.dataimport'])
        self.assertFalse(self.installer.isProductInstalled('thuin.urban.dataimport'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IThuinUrbanDataimportLayer is registered."""
        from thuin.urban.dataimport.interfaces import IThuinUrbanDataimportLayer
        from plone.browserlayer import utils
        self.failUnless(IThuinUrbanDataimportLayer in utils.registered_layers())
