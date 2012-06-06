#!/usr/bin/python

import sys
import os
import getopt


# @brief Print the help menu
def usage():
  print("\t-h\tThis message.")
  print("\t-r\tRefresh the html file produced based on your playlist.")
  print("\t-a\tAdd a URL to your playlist.")
#END usage()

# @brief Parse the configuration file that contains our URL list
# @return A list of URLs in our playlist to parse
def parse_config():

  url_list = []
  
  # Get the home directory where our config file is
  homedir = os.path.expanduser('~')

  # See if the file is there, if it is, open it
  # otherwise, create it then open it
  if(not (os.path.exists(homedir + "/.sectubepl"))):
    open(homedir + "/.sectubepl", "w").close() # Create the file...

  # Now open the file for reading
  config_in = open(homedir + '/.sectubepl', "r")


  config_in.close()

  return url_list

#END parse_config

# @brief Add a url to the configuration file
# @param url_to_add   The filename of the URL to add
def run_add_url(url_to_add):
  print url_to_add
#END add_url

# @brief Run our spider against security tube and output the parsed youtube videos.
# @param filename_out   The html file to output to
def run_spider(filename_out, url_list):
  print filename_out
#END run_spider

def main():

  # Used for command line parsing
  need_run = 0  # Do we upate the HTML?
  run_out = "" # Output filename
  need_add = 0  # Do we add a new url?
  add_url = "" # URL to Add

  if len(sys.argv) < 2:
    usage()
    sys.exit(1)
  #ENDIF

  # Get our command line arguments
  try:
    flags = "hr:a:"
    opts, args = getopt.getopt(sys.argv[1:], flags)
  except getopt.GetoptError, err:
    print str(err)
    usage()
    sys.exit(-1)
  # END

  # Parse our config file
  list_of_urls = []
  list_of_urls = parse_config()

  # Parse our command line arguments
  for o, a in opts:
    if o == "-h":
      usage()
      sys.exit(0)
    elif o == "-r":
      need_run = 1
      run_out = a
    elif o == "-a":
      need_add = 1
      add_url = a
    else:
      usage()
      sys.exit(0)
  # END for

  # First we add a URL if one is provided
  if need_add:
    assert add_url
    run_add_url(add_url)
  # ENDIF

  # Then we update our playlist html file.
  if need_run and len(list_of_urls) > 0:
    assert run_out
    run_spider(run_out)
  #ENDIF

  sys.exit(0)
#END main()

if __name__ == "__main__":
  main()

