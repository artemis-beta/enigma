from setuptools import setup

_test_requires = ['nose2', 'hypothesis']

setup(name                =  'enigma'                                      ,
      version             =  '1.1.4'                                       ,
      description         =  'Enigma Machine Emulator for Python.'         ,
      url                 =  'http://github.com/artemis-beta/enigma'       ,
      author              =  'Kristian Zarebski'                           ,
      author_email        =  'krizar312@gmail.com'                         ,
      license             =  'MIT'                                         ,
      packages            =  ['enigma']                                    ,
      zip_safe            =  False                                         ,
      tests_require       =  _test_requires                                ,
      extras_require      =  {'tests': _test_requires}                     ,
      test_suite          =  'nose2.collector.collector'                   
     )
