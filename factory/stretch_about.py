#!/usr/bin/env python

import os
import yaml
import cv2

image_file = "../images/stretch_about.png"
image = cv2.imread(image_file)

factory_params_filename = os.environ['HELLO_FLEET_PATH']+'/'+os.environ['HELLO_FLEET_ID']+'/stretch_re1_factory_params.yaml'

with open(factory_params_filename, 'r') as fid:
    factory_params = yaml.safe_load(fid)
    robot_info = factory_params['robot']
    batch_name = robot_info['batch_name']
    serial_number = robot_info['serial_no']

# Write information on the image
font = cv2.FONT_HERSHEY_SIMPLEX #cv2.FONT_HERSHEY_PLAIN
font_scale = 0.7
line_color = [0, 0, 0]
line_width = 1

batch_name_string = 'Batch Name: {0}'.format(batch_name)
serial_number_string = 'Serial Number: {0}'.format(serial_number)
color = (0, 0, 255)

# see the following page for a helpful reference
# https://stackoverflow.com/questions/51285616/opencvs-gettextsize-and-puttext-return-wrong-size-and-chop-letters-with-low

text_x = 310
text_y = 375

vertical_spacing_pix = 40

cv2.rectangle(image, (280, 333), (720, 443), (255, 255, 255), cv2.FILLED)
cv2.putText(image, batch_name_string, (text_x, text_y), font, font_scale, line_color, line_width, cv2.LINE_AA)
cv2.putText(image, serial_number_string, (text_x, text_y + vertical_spacing_pix), font, font_scale, line_color, line_width, cv2.LINE_AA)

cv2.imshow('S T R E T C H RESEARCH EDITION', image)
cv2.waitKey(0)