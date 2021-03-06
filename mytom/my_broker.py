from tom_alerts.alerts import GenericQueryForm, GenericAlert
from tom_alerts.models import BrokerQuery
from tom_targets.models import Target
from django import forms
import requests


broker_url = 'https://gist.githubusercontent.com/mgdaily/f5dfb4047aaeb393bf1996f0823e1064/raw/6fe1680f22b86467c50a21a138177838378eb143/example_broker_data.json'

class MyBrokerForm(GenericQueryForm):
    mag_min = forms.IntegerField(required=True)
    mag_max = forms.IntegerField(required=True)
    ra = forms.FloatField(required=False)
    name = forms.CharField(required=False)

class MyBroker:
    name = 'MyBroker'
    form = MyBrokerForm

    @classmethod
    def fetch_alerts(clazz, parameters):
        #print(parameters)
        response = requests.get(broker_url)
        response.raise_for_status()
        test_alerts = response.json()
        #print(test_alerts)
        return [alert for alert in test_alerts if alert['ra'] == parameters['ra'] or alert['name'] == parameters['name'] and alert['mag'] > parameters['mag_min'] and alert['mag'] < parameters['mag_max']]

    @classmethod
    def fetch_alert(clazz, alert_id):
        response = requests.get(broker_url)
        test_alerts = response.json()
        response.raise_for_status()
        for alert in test_alerts:
            if (alert['id'] == int(alert_id)):
                return alert
        return None


    @classmethod
    def to_generic_alert(clazz, alert):
        return GenericAlert(
            timestamp=alert['timestamp'],
            url= broker_url,
            id=alert['id'],
            name=alert['name'],
            ra=alert['ra'],
            dec=alert['dec'],
            mag=alert['mag'],
            score=alert['score']
        )

    @classmethod
    def to_target(clazz, alert):
        return Target(
            identifier=alert['id'],
            name=alert['name'],
            type='SIDEREAL',
            designation='MY ALERT',
            ra=alert['ra'],
            dec=alert['dec'],
        )

