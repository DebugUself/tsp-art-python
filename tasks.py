# -*- coding: utf-8 -*-
'''PoL<-PoW
'''
__version__ = 'TSPart v.200716.1542'
__author__ = 'Zoom.Quiet'
__license__ = 'MIT@2020-07'

import os
#import sys
import os.path as osp

import time
import subprocess

from pprint import pprint as pp
#from textwrap import dedent as dedentxt
import sys
import platform
os_name = platform.system()
del platform


from invoke import task

import draw_tsp_path as drawtp

#_IMG='images'

@task 
def V(c):
    '''Version and how to usage
    '''
    #print('\n\t powded by {}'.format(__version__))
    print( "\n$ inv -l show all support commands \n\tpowered by <-{}->\n".format(__version__) )

@task 
def tsp(c, img, npoints):
    '''got images/THE IMAGE and gen the TSP-art need picture
    '''
    #print(img, npoints)
    _cmd = 'python weighted-voronoi-stippler/stippler.py '
    _cmd += img
    _cmd += ' --save '
    _cmd += '--n_point %s '%npoints
    _cmd += '--n_iter 25 '
    _cmd += '--pointsize 1.0 1.0 '
    _cmd += '--figsize 8 '
    _cmd += '--threshold 255 '
    _cmd += '--force '
    _cmd += '--interactive '
    _cmd += '--png '
    #print(_cmd)
    c.run(_cmd)

    dirname = os.path.dirname(img)
    basename = (os.path.basename(img).split('.'))[0]
    #print(img)
    #print(dirname,basename)
    _stippled = '{}/{}-{}-stipple'.format(dirname,basename,npoints)
    #print(_stippled)
    drawtp.ORIGINAL_IMAGE = '%s.png'%_stippled
    drawtp.IMAGE_TSP = '%s.tsp'%_stippled
    #print(drawtp.ORIGINAL_IMAGE)
    #print(drawtp.IMAGE_TSP)
    drawtp.main()
    _tsp = '{}/{}-{}-tsp.png'.format(dirname,basename,npoints)




