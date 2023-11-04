from ultralytics import YOLO
import csv

model = YOLO('yolov8m.pt')

results = model.track(
	source='C:/Users/rodri/Desktop/TCC/archive', 
	show=True, 
	save=True,
	save_dir='C:/Users/rodri/Desktop/TCC/runs', 
	tracker='bytetrack.yaml',
	classes=(2,3,5,7)
	#0: person
	#1: bicycle
	#2: car
	#3: motorcycle
	#4: airplane
	#5: bus
	#6: train
	#7: truck
	#8: boat
)


























