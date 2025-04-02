# MoERL Zoo - Utilities for MoERL
# Originally from: Unsloth Zoo - Utilities for Unsloth
# Copyright 2023-present Daniel Han-Chen, Michael Han-Chen & the Unsloth team.
# Modifications copyright 2025-present MoERL Team. All rights reserved.
#
# SPDX-License-Identifier: LGPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# MoERL-specific changes:
# - Renamed Unsloth references to MoERL
# - Added dependency checks for MoERL-specific packages


__version__ = "2025.4.2"

from importlib.util import find_spec
if find_spec("moerl") is None:
    raise ImportError("Please install MoERL via `pip install moerl`!")
pass
del find_spec

import os
if not ("MOERL_IS_PRESENT" in os.environ):
    raise ImportError("Please install MoERL via `pip install moerl`!")
pass

# Log MoERL-Zoo Utilities
os.environ["MOERL_ZOO_IS_PRESENT"] = "1"
del os
