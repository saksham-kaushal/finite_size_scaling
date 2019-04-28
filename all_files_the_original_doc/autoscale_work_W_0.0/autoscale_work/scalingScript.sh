# FILE:  scalingScript.sh
# TASK:  invoke scaling analysis program for different intervals xr
# USAGE: bash scalingScript.sh
for MAX in  1.5 1.25 1.0 0.75 ; 
do
 for MIN in -2.25 -2.0 -1.75 -1.5 -1.25 -1. -0.75 ;
 do
  python autoScale.py -f inputFiles.dat -o scaled_L4_6_8.out \
  	        -xc 0.1288 -a 1.57903 -b 0.514 -showS -xr ${MIN} ${MAX}
 done
done
