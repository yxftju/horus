#!/usr/bin/python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------#
#                                                                       #
# This file is part of the Horus Project                                #
#                                                                       #
# Copyright (C) 2014 Mundo Reader S.L.                                  #
#                                                                       #
# Date: March 2014                                                      #
# Author: Carlos Crespo <carlos.crespo@bq.com>                          #
#                                                                       #
# This program is free software: you can redistribute it and/or modify  #
# it under the terms of the GNU General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or     #
# (at your option) any later version.                                   #
#                                                                       #
# This program is distributed in the hope that it will be useful,       #
# but WITHOUT ANY WARRANTY; without even the implied warranty of        #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the          #
# GNU General Public License for more details.                          #
#                                                                       #
# You should have received a copy of the GNU General Public License     #
# along with this program. If not, see <http://www.gnu.org/licenses/>.  #
#                                                                       #
#-----------------------------------------------------------------------#

__author__ = u"Carlos Crespo <carlos.crespo@bq.com>"
__license__ = u"GNU General Public License v3 http://www.gnu.org/licenses/gpl.html"

import cv2
import numpy as np
import copy


class Calibration:
	"""Calibration class. For managing calibration"""
	def __init__(self, parent):


		self._calMatrix=np.array([[  1.39809096e+03  , 0.00000000e+00 ,  4.91502299e+02], [  0.00000000e+00 ,  1.43121118e+03  , 6.74406283e+02], [  0.00000000e+00 ,  0.00000000e+00  , 1.00000000e+00]])
		self._calMatrixDefault=np.array([[  1.39809096e+03  , 0.00000000e+00 ,  4.91502299e+02], [  0.00000000e+00 ,  1.43121118e+03  , 6.74406283e+02], [  0.00000000e+00 ,  0.00000000e+00  , 1.00000000e+00]])
		
		self._distortionVector= np.array([ 0.11892648 ,-0.24087801 , 0.01288427 , 0.00628766 , 0.01007653])
		self._distortionVectorDefault= np.array([ 0.11892648 ,-0.24087801 , 0.01288427 , 0.00628766 , 0.01007653])
		
		self._rotMatrix=np.array([[ 0.99970814 , 0.02222752 ,-0.00946474], [ 0.00930233 , 0.00739852 , 0.99992936],[ 0.02229597, -0.99972556 , 0.00718959]])
		self._rotMatrixDefault=np.array([[ 0.99970814 , 0.02222752 ,-0.00946474], [ 0.00930233 , 0.00739852 , 0.99992936],[ 0.02229597, -0.99972556 , 0.00718959]])
		
		self._transMatrix=np.array([[  -5.56044557],[  73.33950448], [ 328.54553044]])
		self._transMatrixDefault=np.array([[  -5.56044557],[  73.33950448], [ 328.54553044]])
		
		print "calibreision"
	def solvePnp(self):
		print "solfpenepe"
	def calibrationFromImages(self,images):
		print "calibreision from imeichs"
	def detectPrintChessboard(self,image):
		print "detect and print chessbour"
		gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
		retval,corners=cv2.findChessboardCorners(gray,(self.patternColumns,self.patternRows))
		if retval:
			cv2.cornerSubPix(gray,corners,winSize=(11,11),zeroZone=(-1,-1),criteria=self.criteria)
			
		return image