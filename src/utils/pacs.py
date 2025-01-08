from pydicom.dataset import Dataset

class DCMDataset:
    def __init__(self, ds_dict):
        self.ds = self.create(ds_dict)

    def get(self):
        return self.ds

    def create(ds_dict):
        ds = Dataset()
        for key, value in ds_dict.items():
            setattr(ds, key, value)
        return ds


