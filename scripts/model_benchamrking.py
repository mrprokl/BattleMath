import os
import timeit
from ultralytics import models
import time
# import pandas as pd

def main():
    model_name_list = ["yolov3.pt","yolov5n.pt", "yolov8s.pt","yolov8n.pt", "yolov8s.pt", "yolov8m.pt", "yolov8l.pt"]
    model_list = []
    # run_times = pd.DataFrame(columns=["model","run_time"])
    model_dict = dict()

    for model in model_name_list:
        model_dict[model] = models.YOLO(model)

    # for model, model_obj in model_dict.values():
    #     print(model)

    results = []
    results_dict = dict()
    for model, model_obj in model_dict.items():
        t0 = time.time()
        # results = model.predict("https://ultralytics.com/images/bus.jpg", save=True)
        results.append(model_obj.predict(["images/testing.jpg","images/testing.jpg","images/testing.jpg","images/testing.jpg","images/testing.jpg","images/testing.jpg","images/testing.jpg","images/testing.jpg","images/testing.jpg","images/testing.jpg","images/testing.jpg"],
                                     save=True))
        results_dict[model_obj.info()] = results[-1]
        print("##############################################")
        print(f"Model {model} took {time.time() - t0} seconds")
        print(f"Model {model} has params {model_obj.info()}")
        print("##############################################")

if __name__ == "__main__":
    main()
