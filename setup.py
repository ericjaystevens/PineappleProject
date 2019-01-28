from setuptools import setup                                 
setup(                                                           
    name="pineappleProject",                                     
    version="0.1.3",                                             
    author="Eric Stevens",                                       
    author_email="pineappleAdmin@example.com",                      
                                                                 
    # Packages                                                   
    packages=["pypineapple"],                                    
                                                                 
    # Include additional files into the package                  
    include_package_data = True,

    package_data = {
        'static': ['*'],
        'templates': ['*']
    },

    url="https://github.com/ericjaystevens/PineappleProject",    
    description="Sample Project for code release pipeline",      
                                                                 
    # Dependent packages                                         
    install_requires=[                                           
        "flask", 
        "requests",                                                
    ],                                                           
)                                                                