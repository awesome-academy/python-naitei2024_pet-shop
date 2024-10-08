from django.utils.translation import gettext_lazy as _

GENDER_CHOICES = [
    ('Male', _('Male')),
    ('Female', _('Female')),
    ('Other', _('Other')),
]

SIZE_CHOICES = [
    ('None', _('None')),
    ('S', 'S'),
    ('XS', 'XS'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
]

PAYMENT_STATUS_CHOICES = [
    ('Wait_for_pay', _('Wait for pay')),
    ('Wait_for_preparing', _('Wait for preparing')),
    ('Wait_for_delivery', _('Wait for delivery')),
    ('Completed', _('Completed')),
    ('Cancelled', _('Cancelled')),
]

PAYMENT_METHOD_CHOICES = [
    ('CASH', _('Cash')),
    ('VISA', _('Visa')),
    ('BANK', _('Bank')),
]

CITIES = [
    'hanoi',
    'ha noi',
    'hn',
    'danang',
    'da nang',
    'dn',
    'hcm',
    'ho chi minh',
    'hochiminh',
    'hcm city',
    'hcmcity']

VOUCHER_STATUS_CHOICES = [
    ('USABLE', _('Usable')),
    ('EXPIRED', _('Expired')),
    ('UPCOMING', _('Upcoming')),
    ('USED', _('Used')),
]

DEFAULT_USER_AVATAR = "image/upload/v1723017084/wlwartuoohu21c2wzu8k.png"
MAX_LENGTH_NAME = 255
MAX_LENGTH_PHONENUM = 10
MAX_LENGTH_OTP_SCRET = 32
MAX_LENGTH_CHOICES = 255
MAX_LENGTH_PASSWORD = 128
REGEX_USERNAME = r"^\w+$"
REGEX_EMAIL = r"^[\w\.-]+@gmail\.com$"
REGEX_PHONENUM = r'^0\d{9}$'

DEFAULT_DISPLAY_CATEGORIES = ["clothing", "food"]

ROUNDING_VALUE = 0.8
HALF_STAR_VALUE = 0.45
PAGINATE_BY = 9
