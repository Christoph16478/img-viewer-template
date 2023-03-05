#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""generate html code for image display"""

import os

target_dir = "images"

with open ('html_pic_code.txt', 'w', encoding='utf-8') as file:
    file.write('<!-- generatedCode -->')
    for filename in os.listdir(target_dir):
        if not 'usa-flag.png' in filename:
            file.write(f'<img class="rounded mx-auto d-block img-fluid" src="images/{filename}"/><br>\n\n')
    file.write('<!-- /generatedCode -->')        