#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import time
from jinja2 import Environment, PackageLoader


env = Environment(loader=PackageLoader('suntrek', 'jinjatemplates'))

# INDEX file
indextemplate = env.get_template('index.html')
indexfile = open("index.html","w")
indexfile.write(indextemplate.render(date=time.ctime()))
indexfile.close()

#EIT file
eitfilterstemplate = env.get_template('eitfilters.html')
eitfiltersfile = open("eitfilters.html","w")

eitlabels = open("output/current_eit.json","r")
carousellabels = json.load(eitlabels)

eitfiltersfile.write(eitfilterstemplate.render(carousellabels=carousellabels))
eitfiltersfile.close()

#Particles file
particlefluxtemplate = env.get_template('particleflux.html')
particlefluxfile = open("particleflux.html","w")

solarparticlep10flux = open('output/solarparticleP10flux.txt','r').read()
solarparticlep100flux = open('output/solarparticleP100flux.txt','r').read()

result = particlefluxtemplate.render(dataseries01=solarparticlep10flux, dataseries02=solarparticlep100flux)

particlefluxfile.write(result)
particlefluxfile.close()

#Electrons file
electronfluxtemplate = env.get_template('electronflux.html')
electronfluxfile = open("electronflux.html","w")

solarelectron08flux = open('output/solarelectron08flux.txt','r').read()
solarelectron20flux = open('output/solarelectron20flux.txt','r').read()

result = electronfluxtemplate.render(dataseries01=solarelectron08flux, dataseries02=solarelectron20flux)

electronfluxfile.write(result)
electronfluxfile.close()

#XRayy file
xrayfluxtemplate = env.get_template('xrayflux.html')
xrayfluxfile = open("xrayflux.html","w")

solarxrayshortflux = open('output/solarxrayshortflux.txt','r').read()
solarxraylongflux = open('output/solarxraylongflux.txt','r').read()

result = xrayfluxtemplate.render(dataseries01=solarxrayshortflux, dataseries02=solarxraylongflux)

xrayfluxfile.write(result)
xrayfluxfile.close()


#Sunspot file
sunspotstemplate = env.get_template('sunspots.html')
sunspotsfile = open("sunspots.html","w")

sunspotlabels = open('output/sunspot_labels.txt','r').read()

result = sunspotstemplate.render(dataseries01=sunspotlabels)

sunspotsfile.write(result)
sunspotsfile.close()

#Alerts
alertstemplate = env.get_template('alerts.html')
alertsfile = open("alerts.html","w")

alertcontent = open("output/alerts.json","r")
alertlist = json.load(alertcontent)


result = alertstemplate.render(alertlist=alertlist)

alertsfile.write(result)
alertsfile.close()

#Sunspots progression
solarcycletemplate = env.get_template('solarcycle.html')
solarcyclefile = open("solarcycle.html","w")

observedsolarcycle = open('output/observedsolarcycle.json','r').read()
smoothedsolarcycle = open('output/smoothedsolarcycle.json','r').read()
predictedsmoothedsolarcycle = open('output/predictedsmoothedsolarcycle.json','r').read()

result = solarcycletemplate.render(dataseries01=observedsolarcycle, dataseries02=smoothedsolarcycle, dataseries03=predictedsmoothedsolarcycle)

solarcyclefile.write(result)
solarcyclefile.close()

#3day forecast file
threedayforecasttemplate = env.get_template('threedayforecast.html')
threedayforecastfile = open("threedayforecast.html","w")

threedayforecastg = open('output/threedayforecastg.json','r').read()
threedayforecastrb = open('output/threedayforecastrb.json','r').read()
threedayforecastr = open('output/threedayforecastr.json','r').read()

tdfg=json.loads(threedayforecastg)
#tdfrb=json.loads(threedayforecastrb)
tdfr=json.loads(threedayforecastr)

result = threedayforecasttemplate.render(dataseries01=threedayforecastg,
                                         dataseries02=threedayforecastrb,
                                         dataseries03=threedayforecastr,
                                         e1=tdfg["expected"],
                                         r1=tdfg["rationale"],

#                                         r2=tdfrb["rationale"],

                                         r3=tdfr["rationale"],

)

threedayforecastfile.write(result)
threedayforecastfile.close()
