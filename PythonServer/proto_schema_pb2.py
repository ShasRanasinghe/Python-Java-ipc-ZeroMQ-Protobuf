# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto_schema.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto_schema.proto',
  package='TORCS_Sensors',
  syntax='proto2',
  serialized_options=_b('B\017Sensors_Message'),
  serialized_pb=_b('\n\x12proto_schema.proto\x12\rTORCS_Sensors\"\x9d\x03\n\x07Sensors\x12\r\n\x05\x61\x63\x63\x65l\x18\x01 \x01(\x02\x12\x10\n\x08\x62reaking\x18\x02 \x01(\x02\x12\x0c\n\x04gear\x18\x03 \x01(\x05\x12\r\n\x05steer\x18\x04 \x01(\x02\x12\x0c\n\x04meta\x18\x05 \x01(\x05\x12\x0e\n\x06\x63lutch\x18\x06 \x01(\x02\x12\r\n\x05\x66ocus\x18\x07 \x01(\x05\x12\r\n\x05\x61ngle\x18\x08 \x01(\x02\x12\x11\n\tcuLapTime\x18\t \x01(\x02\x12\x0e\n\x06\x64\x61mage\x18\n \x01(\x05\x12\x15\n\rdistFromStart\x18\x0b \x01(\x02\x12\x1a\n\x12totalDistFromStart\x18\x0c \x01(\x02\x12\x11\n\tdistRaced\x18\r \x01(\x02\x12\x0c\n\x04\x66uel\x18\x0e \x01(\x02\x12\x13\n\x0blastLapTime\x18\x0f \x01(\x02\x12\x0f\n\x07racePos\x18\x10 \x01(\x05\x12\x0b\n\x03rpm\x18\x11 \x01(\x02\x12\x0e\n\x06speedX\x18\x12 \x01(\x02\x12\x0e\n\x06speedY\x18\x13 \x01(\x02\x12\x0e\n\x06speedZ\x18\x14 \x01(\x02\x12\x14\n\x0c\x64istToMiddle\x18\x15 \x01(\x02\x12\x0c\n\x04posZ\x18\x16 \x01(\x02\x12\x0b\n\x03\x66ps\x18\x17 \x01(\x02\x12\r\n\x05\x63ount\x18\x18 \x01(\x05\x42\x11\x42\x0fSensors_Message')
)




_SENSORS = _descriptor.Descriptor(
  name='Sensors',
  full_name='TORCS_Sensors.Sensors',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='accel', full_name='TORCS_Sensors.Sensors.accel', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='breaking', full_name='TORCS_Sensors.Sensors.breaking', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gear', full_name='TORCS_Sensors.Sensors.gear', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='steer', full_name='TORCS_Sensors.Sensors.steer', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meta', full_name='TORCS_Sensors.Sensors.meta', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clutch', full_name='TORCS_Sensors.Sensors.clutch', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='focus', full_name='TORCS_Sensors.Sensors.focus', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angle', full_name='TORCS_Sensors.Sensors.angle', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cuLapTime', full_name='TORCS_Sensors.Sensors.cuLapTime', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='damage', full_name='TORCS_Sensors.Sensors.damage', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distFromStart', full_name='TORCS_Sensors.Sensors.distFromStart', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalDistFromStart', full_name='TORCS_Sensors.Sensors.totalDistFromStart', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distRaced', full_name='TORCS_Sensors.Sensors.distRaced', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fuel', full_name='TORCS_Sensors.Sensors.fuel', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastLapTime', full_name='TORCS_Sensors.Sensors.lastLapTime', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='racePos', full_name='TORCS_Sensors.Sensors.racePos', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rpm', full_name='TORCS_Sensors.Sensors.rpm', index=16,
      number=17, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='speedX', full_name='TORCS_Sensors.Sensors.speedX', index=17,
      number=18, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='speedY', full_name='TORCS_Sensors.Sensors.speedY', index=18,
      number=19, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='speedZ', full_name='TORCS_Sensors.Sensors.speedZ', index=19,
      number=20, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distToMiddle', full_name='TORCS_Sensors.Sensors.distToMiddle', index=20,
      number=21, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='posZ', full_name='TORCS_Sensors.Sensors.posZ', index=21,
      number=22, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fps', full_name='TORCS_Sensors.Sensors.fps', index=22,
      number=23, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='TORCS_Sensors.Sensors.count', index=23,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=451,
)

DESCRIPTOR.message_types_by_name['Sensors'] = _SENSORS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Sensors = _reflection.GeneratedProtocolMessageType('Sensors', (_message.Message,), dict(
  DESCRIPTOR = _SENSORS,
  __module__ = 'proto_schema_pb2'
  # @@protoc_insertion_point(class_scope:TORCS_Sensors.Sensors)
  ))
_sym_db.RegisterMessage(Sensors)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
