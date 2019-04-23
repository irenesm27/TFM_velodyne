// Auto-generated. Do not edit!

// (in-package lcm_to_ros.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class warnings_coche {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.tipo_obs = null;
      this.longitud = null;
      this.latitud = null;
      this.velocidad = null;
    }
    else {
      if (initObj.hasOwnProperty('tipo_obs')) {
        this.tipo_obs = initObj.tipo_obs
      }
      else {
        this.tipo_obs = 0;
      }
      if (initObj.hasOwnProperty('longitud')) {
        this.longitud = initObj.longitud
      }
      else {
        this.longitud = 0.0;
      }
      if (initObj.hasOwnProperty('latitud')) {
        this.latitud = initObj.latitud
      }
      else {
        this.latitud = 0.0;
      }
      if (initObj.hasOwnProperty('velocidad')) {
        this.velocidad = initObj.velocidad
      }
      else {
        this.velocidad = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type warnings_coche
    // Serialize message field [tipo_obs]
    bufferOffset = _serializer.int8(obj.tipo_obs, buffer, bufferOffset);
    // Serialize message field [longitud]
    bufferOffset = _serializer.float64(obj.longitud, buffer, bufferOffset);
    // Serialize message field [latitud]
    bufferOffset = _serializer.float64(obj.latitud, buffer, bufferOffset);
    // Serialize message field [velocidad]
    bufferOffset = _serializer.float64(obj.velocidad, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type warnings_coche
    let len;
    let data = new warnings_coche(null);
    // Deserialize message field [tipo_obs]
    data.tipo_obs = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [longitud]
    data.longitud = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [latitud]
    data.latitud = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [velocidad]
    data.velocidad = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 25;
  }

  static datatype() {
    // Returns string type for a message object
    return 'lcm_to_ros/warnings_coche';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd63e4b099b36145ebd6de918f9a6bd94';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    #######################################################################
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new warnings_coche(null);
    if (msg.tipo_obs !== undefined) {
      resolved.tipo_obs = msg.tipo_obs;
    }
    else {
      resolved.tipo_obs = 0
    }

    if (msg.longitud !== undefined) {
      resolved.longitud = msg.longitud;
    }
    else {
      resolved.longitud = 0.0
    }

    if (msg.latitud !== undefined) {
      resolved.latitud = msg.latitud;
    }
    else {
      resolved.latitud = 0.0
    }

    if (msg.velocidad !== undefined) {
      resolved.velocidad = msg.velocidad;
    }
    else {
      resolved.velocidad = 0.0
    }

    return resolved;
    }
};

module.exports = warnings_coche;