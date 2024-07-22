import sys
from optparse import OptionParser
#debug poruke
def debug(msg,verbose):
	if verbose:
		print(msg)
#dodavanje opcija
parser = OptionParser()
parser.add_option("-i", "--input",action="store",dest="input_file",help="Ulazni fajl")
parser.add_option("-o", "--output",action="store",dest="output_file",help="Izlazni fajl")
parser.add_option("-v", "--verbose", action="store_true",dest="debug",help="Verbosity")
parser.set_defaults(debug=False)
# parsiranje opcija
opts,args = parser.parse_args()
# ako opcije nisu zadane
if opts.input_file == None or opts.output_file == None:
	parser.print_help()
	sys.exit(0)
#sam program
f1 = open(opts.input_file,"rb")
debug("Reading file...",opts.debug)
d1 = f1.read()
f1.close()
debug("Inverting data...",opts.debug)
d2 = d1[::-1]
debug("Writing file...",opts.debug)
with open(opts.output_file,"wb") as f2 :
	f2.write(d2)
debug("Wrote file",opts.debug)

# pokreni kao: python 15_parser_argumenata1.py -i 15_parser_argumenata1.py -o yp.1atanemugra_51 -v