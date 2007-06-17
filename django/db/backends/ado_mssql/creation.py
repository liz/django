DATA_TYPES = {
    'AutoField':         'int IDENTITY (1, 1)',
    'BooleanField':      'bit',
    'CharField':         'varchar(%(maxlength)s)',
    'CommaSeparatedIntegerField': 'varchar(%(maxlength)s)',
    'DateField':         'smalldatetime',
    'DateTimeField':     'smalldatetime',
    'DecimalField':      'numeric(%(max_digits)s, %(decimal_places)s)',
    'FileField':         'varchar(100)',
    'FilePathField':     'varchar(100)',
    'FloatField':        'double precision',
    'ImageField':        'varchar(100)',
    'IntegerField':      'int',
    'IPAddressField':    'char(15)',
    'ManyToManyField':   None,
    'NullBooleanField':  'bit',
    'OneToOneField':     'int',
    'PhoneNumberField':  'varchar(20)',
    'PositiveIntegerField': 'int CONSTRAINT [CK_int_pos_%(column)s] CHECK ([%(column)s] > 0)',
    'PositiveSmallIntegerField': 'smallint CONSTRAINT [CK_smallint_pos_%(column)s] CHECK ([%(column)s] > 0)',
    'SlugField':         'varchar(%(maxlength)s)',
    'SmallIntegerField': 'smallint',
    'TextField':         'text',
    'TimeField':         'time',
    'USStateField':      'varchar(2)',
}
