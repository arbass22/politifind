from congress import Congress

def main():
    congress = Congress('DB9r6gpgLzulQ9Z2GQKbWfLWXh9FtrK9utwjoFZk')
    desired_keys = ['fec_candidate_id', 'first_name', 'last_name', 'party', 'title', 'youtube_account', 'facebook_account', 'twitter_account', 'date_of_birth', 'state', 'title']
    house = congress.members.filter('house')[0].get('members')
    senate = congress.members.filter('senate')[0].get('members')
    print house[0]
#    members = map(lambda d: { k: d[k] for k in desired_keys }, house + senate)

if __name__ == '__main__':
    main()
