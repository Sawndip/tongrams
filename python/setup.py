from distutils.core import setup, Extension

module = Extension('tongrams',
                    define_macros = [('MAJOR_VERSION', '1'),
                                     ('MINOR_VERSION', '0')],
                    include_dirs = ['../include', '../external/emphf', '../external/essentials'],
                    libraries = ['boost_iostreams', 'boost_regex'],
                    extra_compile_args=['-std=c++17'],
                    sources = ['tongrams.cpp'])

setup(name = 'tongrams',
      version = '1.0',
      description = 'Tons of N-Grams',
      ext_modules = [module])
