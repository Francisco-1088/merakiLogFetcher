import meraki
import config
import pandas as pd
from datetime import datetime, timedelta

dashboard = meraki.DashboardAPI(config.api_key)

orgs = dashboard.organizations.getOrganizations()

for org in orgs:
    if org['name']==config.org_name:
        org_id = org['id']

nets = dashboard.organizations.getOrganizationNetworks(org_id)

if config.startingAfter == "":
    now = datetime.now()
    startingAfter = (now - timedelta(days=config.daysLookback)).strftime("%Y-%m-%dT%H:%M:%S")
else:
    startingAfter = config.startingAfter

for net_name in config.net_names:
    net_id = ""
    for net in nets:
        if net['name']==net_name:
            net_id = net['id']

    if net_id != "":
        for prod in config.productType:
            try:
                logs = dashboard.networks.getNetworkEvents(networkId=net_id, direction='prev', productType=prod, perPage=1000, startingAfter=startingAfter)
                events_df = pd.DataFrame(logs['events'])
                events_df.to_csv(f"{net_name}_{prod}_logs.csv")
            except meraki.APIError as e:
                print(e, net_name)
