#!/bin/bash

# Script Name:                  greber.sh
# Author:                       Michael Sineiro
# Date of latest revision:      10/31/2023
# Purpose:                      Demo variables / and functions
# Execution:                    bash greber.sh ./greber.sh chmod -x greber.sh


# Decleration of variables

# Decleration of functions

# Function to display component info
 format () {
    component=$1
    info=$2

    echo "[$component]"
    echo "$info"
    echo ""
}

# Main
#!/bin/bash

# Use lshw to retrieve system information and filter with grep
output=$(sudo lshw | grep -E "description:|product:|vendor:|physical id:|bus info:
                                |width:|clock:|capabilities:|configuration:|resources:")



# computer name
name=$(hostname)
format "Computer Name" "$name"

# CPU
cpuInfo=$(echo "$output" | grep -E "description:|product:|vendor:|physical id:|bus info:|width:")
format "CPU" "$cpuInfo"

# RAM
ramInfo=$(echo "$output" | grep -E "description:|physical id:|size:")
format "RAM" "$ramInfo"

# display adapter 
displayInfo=$(echo "$output" | grep -E "description:|product:|vendor:|physical id:
                                            |bus info:|width:|clock:|capabilities:
                                            |configuration:|resources:")
format "Display Adapter" "$displayInfo"

# network adapter
networkInfo=$(echo "$output" | grep -E "description:|product:|vendor:|physical id:
                                            |bus info:|logical name:|version:|serial:
                                            |size:|capacity:|width:|clock:|capabilities:
                                            |configuration:|resources:")
format "Network Adapter" "$networkInfo"


# End



