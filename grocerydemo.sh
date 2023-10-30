#!/bin/bash

# Script Name:                  HDemo.sh
# Author:                       Michael Sineiro
# Date of latest revision:      10/25/2023
# Purpose:                      Demo variables / and functions
# Execution:                    bash demo.sh ./demo.sh chmod -x demo.sh


# Decleration of variables

grocery_list=("apples" "milk" "bread" "eggs")

is_item_in_list() {
    search_item="$1"
    for iteam in "${grocery_list[@]}"; do

        if [ "$item" == "$search_item"]; then
            return 0
        fi
    done
    return 1
}

while true; do
    read -p "Enter an ithem to check if it's on the list"

    if [ "item_to_check" = "done"]; then
        break
    fi

if is_item_in_list "$item_to_check"; then
    echo "Item '$item_to_check' is already on your list.";
else

    read -p " '$item_to_check' is not on your list. Add it? "
    if [ "$add_item" = "yes"]; then
        grocery_list+=("$item_to_check")
        echo "'Item '$item_to_check' added to list"
    else
        echo "'$item_to_check' is not in your list"
        fi
    fi
done

read -p "Want to see the new list?" show_list
if ["$show_;ist" = "yes"]; then
    echo "Your list is completed"
    echo "${grocery_list[@]}"
else
    echo "Okay, we can look later"
fi


# Decleration of functions

# Main


# End