from pydicom import dcmread

from src.utils.pacs import DCMDataset
from pydicom.dataset import Dataset
import pacs

def get_all_dicom():
    ds_dict = {
        'PatientName': 'Test^Pattern',
        'PatientID': 'PM5644',
        # 'StudyInstanceUID': '1.3.6.1.4.1.34261.90254037371867.41912.1553085024.2',
        'StudyInstanceUID': '1.2.826.0.1.3680043.8.498.90263342633744818309966567740247634267',
        'QueryRetrieveLevel': 'SERIES'
    }

    ds = DCMDataset.create(ds_dict)
    # ds = Dataset()

    status = pacs.find_all(ds)
    print (status)



def run():
    # dicom_path = 'dicom_files/example/PM5644-960x540_RGB.dcm'
    # dicom_path = 'dicom_files/example_private/1.2.826.1.101009.947164870.1657604110.20250106100248/1.2.826.0.1.3680043.9.6965.1434327336.792316737.806139171/1.2.826.0.1.3680043.9.6965.1434327336.540312631.1182125904.dcm'
    # dicom_path = 'dicom_files/example_private/1.2.826.1.101009.947164870.1657604110.20250106100248/1.2.826.0.1.3680043.9.6965.1434327336.445349832.1434192875/1.2.826.0.1.3680043.9.6965.1434327336.444547519.1436781289.dcm'
    dicom_path = 'dicom_files/example_private/1.2.826.1.101009.947164870.1657604110.20250106100248/1.2.826.0.1.3680043.9.6965.1434327336.509243701.1254247338/1.2.826.0.1.3680043.9.6965.1434327336.483094607.1322137624.dcm'
    dicom = dcmread(dicom_path)
    status = pacs.store_dcm(dicom)
    print (status)

    # get_all_dicom()

if __name__ == '__main__':
    run()