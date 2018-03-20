#!/usr/bin/env python

import sys
sys.path.append('/usr/share/inkscape/extensions')

# Purge short lines
# This script is designed to be used to clean up/simplify 2D vector exports from
# SketchUp. It ignores everything but paths between exactly 2 points.

import inkex
import math
from simplestyle import *

debug = False

class EnerothPurgeShortEdges(inkex.Effect):
  def __init__(self):
    inkex.Effect.__init__(self)
    self.OptionParser.add_option('-w', '--length', action = 'store',
      type = 'float', dest = 'length', default = 10.0)

  def effect(self):
    length = self.options.length
    svg = self.document.getroot()

    if len(self.selected)==0:
      self.iterate_node(self.document.getroot())
    else:
      for id, node in self.selected.iteritems():
        self.iterate_node(node)

  def iterate_node(self, node):
    self.do_node(node)
    for child in node:
      self.iterate_node(child)

  def do_node(self, node):
    if node.attrib.has_key('d'):
      points = []

      instruction = None
      prev_coords = None

      words = node.get('d').split(' ')
      for i, word in enumerate(words):
        if len(word) == 1:
          instruction = word
        else:
          coords = map(lambda c: float(c), word.split(','))
          if instruction.lower() == instruction:
            coords[0] += prev_coords[0]
            coords[1] += prev_coords[1]
          prev_coords = coords
          # Assume all coordinates are points of straight lines (instructor being M, m, L or l)
          points.append(coords)

      if len(points) == 2:
        length = math.sqrt((points[0][0]-points[1][0])**2 + (points[0][1]-points[1][1])**2)
        if debug:
          inkex.debug(length)
        if length < self.options.length:
          node.getparent().remove(node)

EnerothPurgeShortEdges().affect()
