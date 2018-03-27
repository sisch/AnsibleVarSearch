# Ansible Variable Search
## Purpose
Ansible allows for variables to be declared in several places. But not necessarily anywhere near the usage. Thus, this program is supposed to traverse an ansible directory **recursively** and find all variable usages and declarations and map them.

The output is a markdown list sorted by variable name, with all files using it and all files declaring it. Since it is markdown, it can easily be checked into version control as Variables.md

## Example output
\#\# software_packages  
\#\#\# Usage  
\* ./roles/setup/tasks/main.yml  
\* ./maintenance.yml  
\#\#\# Declaration  
\* ./group_vars/debian.yml  
\* ./group_vars/ubuntu.yml  
\* ./host_vars/customHost.yml  

## How to use
`python3 main.py [path]`

With no path provided, the script starts from current working directory.

## Authors and License
* Simon Schliesky

Copyright 2018 Simon Schliesky.

This program is free software released under GPLv3. That essentially means license is granted for unlimited use, distribution, and modification of the program without warranty as long as all derivatives are available under the same license. For the legally binding complete license text, check [LICENSE.md]().
