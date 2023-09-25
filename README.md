# wikipedia_android_app_tests

## Android Mobile tests configured to be run on BrowserStack/Local real Device/Local Emulator

### Common precondition:
Put the [wikipedia .apk](https://github.com/wikimedia/apps-android-wikipedia/releases/download/latest/app-alpha-universal-release.apk) to the root folder of the project

### For run on bstack:
1. Have an acc on bstack 
2. Configure .env.credentials file
3. Configure .env.bstack file according to way you are going to run tests
4. Run test in terminal using command like 'context=bstack pytest'

### For local run:
1. Install and run emulator/connect to PC and configure real device 
2. Install Java SDK, Appium server
3. Start appium server using command like 'appium' 
4. Configure .env.local_<> file according to way you are going to run tests
5. Run test in terminal using command like 'context=local_real pytest' or 'context=local_emulator pytest'
