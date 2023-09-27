import dotenv
import pydantic_settings
from typing import Literal
from appium.options.android import UiAutomator2Options
from wikipedia_android_app_tests.utils.path_helper import path_form


class Config(pydantic_settings.BaseSettings):
    context: Literal['local_emulator', 'local_real', 'bstack'] = 'bstack'

    if context == 'bstack':
        dotenv.load_dotenv(dotenv_path=path_form('.env.credentials'))

    timeout: str = '15.0'

    browserstack_username: str = ''
    browserstack_accesskey: str = ''
    remote_url: str = 'http://hub.browserstack.com/wd/hub'
    app: str = 'bs://101bf2d9af58af67bce615be3b269b705b71dc5f'
    project_name: str = 'Mobile Tests Lesson 2'
    build_name: str = 'browserstack-build-2'
    session_name: str = 'BStack test'
    android_version: str = '9.0'
    android_device: str = 'Google Pixel 3'

    udid: str = ''

    app_wait_activity: str = 'org.wikipedia.*'

    def to_driver_options(self):
        options = UiAutomator2Options()
        options.set_capability('appWaitActivity', self.app_wait_activity)

        if self.context == 'bstack':
            options.set_capability('app', self.app)
            options.load_capabilities({
                'platformVersion': self.android_version,
                'deviceName': self.android_device,

                'bstack:options': {
                    'projectName': self.project_name,
                    'buildName': self.build_name,
                    'sessionName': self.session_name,
                    'userName': self.browserstack_username,
                    'accessKey': self.browserstack_accesskey
                }
            })

        else:
            options.set_capability('app', path_form(self.app))
            options.set_capability('udid', self.udid)

        return options


config = Config(_env_file=dotenv.find_dotenv(f'.env.{Config().context}'))
