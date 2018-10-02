# -*- coding: utf-8 -*-

from imio.urban.dataimport.browser.controlpanel import ImporterControlPanel
from imio.urban.dataimport.browser.import_panel import ImporterSettings
from imio.urban.dataimport.browser.import_panel import ImporterSettingsForm
from imio.urban.dataimport.urbaweb.settings import UrbawebImporterFromImportSettings


class ThuinImporterSettingsForm(ImporterSettingsForm):
    """ """

class ThuinImporterSettings(ImporterSettings):
    """ """
    form = ThuinImporterSettingsForm


class ThuinImporterControlPanel(ImporterControlPanel):
    """ """
    import_form = ThuinImporterSettings


class ThuinImporterFromImportSettings(UrbawebImporterFromImportSettings):
    """ """

    def get_importer_settings(self):
        """
        Return the db name to read.
        """
        settings = super(ThuinImporterFromImportSettings, self).get_importer_settings()

        db_settings = {
            'db_name': '',
        }

        settings.update(db_settings)

        return settings
