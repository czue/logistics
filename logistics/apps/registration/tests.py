import unittest
from django import forms
from rapidsms.conf import settings
from rapidsms.tests.scripted import TestScript
from logistics.apps.registration.forms import IntlSMSContactForm
from logistics.apps.logistics.models import Location, Facility, SupplyPointType 
from logistics.apps.registration.handlers.registration import REGISTER_MESSAGE,\
    HELP_MESSAGE

class TestRegister(TestScript):
    fixtures = ["ghana_initial_data.json"] 
    def setUp(self):
        TestScript.setUp(self)
        location = Location.objects.get(code='de')
        facilitytype = SupplyPointType.objects.get(code='hc')
        rms = Facility.objects.get(code='garms')
        Facility.objects.get_or_create(code='dedh', name='Dangme East District Hospital',
                                       location=location, active=True,
                                       type=facilitytype, supplied_by=rms)

    def testRegister(self):
        a = """
              8005551212 > register
              8005551212 < %(register_message)s
              8005551212 > register stella
              8005551212 < Sorry, I didn't understand. To register, send register <name> <facility code>. Example: register john dwdh'
              8005551212 > register stella doesntexist
              8005551212 < Sorry, can't find the location with FACILITY CODE doesntexist
              8005551212 > register stella dedh
              8005551212 < Congratulations stella, you have successfully been registered for the Early Warning System. Your facility is Dangme East District Hospital
            """ % {'register_message':HELP_MESSAGE}
        self.runScript(a)

    def testRegisterTwice(self):
        a = """
              8005551212 > register stella dedh
              8005551212 < Congratulations stella, you have successfully been registered for the Early Warning System. Your facility is Dangme East District Hospital
              8005551212 > register cynthia dedh
              8005551212 < Congratulations cynthia, you have successfully been registered for the Early Warning System. Your facility is Dangme East District Hospital
            """
        self.runScript(a)

    def testWebPhoneRegistration(self):
        form = IntlSMSContactForm()
        idc = "%s%s" % (settings.INTL_DIALLING_CODE, settings.COUNTRY_DIALLING_CODE)
        self.assertEquals(form._clean_phone_number('16176023333'),'16176023333')
        self.assertEquals(form._clean_phone_number('1 617 602 3333'),'16176023333')
        self.assertEquals(form._clean_phone_number('1(617)6023333'),'16176023333')
        self.assertEquals(form._clean_phone_number('1-617-602-3333'),'16176023333')
        self.assertEquals(form._clean_phone_number('11-44-602-3333'),'11446023333')
        self.assertEquals(form._clean_phone_number('602-3333'),'6023333')
        # the following is considered poorly formatted, and not supported
        #self.assertEquals(form._clean_phone_number('+233(0)1234567'),'+2331234567')
        self.assertEquals(form._clean_phone_number('+2331234567'),'+2331234567')
        try:
            form._clean_phone_number('*01234567')
            self.fail('Cleaning "*01234567" should have raised a ValidationError, but it didn\'t')
        except forms.ValidationError:
            pass
        try:
            ddc = settings.DOMESTIC_DIALLING_CODE
            self.assertEquals(form._clean_phone_number('%s1234567' % ddc),'%s1234567' % idc)
        except NameError:
            # DOMESTIC_DIALLING_CODE not defined, no biggie
            pass
