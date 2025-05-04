#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025

from PIL import Image

class Figure:
  """ By design, the figure data members cannot be modified.
      So objects can contain references to figures.
  """
  def __init__(self, image: Image):
    if not isinstance(image, Image.Image):
      raise TypeError('image')

    self._image= image

  @property
  def image( self):
    return self._image

#--------------------------------------------------------------------------------------------------
if __name__ == "__main__":
  pass
