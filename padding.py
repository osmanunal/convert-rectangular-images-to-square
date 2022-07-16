import glob
import os
import cv2

# Create directory - dizin oluşturma 
os.mkdir("new_imgs")

imgs_paths = glob.glob("./imgs/*")   # imgs--> directory with my images - resimlerimin olduğu dizin

for img_path in imgs_paths : 
    
    img_name = os.path.basename(img_path) 
    frame = cv2.imread(f"./imgs/{img_name}")

    height = frame.shape[0]
    width = frame.shape[1]

    if height>width : 
        add_ = int((height-width)/2)
        new_frame = cv2.copyMakeBorder(frame, 0,0,add_,add_,cv2.BORDER_CONSTANT, (0,0,0)) #arg 2,3,4 --> top, bottom, left, right 
    
        cv2.imwrite(f"./new_imgs/new_{img_name}",new_frame)
        
    elif width> height :
        add_ = int((width-height)/2)
        new_frame = cv2.copyMakeBorder(frame, add_,add_,0,0,cv2.BORDER_CONSTANT, (0,0,0))
    
        cv2.imwrite(f"./new_imgs/new_{img_name}",new_frame)
    else : 
        cv2.imwrite(f"./new_imgs/new_{img_name}",frame)


cv2.waitKey(0)
cv2.destroyAllWindows()
