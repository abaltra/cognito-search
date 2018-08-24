from __future__ import print_function
import os
import sys
import re
import argparse
import boto3
import time
import pprint
import shelve


pp = pprint.PrettyPrinter(indent=2)

def search_cognito_userpools(user_pools, search_strings):
    num_matches = 0
    for parameter in user_pools:
        found_count = 0
        for search_string in search_strings:
            try:
                if search_string.lower() in parameter['Name'].lower():
                    found_count += 1
            except Exception as e:
                raise ("Error processing user pool: {}\nUser Pool: {}".format(str(e), parameter))
        if found_count > 0:
            num_matches += 1
            pp.pprint(parameter)
            print("\n")


    print("Found {} matches out of {} user pools from Cognito".format(
        num_matches,
        len(user_pools)))


def load_user_pools(profile_name = None):
    if profile_name:
        session = boto3.session.Session(profile_name=profile_name)
    else:
        session = boto3.session.Session()

    client = session.client('cognito-idp')
    next_token = None
    page = 1
    max_results = 60
    full_params = []

    print("Reading user pools from Cognito")
    while True:
        try:
            sys.stdout.write('.')
            sys.stdout.flush()
            if next_token:
                response = client.list_user_pools(
                    MaxResults=max_results,
                    NextToken=next_token
                )
            else:
                response = client.list_user_pools(
                    MaxResults=max_results
                )
            full_params.extend(response['UserPools'])
            if 'NextToken' in response:
                next_token = response['NextToken']
            else:
                break

            page += 1
        except Exception as e:
            print("Error querying list of user pools: {}".format(repr(e)))
            raise

    sys.stdout.write('\n')

    return full_params

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--search-string', required=True,
                        action='append', dest='search_string',
                        help='The string to search Cognito for any user pools with this in the name.')
    parser.add_argument('--profile', required=False,
                        help='The AWS profile to run this request under.' )
    parser.add_argument('--no-cache', action='store_true', default=False,
                        help='Will force fresh loading of user pools from Cognito')
    args = parser.parse_args()
    return args
    
    
def main():
    here = os.path.abspath(os.path.dirname(__file__))
    about = {}
    with open(os.path.join(here, 'version.py'), 'r') as f:
        exec(f.read(), about)

    print('Cognito Search version {}'.format(about['__version__']))

    args = parse_args()

    print("Searching User Pool for {}".format(args.search_string))
        
    user_pools = load_user_pools(args.profile)
    search_cognito_userpools(user_pools, args.search_string)

if __name__ == '__main__':
    main()
