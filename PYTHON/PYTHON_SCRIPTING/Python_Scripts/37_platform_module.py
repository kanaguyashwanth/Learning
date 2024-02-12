#Platform module is used to access underlying platform's data such as hardware, OS, and interpreter version
 
import platform
print(f"Operating System: {platform.system()}")
print(f'Python version: {platform.python_version()}')
print(platform.python_version_tuple())
print(platform.machine())
print(platform.platform())
print(platform.architecture())
print(platform.processor())
print(platform.node())
print(platform.uname())
