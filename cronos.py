
import os
import ezgmail

vasometrics_path = "v:\\Vasometrics"
clinic_list = os.listdir(vasometrics_path)

for clinic in clinic_list:
    #### Skip these files/directories
    if clinic == "Vasometrics Archive":
        continue  # skips



    clinic_object_list = os.listdir(os.path.join(vasometrics_path,clinic))
    clinic_path = os.path.join(vasometrics_path, clinic)
    print("Clinic '{}':".format(clinic))
    for object in  clinic_object_list:
        if object == "Processed Studies":
            continue

        object_path = os.path.join(clinic_path,object)
        print("\t{}".format(object_path))