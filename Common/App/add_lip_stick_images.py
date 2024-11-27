import random
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy


def add_lip_stick_images(wait):
    loop_count = random.randint(2, 3)

    for img_loop in range(loop_count):
        try:
            add_image_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, '+')))
            add_image_btn.click()
        except Exception as e:
            print('There has been an error in clicking the "+" icon.\n', e)
         
        try:               
            galery_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, ', Abrir galeria')))
            galery_opt.click()
        except Exception as e:
            print('There has been an error in openning the Galery".\n', e)
                       
        try:
            album_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Álbuns')))
            album_opt.click()
        except Exception as e:
            print('There has been an error in openning the Álbuns.\n', e)
        
        try:
            download_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Downloads")')))
            download_opt.click()         
        except Exception as e:
            print('Error in clicking the "Download" option.\n', e)
            
        try:                                                       
            image = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().resourceId("com.google.android.providers.media.module:id/icon_thumbnail").instance({img_loop+1})')))
            image.click()
        except Exception as e:
            print(f'There has been an error in openning image "{loop_count+1}".\n', e)
            
        img_loop += 1
        
def add_color_image(wait):
    try:
        add_image_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, '+')))
        add_image_btn.click()
    except Exception as e:
        print('There has been an error in clicking the "+" icon.\n', e)
     
    try:               
        galery_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, ', Abrir galeria')))
        galery_opt.click()
    except Exception as e:
        print('There has been an error in openning the Galery".\n', e)
                   
    try:
        album_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Álbuns')))
        album_opt.click()
    except Exception as e:
        print('There has been an error in openning the Álbuns.\n', e)
    
    try:
        download_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Downloads")')))
        download_opt.click()         
    except Exception as e:
        print('Error in clicking the "Download" option.\n', e)
                
    try:                                           
        image = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.google.android.providers.media.module:id/icon_thumbnail").instance(0)')))
        image.click()
    except Exception as e:
        print('Error in openning the color image.\n', e)
        
        
def add_lip_stick_images_promotor(wait):
    loop_count = random.randint(2, 3)

    for img_loop in range(loop_count):
        try:
            add_image_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, '')))
            add_image_btn.click()
        except Exception as e:
            print('There has been an error in clicking the "" icon.\n', e)
         
        try:               
            galery_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, ', Abrir galeria')))
            galery_opt.click()
        except Exception as e:
            print('There has been an error in openning the Galery".\n', e)
                       
        try:
            album_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Álbuns')))
            album_opt.click()
        except Exception as e:
            print('There has been an error in openning the Álbuns.\n', e)
        
        try:
            download_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Downloads")')))
            download_opt.click()         
        except Exception as e:
            print('Error in clicking the "Download" option.\n', e)
            
        try:                                                       
            image = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().resourceId("com.google.android.providers.media.module:id/icon_thumbnail").instance({img_loop+1})')))
            image.click()
        except Exception as e:
            print(f'There has been an error in openning image "{loop_count+1}".\n', e)
            
        img_loop += 1
        
def add_color_image_promotor(wait):
    try:
        add_image_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, '')))
        add_image_btn.click()
    except Exception as e:
        print('There has been an error in clicking the "+" icon.\n', e)
     
    try:               
        galery_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, ', Abrir galeria')))
        galery_opt.click()
    except Exception as e:
        print('There has been an error in openning the Galery".\n', e)
                   
    try:
        album_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Álbuns')))
        album_opt.click()
    except Exception as e:
        print('There has been an error in openning the Álbuns.\n', e)
    
    try:
        download_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Downloads")')))
        download_opt.click()         
    except Exception as e:
        print('Error in clicking the "Download" option.\n', e)
                
    try:                                           
        image = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.google.android.providers.media.module:id/icon_thumbnail").instance(0)')))
        image.click()
    except Exception as e:
        print('Error in openning the color image.\n', e)
    