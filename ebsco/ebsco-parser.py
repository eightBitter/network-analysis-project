# python 3.7.0. This script pulls out specified fields from EBSCO's "Generic bibliographic management format"
# and transforms the data to a csv
import re

class RIS:
    """ RIS file structure """
    def __init__(self, in_file=None):
        """ Initialize and parse input """
        self.records = []
        if in_file:
            self.parse(in_file)

    def parse(self, in_file):
        """ Parse input file """
        self.current_tag = None
        self.current_record = None
        # divide each line into two buckets, delimited by hyphen (-)
        prog = re.compile("^([A-Z][A-Z])\- (.*)")
        lines = []
        for line in in_file:
            lines.append(line)
        for line in lines:
            # chops data into records based on blank space
            if line == "\n":
                continue
            # put data into the two buckets if it matches the pattern on line 18
            match = prog.match(line)
            if match:
                tag = match.groups()[0]
                field = match.groups()[1]
                self.process_field(tag, field)
            else:
                raise ValueError(line)

    def process_field(self, tag, field):
        """ Process RIS file field  and pull out specific tags """
        if tag == "TI":
            self.current_record = {tag: field}
        elif tag == "UR":
            self.records.append(self.current_record)
            self.current_record = None
        elif tag in "JN":
            if tag in self.current_record:
                self.current_record[tag].append(field)
            else:
                self.current_record[tag] = [field]
        elif tag in "DE":
            if tag in self.current_record:
                self.current_record[tag].append(field)
            else:
                self.current_record[tag] = [field]
        elif tag in "SU":
            if tag in self.current_record:
                self.current_record[tag].append(field)
            else:
                self.current_record[tag] = [field]
        elif tag in "KW":
            if tag in self.current_record:
                self.current_record[tag].append(field)
            else:
                self.current_record[tag] = [field]
        elif tag in "PY":
            if tag in self.current_record:
                self.current_record[tag].append(field)
            else:
                self.current_record[tag] = [field]
        elif tag in "DT":
            self.current_record[tag] = str(field)
        # else:
            # if not tag in self.current_record:
            # self.current_record[tag] = field
            # else:
            #     error_str = "Duplicate tag: %s" % tag
            #     raise ValueError(error_str)

def main():
    """ Convert output to csv """
    import csv
    with open("american-journal-health-promotion-in.txt", "rt") as ris_file:
        ris = RIS(ris_file)
    with open("output.csv", "w") as ris_csv:
        wcsv = csv.DictWriter(ris_csv, fieldnames=["JN","TI","DT","PY","KW","DE","SU"])
        # ris.records[0].keys())
        wcsv.writeheader()
        for record in ris.records:
            wcsv.writerow(record)
    print("done")

if __name__ == "__main__":
    main()
