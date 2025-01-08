from pydicom.uid import JPEG2000Lossless, DigitalXRayImageStorageForProcessing
from pynetdicom import AE, StoragePresentationContexts, debug_logger
from settings import PACS, DEBUG
from constraint.uid import PatientRootQueryRetrieveInformationModelFind
def save_dcm_to_pacs(dicom):
    if DEBUG:
        debug_logger()

    ae = AE()

    SOPClassUID = dicom.file_meta.MediaStorageSOPClassUID
    TransferSyntaxUID = dicom.file_meta.TransferSyntaxUID
    ae.add_requested_context(SOPClassUID, TransferSyntaxUID)

    assoc = ae.associate(PACS.get('server'), PACS.get('port'), ae_title=PACS.get('ae_title'))
    if assoc.is_established:
        status = assoc.send_c_store(dicom)
        if status:
            print('C-STORE request status: 0x{0:04x}'.format(status.Status))
        else:
            print('Connect  ion timed out, was aborted or received invalid response')
        assoc.release()
        return status
    else:
        print("Association rejected, aborted or never connected")

def find_all(ds):
    if DEBUG:
        debug_logger()

    ae = AE()

    ae.add_requested_context(PatientRootQueryRetrieveInformationModelFind)

    # ae.add_requested_context('1.2.840.10008.5.1.4.1.1.77.1.5.1')
    # ae.add_supported_context('1.2.840.10008.1.1')
    assoc = ae.associate(PACS.get('server'), PACS.get('port'), ae_title=PACS.get('ae_title'))

    if assoc.is_established:
        # Send the C-FIND request
        responses = assoc.send_c_find(ds, PatientRootQueryRetrieveInformationModelFind)
        for (status, identifier) in responses:
            if status:
                print('C-FIND query status: 0x{0:04X}'.format(status.Status))
                print('identifier', identifier)

            else:
                print('Connection timed out, was aborted or received invalid response')
            print ('=====================================')
        # Release the association
        assoc.release()
    else:
        print('Association rejected, aborted or never connected')

