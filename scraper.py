from optparse import OptionParser

parser = OptionParser()
parser.add_option("-b", "--board", type="string", dest="boardname")
parser.add_option("-d", "--dest", type="string", dest="dest")
(options, args) = parser.parse_args()

