from torch.utils.data import Dataset, DataLoader

class SlidingWindowDataset(Dataset):
    def __init__(self, data, window_size):
        self.data = data
        self.window_size = window_size

    def __len__(self):
        return max(0, len(self.data) - self.window_size + 1)
    # TODO: Fix this

    def __getitem__(self, idx):
        window_data = self.data[idx:idx+self.window_size]
        window_label = self.data[idx+self.window_size+1]
        return window_data, window_label    


def get_dataloader(data, window_size, batch_size):
    dataset = SlidingWindowDataset(data, window_size)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=False)
    return dataloader