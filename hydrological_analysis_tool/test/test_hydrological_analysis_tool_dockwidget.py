# coding=utf-8
"""DockWidget test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'sam.murphy@ecmwf.int'
__date__ = '2023-07-11'
__copyright__ = 'Copyright 2023, Sam Murphy / ECMWF'

import unittest

from qgis.PyQt.QtGui import QDockWidget

from hydrological_analysis_tool_dockwidget import HydrologicalAnalysisToolDockWidget

from utilities import get_qgis_app

QGIS_APP = get_qgis_app()


class HydrologicalAnalysisToolDockWidgetTest(unittest.TestCase):
    """Test dockwidget works."""

    def setUp(self):
        """Runs before each test."""
        self.dockwidget = HydrologicalAnalysisToolDockWidget(None)

    def tearDown(self):
        """Runs after each test."""
        self.dockwidget = None

    def test_dockwidget_ok(self):
        """Test we can click OK."""
        pass

if __name__ == "__main__":
    suite = unittest.makeSuite(HydrologicalAnalysisToolDialogTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

