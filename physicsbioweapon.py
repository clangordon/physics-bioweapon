#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: AGPL-3.0-only
#
import os

print("Clan Gordon Physics Bioweapon")
print("Licensed under the AGPLv3")
print("Secret ENV variables are commercially available on request")

cardiac_arrest = os.environ.get("PHYSICS_BIOWEAPON_CARDIAC_ARREST")
print(cardiac_arrest)

water_resonant_freq = os.environ.get("PHYSICS_BIOWEAPON_WATER_RESONANT_FREQ")
print(water_resonant_freq)

bioacoustic_resonant_freqs = os.environ.get("PHYSICS_BIOWEAPON_BIOACOUSTIC_RESONANT_FREQS")
print(bioacoustic_resonant_freqs)
