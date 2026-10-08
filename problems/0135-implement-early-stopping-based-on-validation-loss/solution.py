from typing import Tuple

def early_stopping(val_losses: list[float], patience: int, min_delta: float) -> Tuple[int, int]:
    # Your code here
    best_loss = float("inf")
    best_epoch = 0
    wait = 0
    for epoch, loss in enumerate(val_losses):
        
        if best_loss - loss > min_delta:
            best_loss, best_epoch = loss, epoch
            wait = 0
        else:
            wait += 1
            if wait >= patience:
                return epoch, best_epoch

    return len(val_losses) - 1, best_epoch
