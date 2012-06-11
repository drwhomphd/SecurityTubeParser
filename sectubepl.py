#!/usr/bin/python

import sys
import os
import getopt
import httplib

CONFIG_FILE = os.path.expanduser('~') + "/.sectubepl"

# @brief Print the help menu
def usage():
  print("\t-h\tThis message.")
  print("\t-r [filename]\tRefresh the html file produced based on your playlist.")
  print("\t-a [URL]\tAdd a URL to your playlist.")
#END usage()

# @brief Checks to see if the URL is valid
# @param url_to_check   The URL to check
def url_is_valid(url_to_check):
  # TODO: Make sure URL is valid
  return True
#END url_is_valid()

# @brief Parse the configuration file that contains our URL list
# @return A list of URLs in our playlist to parse
def parse_config():

  url_list = []
  
  # See if the file is there, if it is, open it
  # otherwise, create it then open it
  if(not (os.path.exists(CONFIG_FILE))):
    open(CONFIG_FILE, "w").close() # Create the file...

  # Now open the file for reading
  config_in = open(CONFIG_FILE, "r")

  config_lines = config_in.readlines()

  for line in config_lines:
    line_split = line.split(',')

    assert url_is_valid(line_split[0])

    url_list.append(line_split[0])

  #END for

  config_in.close()

  return url_list

#END parse_config

# @brief Add a url to the configuration file
# @param url_to_add   The filename of the URL to add
def run_add_url(url_to_add):

  # Open config file
  try:
    config_in = open(CONFIG_FILE, 'a+')
  except IOError:
    print("Cannot find " + CONFIG_FILE + ". Creating...")
    parse_config()
  # End try

  config_in.write(url_to_add+",0\n")

  config_in.close()

#END add_url

# @brief Run our spider against security tube and output the parsed youtube videos.
# @param filename_out   The html file to output to
def run_spider(filename_out, url_list):

  file_out = open(filename_out, 'w')

  file_out.write("<html>\n")

  for url in url_list:

    # Split url into two parts, we ignore http:// at the beginning
    # then we add back in 7 to take into account we removed
    # 7 characters before the find
    file_start = url[7:].find('/') + 7

    # First part is the main server, we still ignore the http:// portion.
    host = url[7:file_start]

    # Second part is the specific file
    fetch_file = url[file_start:]

    # Open our connection
    conn = httplib.HTTPConnection(host)

    # Get our file
    conn.request("GET", fetch_file)
    response = conn.getresponse()
    file_data = response.read()

    # Send file to HTML parser to find specific
    # youtube section and get specific youtube url


    # Write out specific youtube url to our
    # output file using our own embedded object
    # for the youtube video

  #END for

  file_out.write("</html>\n")

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

  if len(list_of_urls) == 0:
    print("No URLs in playlist")

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
  if need_add and add_url not in list_of_urls:
    
    assert add_url
    assert url_is_valid(add_url)

    run_add_url(add_url)
    list_of_urls.append(add_url)
  # ENDIF

  # Then we update our playlist html file.
  if need_run and len(list_of_urls) > 0:
  
    assert run_out
    
    run_spider(run_out, list_of_urls)
  #ENDIF


  sys.exit(0)
#END main()

if __name__ == "__main__":
  main()

