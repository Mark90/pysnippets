import platform
import os
import re
import subprocess


def get_processor_name():
    if platform.system() == "Windows":
        return platform.processor()
    elif platform.system() == "Darwin":
        os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
        command = "sysctl -n machdep.cpu.brand_string"
        b_cpu_details = subprocess.check_output(command.split(' ')).strip()
        return b_cpu_details.decode()
    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        all_info = subprocess.check_output(command.split(' ')).strip()
        for line in all_info.decode().split("\n"):
            if "model name" in line:
                return re.sub(".*model name.*:", "", line, 1)
    return ""
