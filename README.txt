for running the code, first need to download files: butterfly.mp4 and yolov3_for_butterflies.weights from https://drive.google.com/drive/folders/1nn73QBXyBzLpQwoiEZNDjXk-r8iLiFhW?usp=sharing

and then run butterfly_test.py

My logic-flow of doing prompt1:

1 Fine some butterfly photo from Kaggle and label them.

->2 using the data to funtine a yolo model to make it be able to detect bufferfly

->3 use the model to detect the location of each bufferfly

->4 use KCF tracking algorithms to track each detected butterfly

->5 for each some seconds go back to step 3 to renew the detection

If a butterfly lost track, it means it fly away (frame out).
If a new butterfly get detected during the new detection, it means it fly in (frame in).

 But the performance is very bad for both yolo-model and KCF tracking algorithms.
I guess there are sereval reasons:

1, The yolo model is not well trained.
2, Yolo model is 'too big' , yolo tiny may be better for this task.
3, Yolo model not suitable for this task since yolo is good for muti-objects detection but the task only need to detect one type of object.
4, KCF tracking is not good for track objects that will 'change shape'.(butterfly change shape during it "拍翼")( I didn't know the reason yet, I just google it and assume it is true) 

so, If I can do this task(or similar task/ task that only detection one type of object) again, I will try just use a tracking algorithm.



I did not do prompt2 (sorry for the lady that record the sound track) since I suggle to do prompt1 :(
but I can share the logic-flow if I do the task (similar to prompt1):

1 Use the pretrained auto-speech-recognition model to "convert" the sound track to sequence of text.
2 count how many pa ta ka in the sequence of text.
