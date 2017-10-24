from congress import Congress

def main():
    congress = Congress('DB9r6gpgLzulQ9Z2GQKbWfLWXh9FtrK9utwjoFZk')
    desired_keys = ['bill_id', 'number', 'title', 'active', 'primary_subject', 'summary_short', 'latest_major_action_date', 'latest_major_action']
    house_bills = congress.bills.recent('house').get('bills')
    senate_bills = congress.bills.recent('senate').get('bills')
    bills = map(lambda d: { k: d[k] for k in desired_keys }, house_bills + senate_bills)

if __name__ == '__main__':
    main()
