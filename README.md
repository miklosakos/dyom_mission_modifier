# DYOM mission modifier

This Python script allows you to change the "published" state of a [DYOM](https://dyom.gtagames.nl) mission.

## Usage

Script needs Python 3.12+ and can be run as follows: `python3 app.py DYOMn.dat`

## What gets changed

A Design Your Own Mission mission file's first 4 bytes can be the following:

For unpublished missions:

| 06 	| 00 	| 00 	| 00 	|
|---	|---	|---	|---	|

For published missions:

| FA 	| FF 	| FF 	| FF 	|
|---	|---	|---	|---	|

From my minimal research it looks like there is no checksum check inside the mod to make sure the mission file has not been tampered with.