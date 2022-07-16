# convert-rectangular-images-to-square
dikdörtgen resimleri kareye çevirme işlemi

CNN modelini eğitirken görüntüleri kare formatta yeniden boyutlandırılması istenir.(örneğin, ResNet'in input_shape= 224x224 kare bir görüntü alır) 
Bu yüzden resimi yeniden boyutlandırma yaparken bozulmaları önlemek için ön işlem olarak siyah pikseller ekleyip kare formata getirilir.    
Sıfır pikselli alanlar için evrişim işleminin çıktısı sıfırdır. Yani bu işlem ağırlıkları etkilemeyecektir.
