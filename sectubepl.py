#!/usr/bin/python

import sys
import getopt

# @brief Print the help menu
def usage():
  print("sectubepl attempts to create a playlist of security tube videos in one page. The code for embedding the videos has changed so they can be added to the youtube playlist of your choice.")
  print("\t-h\tThis message.")
  print("\t-r\tRefresh the html file produced based on your playlist.")
  print("\t-a\tAdd a URL to your playlist.")
#END usage()

def main():

  # Used for command line parsing
  need_run = 0  # Do we upate the HTML?
  run_out = "" # Output filename
  need_add = 0  # Do we add a new url?
  add_url = "" # URL to Add

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
    # Add our new URL to our play list
    add_url(add_url)
  # ENDIF

  # Then we update our playlist html file.
  if need_run:
    assert run_out
    run_spider(run_out)
  #ENDIF

  sys.exit(0)
#END main()

if __name__ == "__main__":
  main()

