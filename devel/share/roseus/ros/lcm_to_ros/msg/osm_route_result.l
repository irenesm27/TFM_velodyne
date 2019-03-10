;; Auto-generated. Do not edit!


(when (boundp 'lcm_to_ros::osm_route_result)
  (if (not (find-package "LCM_TO_ROS"))
    (make-package "LCM_TO_ROS"))
  (shadow 'osm_route_result (find-package "LCM_TO_ROS")))
(unless (find-package "LCM_TO_ROS::OSM_ROUTE_RESULT")
  (make-package "LCM_TO_ROS::OSM_ROUTE_RESULT"))

(in-package "ROS")
;;//! \htmlinclude osm_route_result.msg.html


(defclass lcm_to_ros::osm_route_result
  :super ros::object
  :slots (_id _n_puntos _puntos ))

(defmethod lcm_to_ros::osm_route_result
  (:init
   (&key
    ((:id __id) 0)
    ((:n_puntos __n_puntos) 0)
    ((:puntos __puntos) (let (r) (dotimes (i 0) (push (instance lcm_to_ros::osm_waypoint :init) r)) r))
    )
   (send-super :init)
   (setq _id (round __id))
   (setq _n_puntos (round __n_puntos))
   (setq _puntos __puntos)
   self)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:n_puntos
   (&optional __n_puntos)
   (if __n_puntos (setq _n_puntos __n_puntos)) _n_puntos)
  (:puntos
   (&rest __puntos)
   (if (keywordp (car __puntos))
       (send* _puntos __puntos)
     (progn
       (if __puntos (setq _puntos (car __puntos)))
       _puntos)))
  (:serialization-length
   ()
   (+
    ;; int32 _id
    4
    ;; int32 _n_puntos
    4
    ;; lcm_to_ros/osm_waypoint[] _puntos
    (apply #'+ (send-all _puntos :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _id
       (write-long _id s)
     ;; int32 _n_puntos
       (write-long _n_puntos s)
     ;; lcm_to_ros/osm_waypoint[] _puntos
     (write-long (length _puntos) s)
     (dolist (elem _puntos)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _id
     (setq _id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _n_puntos
     (setq _n_puntos (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; lcm_to_ros/osm_waypoint[] _puntos
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _puntos (let (r) (dotimes (i n) (push (instance lcm_to_ros::osm_waypoint :init) r)) r))
     (dolist (elem- _puntos)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get lcm_to_ros::osm_route_result :md5sum-) "1e17e3fc432d0f2c2a93661fa8d61a75")
(setf (get lcm_to_ros::osm_route_result :datatype-) "lcm_to_ros/osm_route_result")
(setf (get lcm_to_ros::osm_route_result :definition-)
      "#######################################################################
# This message was automatically generated by the lcm_to_ros package
# https://github.com/nrjl/lcm_to_ros, nicholas.lawrance@oregonstate.edu
#######################################################################
#
# Source message:    .msg
# Creation:          lun 18 feb 2019 17:14:17 CET
#
#######################################################################
int32               id
int32               n_puntos
osm_waypoint[]      puntos

================================================================================
MSG: lcm_to_ros/osm_waypoint
#######################################################################
# This message was automatically generated by the lcm_to_ros package
# https://github.com/nrjl/lcm_to_ros, nicholas.lawrance@oregonstate.edu
#######################################################################
#
# Source message:    .msg
# Creation:          lun 18 feb 2019 17:14:17 CET
#
#######################################################################
float64             latitud
float64             longitud
float64             orientacion

")



(provide :lcm_to_ros/osm_route_result "1e17e3fc432d0f2c2a93661fa8d61a75")

