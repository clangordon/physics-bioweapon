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

heart_rate_acceleration = os.environ.get("PHYSICS_BIOWEAPON_HEART_RATE_ACCELERATION")
print(heart_rate_acceleration)

initial_heart_rate = os.environ.get("PHYSICS_BIOWEAPON_INITIAL_HEART_RATE")
print(initial_heart_rate)

heart_rate_failure = os.environ.get("PHYSICS_BIOWEAPON_HEART_RATE_FAILURE")
print(heart_rate_failure)

water_resonant_freq = os.environ.get("PHYSICS_BIOWEAPON_WATER_RESONANT_FREQ")
print(water_resonant_freq)

bioacoustic_resonant_freqs = os.environ.get("PHYSICS_BIOWEAPON_BIOACOUSTIC_RESONANT_FREQS")
print(bioacoustic_resonant_freqs)

if(cardiac_arrest):
  print("Cardiac arrest")

if(bioacoustic_resonant_freqs):
  print("Bioacoustic resonant freqs")
