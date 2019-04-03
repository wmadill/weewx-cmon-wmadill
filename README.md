# weewx-cmon-wmadill

## Description
Initially this is a "fork" of Matthew Wall's WeeWX computer monitoring (cmon) 
extension and skin. The version I used is at
http://lancet.mit.edu/mwall/projects/weather/releases/weewx-cmon-0.16.tgz.

## Changes 
The only changes to date (April 2019) are the name of the public_html directory
where the cmon files are and admusting the frequency on non-daily image
generation. Eventually the extension will be modified for Raspberry Pi
(requires schema changes) and the skin will be subsumed by the
weewx-orcas-skin skin.

## Installation
Install as described in "cmon-readme.txt", Matthew's original readme.txt. I
chose to put the generated html file and images in a "sysinfo" directory rather
than in one named "cmon". This is changed in weewx.conf.
