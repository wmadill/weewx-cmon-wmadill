# Change Log

## v0.1 - 30 March 2019
- Initial upload of an unmodified weewx-cmon v0.16 from Matthew Wall
- Renamed original readme.txt and changelog to avoid conflicts with
repo version for my changes
- Modify cmon skin to generate non-daily charts only infrequently
rather than on every archive interval. The changes use the default
weewx skin as example.
- The location of the cmon files is changed in weewx.conf 
(see commit 7f983ef in the weewx-orcas repo).
