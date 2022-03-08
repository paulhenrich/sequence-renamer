# this is an example for how you could parse your sequences file to create a
# dict of ID to descriptive name and then use that to rewrite the output file
# from your processor to include the descriptive name.

import re

# used to search for labels in the sequence metadata and extract them into two
# capture groups (two interior parens)
EXTRACT_ID_AND_FULL_NAME = re.compile('^>(\S*)\s(.*)')

id_to_names = {}
def main():
    build_dict()
    read_and_write_new_summaries()

def build_dict():
    with open('sequences.txt') as sequences_file:
        for line in sequences_file:
            match = re.match(EXTRACT_ID_AND_FULL_NAME, line)
            if match:
                # build the dict
                id_to_names[match.group(1)] = format_name(match.group(0))

def read_and_write_new_summaries():
    with open('summaries.txt') as summaries_file, open('new_summaries.txt', 'w') as new_summaries_file:
        for line in summaries_file:
            match = re.match(r'(^\S*)', line)
            id = match.group(1)
            new_name = id_to_names[id]
            updated_line = re.sub(r'^\S*', new_name, line)
            # I did a lot of print-based debugging while doing this because I
            # was learning python while writing this, like this:
            # print(updated_line)
            new_summaries_file.write(updated_line)


def format_name(metadata):
    return re.sub(r'\s', '_', metadata)


if __name__ == '__main__':
    main()
