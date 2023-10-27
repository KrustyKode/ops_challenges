# ops_challenges
Ops 201 challenges

## Making some scripts today. for lab


### # Decleration of variables


newDir=("dir1" "dir2" "dir3" "dir4")

# Decleration of functions
echo ${newDir[2]}
echo ${newDir[0]}

for  ((i=1; i<=5; i++)); do
     mkdir dir1 &
done
echo ${newDir[0]}
# Main


# End