import urllib2

def sonoff(switchstate):
        send_params = {'user' : 'hello',
                       'password' : 'world',
                       'cmnd' : 'Power {0}'.format(switchstate)
                        }
        new_send_params = []
        for (k, v) in send_params.items():
           new_send_params.append(k + "=" + urllib2.quote(v))

        url = 'http://fritz.box?'+ '&'.join(new_send_params)
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        print "Request URL: " + url
#       print response.read()
