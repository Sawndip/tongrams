from distutils.core import setup, Extension

module1 = Extension('tongram',
                    define_macros = [('MAJOR_VERSION', '1'),
                                     ('MINOR_VERSION', '0')],
                    include_dirs = ['../include', '../external/emphf', '../external/essentials'],
                    libraries = ['boost_iostreams',
                                 'boost_regex', 'boost_chrono', 'boost_date_time',
                                 'pthread'],
                    extra_compile_args=['-std=c++14'],
                    sources = ['tongrammodule.cpp'])

setup(name = 'tongrams',
      version = '1.0',
      description = 'Tons of N-Grams',
      ext_modules = [module1])
