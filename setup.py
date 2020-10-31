from setuptools import setup

setup(name                =  'enigma'                                      ,
      version             =  '1.1.4'                                       ,
      description         =  'Enigma Machine Emulator for Python.'         ,
      url                 =  'http://github.com/artemis-beta/enigma'       ,
      author              =  'Kristian Zarebski'                           ,
      author_email        =  'krizar312@gmail.com'                         ,
      license             =  'MIT'                                         ,
      packages            =  ['enigma']                                    ,
      zip_safe            =  False                                         ,
      install_requires    =  ['nose2', 'hypothesis']
     )
