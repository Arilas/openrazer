"""
Mug class
"""
import re

from openrazer_daemon.hardware.device_base import RazerDeviceBrightnessSuspend as _RazerDeviceBrightnessSuspend


class RazerChromaMugHolder(_RazerDeviceBrightnessSuspend):
    """
    Class for the Razer Chroma Mug Holder
    """
    EVENT_FILE_REGEX = re.compile(r'.*Razer_Chroma_Mug_Holder-if0(1|2)-event-kbd')

    USB_VID = 0x1532
    USB_PID = 0x0F07
    HAS_MATRIX = True
    MATRIX_DIMS = [1, 15]
    METHODS = ['get_device_type_accessory',
               'set_static_effect', 'set_spectrum_effect', 'set_wave_effect', 'set_none_effect', 'set_breath_single_effect', 'set_breath_dual_effect', 'set_breath_random_effect', 'set_blinking_effect',
               'is_mug_present',
               'set_custom_effect', 'set_key_row']

    DEVICE_IMAGE = "https://assets2.razerzone.com/images/mug-holder/e64e507b73e61c44789d996065fd9645-1500x1000mug_01.jpg"

    # Deprecated - RAZER_URLS be removed in future.
    RAZER_URLS = {
        "top_img": "https://assets2.razerzone.com/images/mug-holder/e64e507b73e61c44789d996065fd9645-1500x1000mug_01.jpg",
        "perspective_img": "https://assets2.razerzone.com/images/mug-holder/e64e507b73e61c44789d996065fd9645-1500x1000mug_01.jpg"
    }


class RazerChromaHDK(_RazerDeviceBrightnessSuspend):
    """
    Class for the Razer Chroma Hardware Development Kit (HDK)
    """
    USB_VID = 0x1532
    USB_PID = 0x0F09
    HAS_MATRIX = True
    MATRIX_DIMS = [4, 16]
    METHODS = ['get_device_type_accessory', 'set_static_effect', 'set_wave_effect', 'set_spectrum_effect',
               'set_none_effect', 'set_breath_random_effect', 'set_breath_single_effect', 'set_breath_dual_effect',
               'set_custom_effect', 'set_key_row']

    DEVICE_IMAGE = "https://assets2.razerzone.com/images/chromahdk2017/788b689d471fedbc0c5a175592316657-gallery-08.jpg"

    # Deprecated - RAZER_URLS be removed in future.
    RAZER_URLS = {
        "top_img": "https://assets2.razerzone.com/images/chromahdk2017/788b689d471fedbc0c5a175592316657-gallery-08.jpg"
    }


class RazerBaseStationChroma(_RazerDeviceBrightnessSuspend):
    """
    Class for the Razer Base Station Chroma (Headphone Stand)
    """
    USB_VID = 0x1532
    USB_PID = 0x0F08
    HAS_MATRIX = True
    MATRIX_DIMS = [1, 15]
    METHODS = ['get_device_type_accessory', 'set_static_effect', 'set_wave_effect', 'set_spectrum_effect',
               'set_none_effect', 'set_breath_random_effect', 'set_breath_single_effect', 'set_breath_dual_effect',
               'set_custom_effect', 'set_key_row']

    DEVICE_IMAGE = "https://rzrwarranty.s3.amazonaws.com/145dcc47f9f9d33b0bd07b066364704160f45e87b756d690b203decec7d1e87c.png"

    # Deprecated - RAZER_URLS be removed in future.
    RAZER_URLS = {
        "top_img": DEVICE_IMAGE
    }


class RazerMouseDock(RazerBaseStationChroma):
    HAS_MATRIX = False
    USB_PID = 0x007E
    EVENT_FILE_REGEX = re.compile(r'.*Razer_Mouse_Dock-if0(1|2)-event-kbd')
    METHODS = ['get_device_type_accessory', 'set_static_effect', 'set_spectrum_effect', 'set_brightness',
               'set_none_effect', 'set_breath_random_effect', 'set_breath_single_effect', 'set_breath_dual_effect',
               'set_custom_effect', 'set_key_row']


class RazerNommoChroma(_RazerDeviceBrightnessSuspend):
    """
    Class for the Razer Nommo Chroma (Speakers)
    """
    USB_VID = 0x1532
    USB_PID = 0x0517
    HAS_MATRIX = True
    MATRIX_DIMS = [2, 24]
    METHODS = ['get_device_type_accessory', 'set_static_effect', 'set_wave_effect', 'set_spectrum_effect',
               'set_none_effect', 'set_breath_random_effect', 'set_breath_single_effect', 'set_breath_dual_effect',
               'set_custom_effect', 'set_key_row']

    DEVICE_IMAGE = "https://d4kkpd69xt9l7.cloudfront.net/sys-master/root/he6/h1a/8939927175198/nommo-gallery-1500x1000-11.jpg"

    # Deprecated - RAZER_URLS be removed in future.
    RAZER_URLS = {
        "top_img": DEVICE_IMAGE
    }


class RazerNommoPro(_RazerDeviceBrightnessSuspend):
    """
    Class for the Razer Nommo Pro (Speakers)
    """
    USB_VID = 0x1532
    USB_PID = 0x0518
    HAS_MATRIX = True
    MATRIX_DIMS = [2, 8]
    METHODS = ['get_device_type_accessory', 'set_static_effect', 'set_wave_effect', 'set_spectrum_effect',
               'set_none_effect', 'set_breath_random_effect', 'set_breath_single_effect', 'set_breath_dual_effect',
               'set_custom_effect', 'set_key_row']

    DEVICE_IMAGE = "https://d4kkpd69xt9l7.cloudfront.net/sys-master/root/h89/hc4/9003754717214/razer-nommo-pro-audio-04.jpg"

    # Deprecated - RAZER_URLS be removed in future.
    RAZER_URLS = {
        "top_img": DEVICE_IMAGE
    }
