
from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import netmiko_send_command  # netmiko 

nr = InitNornir(config_file="config.yaml")
results = nr.run(task=netmiko_send_command,command_string="show run")
print_result(results)

