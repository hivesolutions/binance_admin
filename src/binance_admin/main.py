#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Binance Admin
# Copyright (c) 2008-2020 Hive Solutions Lda.
#
# This file is part of Hive Binance Admin.
#
# Hive Binance Admin is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Binance Admin is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Binance Admin. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2020 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import appier
import appier_extras

from binance_admin import models

class BinanceAdminApp(appier.WebApp):

    def __init__(self, *args, **kwargs):
        appier.WebApp.__init__(
            self,
            name = "binance",
            parts = (
                appier_extras.AdminPart,
            ),
            *args, **kwargs
        )

    def start(self):
        appier.WebApp.start(self)
        appier.hourly_work(self._snapshot)

    def _snapshot(self):
        models.BalanceFact.snapshot_s()

if __name__ == "__main__":
    app = BinanceAdminApp()
    app.serve()
else:
    __path__ = []
