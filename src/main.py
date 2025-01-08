from pydicom import dcmread

from src.utils.pacs import DCMDataset
from pydicom.dataset import Dataset
import pacs

def find_studies():
    ds_dict = {
        'PatientName': '',
        'PatientID': '',
        'Modality':'',
        'StudyInstanceUID': '',
        'StudyDescription': '',
        'StudyDate': '',
        'QueryRetrieveLevel': 'STUDY'
    }

    ds = DCMDataset.create(ds_dict)

    result = pacs.find_studies(ds)
    print (result)



def run():
    # dicom_path = 'dicom_files/example/PM5644-960x540_RGB.dcm'
    # dicom_path = 'dicom_files/example_private/1.2.826.1.101009.947164870.1657604110.20250106100248/1.2.826.0.1.3680043.9.6965.1434327336.792316737.806139171/1.2.826.0.1.3680043.9.6965.1434327336.540312631.1182125904.dcm'
    # dicom_path = 'dicom_files/example_private/1.2.826.1.101009.947164870.1657604110.20250106100248/1.2.826.0.1.3680043.9.6965.1434327336.445349832.1434192875/1.2.826.0.1.3680043.9.6965.1434327336.444547519.1436781289.dcm'
    # dicom_path = 'dicom_files/example_private/1.2.826.1.101009.947164870.1657604110.20250106100248/1.2.826.0.1.3680043.9.6965.1434327336.509243701.1254247338/1.2.826.0.1.3680043.9.6965.1434327336.483094607.1322137624.dcm'
    # dicom_path = 'dicom_files/large_example/Anonymized_20250108/series-00000/image-00001.dcm'
    # dicom_path = 'dicom_files/large_example/series-00000/image-00000.dcm'
    # dicom = dcmread(dicom_path)
    # status = pacs.store_dcm(dicom)
    # print (status)


    find_studies()

if __name__ == '__main__':
    run()