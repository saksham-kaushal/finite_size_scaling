# FILE:  scalingPlot.sh
# TASK:  create scaling plot to inspect data collapse
# USAGE: bash scalingPlot.sh <xc> <a> <b>
P='./ORDER_PARAMETER' 	# path to input files
gnuplot -persist << EOF

set key samplen 1. left					# customize key
set xl "(x-xc) L^a"; set yl "y L^b"			# set x,y labels 
xc=$1; a=$2; b=$3					# set scaling parameters
set label 1 "xc=$1\na =$2\nb =$3" at graph 0.7,0.2 	# list scaling parameters
sx(x,L)=(x-xc)*L**a; sy(y,L)=y*L**b			# def scaling assumption

p "$P/orderParam_L4.dat"  u (sx(\$1,4)): (sy(\$2,4))  w lp t "L=4"\
, "$P/orderParam_L6.dat"  u (sx(\$1,6)): (sy(\$2,6))  w lp t "  6"\
, "$P/orderParam_L8.dat"  u (sx(\$1,8)): (sy(\$2,8))  w lp t "  8"\
, "$P/orderParam_L10.dat" u (sx(\$1,10)):(sy(\$2,10)) w lp t " 10"\
, "$P/orderParam_L12.dat" u (sx(\$1,12)):(sy(\$2,12)) w lp t " 12"\
, "$P/orderParam_L18.dat" u (sx(\$1,18)):(sy(\$2,18)) w lp t " 18"
EOF
