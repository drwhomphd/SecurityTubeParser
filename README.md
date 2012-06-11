sectubepl is a script that will take URL's cut and pasted from Security Tube, add them to a configuration file, and then run a spider over the provided URLs to pull out only the youtube links in embedded iframes. The iframes are written to a specified file. The video's title is included as well. 

The configuration file is in the following format:
<url>,<bool>

The boolean is there for future need and the comma delimited configuration file's format can be expanded if other features must be added in the future. The configuration file's hard coded as ~/.sectubepl.

Run ./sectubepl.py -h for command line information.
