from database import CheckDB, OrganizingCites
from citationslicer import ParseCitations, filepath1
from net import get_file

CheckDB()
citation = ParseCitations(filepath1)
OrganizingCites(citation)
# get_file("100.10")