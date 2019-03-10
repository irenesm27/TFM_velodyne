# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from lcm_to_ros/warnings_coche.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class warnings_coche(genpy.Message):
  _md5sum = "d63e4b099b36145ebd6de918f9a6bd94"
  _type = "lcm_to_ros/warnings_coche"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """#######################################################################
# This message was automatically generated by the lcm_to_ros package
# https://github.com/nrjl/lcm_to_ros, nicholas.lawrance@oregonstate.edu
#######################################################################
#
# Source message:    .msg
# Creation:          lun 18 feb 2019 17:14:17 CET
#
#######################################################################
int8                tipo_obs
float64             longitud
float64             latitud
float64             velocidad
"""
  __slots__ = ['tipo_obs','longitud','latitud','velocidad']
  _slot_types = ['int8','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       tipo_obs,longitud,latitud,velocidad

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(warnings_coche, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.tipo_obs is None:
        self.tipo_obs = 0
      if self.longitud is None:
        self.longitud = 0.
      if self.latitud is None:
        self.latitud = 0.
      if self.velocidad is None:
        self.velocidad = 0.
    else:
      self.tipo_obs = 0
      self.longitud = 0.
      self.latitud = 0.
      self.velocidad = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_b3d().pack(_x.tipo_obs, _x.longitud, _x.latitud, _x.velocidad))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 25
      (_x.tipo_obs, _x.longitud, _x.latitud, _x.velocidad,) = _get_struct_b3d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_b3d().pack(_x.tipo_obs, _x.longitud, _x.latitud, _x.velocidad))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 25
      (_x.tipo_obs, _x.longitud, _x.latitud, _x.velocidad,) = _get_struct_b3d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_b3d = None
def _get_struct_b3d():
    global _struct_b3d
    if _struct_b3d is None:
        _struct_b3d = struct.Struct("<b3d")
    return _struct_b3d