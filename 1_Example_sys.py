# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 18:52:08 2018

@author: uidq3949
"""

import sys

## sys.path : Path to module
PyLibFolder = 'd:/sandbox/build/VT_STK_02.02.05_INT-1/04_Engineering/31_PyLib/'

if PyLibFolder not in sys.path:
    sys.path.append(PyLibFolder)   
    
import stk_bsig

bsig = stk_bsig.stkBsig()
bsig.open('D:\\00_\\08_Data\\Python\\Seminar\\BSIG\\1-1_N1_Continuous_2018.09.01_at_10.24.24_LEFT__Rear.bsig')

#signal = []
signal = list()

signal.append(bsig.get_signal_by_name("DGPS CAN.RT-Range_ISO8855.RangeForward.RangePosForward"))

print signal[0][1]

################################################################################
# 한 디렉토리에서 여러 Bsig 파일을 어떻게 불러올까?  -> 2_Exmaple_os
################################################################################