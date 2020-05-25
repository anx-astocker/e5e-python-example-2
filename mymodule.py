import os
import sys

from mydata import IMG_CONTENT_TYPE, IMG_DATA


def myfunction(event, context):
    return {
        'type': 'binary',
        'status': 200,
        'response_headers': {
            'Content-Type': IMG_CONTENT_TYPE,
        },
    	'data': IMG_DATA,
    }

