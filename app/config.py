apps_template = { 'ag' :        { 'number': 10, 'type': 'web', 'mirrored': True, 'display': 'www.apartmentguide.com' }, 
                  'rentals':    { 'number': 6, 'type': 'web', 'mirrored': True, 'display': 'www.rentals.com' },
                  'mag':        { 'number': 5, 'type': 'web', 'mirrored': True, 'display': 'm.apartmentguide.com' },
                  'agsites':    { 'number': 2, 'type': 'web', 'mirrored': True, 'display': 'agsites.com' },
                  'myag':       { 'number': 2, 'type': 'web', 'mirrored': False, 'display': 'my.apartmentguide.com'},
                  'mnhg':       { 'number': 2, 'type': 'web', 'mirrored': True, 'display': 'm.newhomeguide.com' },
                  'rnrui':      { 'number': 2, 'type': 'web', 'mirrored': False, 'display': 'reviews.apartmentguide.com' },
                  'mobileapi':  { 'number': 2, 'type': 'service', 'mirrored': True, 'display': 'm.api.apartmentguide.com' },
                  'metasaurus': { 'number': 2, 'type': 'service', 'mirrored': True, 'display': 'metasaurus' },
                  'onesearch':  { 'number': 3, 'type': 'service', 'mirrored': True, 'display': 'onesearch.svc.primedia.com' },
                  'zutron':  { 'number': 3, 'type': 'service', 'mirrored': True, 'display': 'zutron.primedia.com' }
                }

def generate_hosts(sites):
   complete_dict = {}
   for site, info in sites.iteritems():
      complete_dict[site] = {}
      if info['type'] == 'web':
         middle = '-web-'
      else:
         middle = '-'
      complete_dict[site]['atl'] = [ site + middle + str(x).zfill(2) + '.atl.primedia.com' for x in range(1,info['number']+1) ]
      if info['mirrored']:
         complete_dict[site]['lax'] = [ site + middle + str(x).zfill(2) + '.lax.primedia.com' for x in range(1,info['number']+1) ]
      else:
         complete_dict[site]['lax'] = [ 'none' ]
   return complete_dict

def generate_mappings(sites):
   complete_dict = {}
   for site, info in sites.iteritems():
      complete_dict[site] = sites[site]['display']
   return complete_dict
