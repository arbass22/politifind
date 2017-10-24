from congress import Congress

def main():
    congress = Congress('DB9r6gpgLzulQ9Z2GQKbWfLWXh9FtrK9utwjoFZk')
    desired_keys = ['name', 'id', 'chair_id', 'subcommittees']
    house = congress.committees.filter('house').get('committees')
    senate = congress.committees.filter('senate').get('committees')
    committees = map(lambda d: { k: d[k] for k in desired_keys }, house + senate)
    print committees

if __name__ == '__main__':
    main()
