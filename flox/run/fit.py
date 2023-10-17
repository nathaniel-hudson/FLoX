from __future__ import annotations

import torch

from flox.flock import Flock
from flox.run.fit_sync import sync_federated_fit
from flox.nn.types import Kind, Where
from flox.strategies import Strategy
from flox.utils.data import FederatedDataset


def federated_fit(
    flock: Flock,
    module_cls: type[torch.nn.Module],
    datasets: FederatedDataset,
    num_global_rounds: int,
    strategy: Strategy | str,
    kind: Kind = "sync",
    where: Where = "local",
):
    """

    Args:
        flock (Flock):
        module_cls (type[torch.nn.Module]):
        datasets (FederatedDataset):
        num_global_rounds (int):
        strategy (Strategy):
        kind (Kind):
        where (Where):

    Returns:

    """
    if kind == "sync":
        executor = "thread" if where == "local" else "globus_compute"
        return sync_federated_fit(
            flock, module_cls, datasets, num_global_rounds, strategy, executor
        )
    elif kind == "async":
        raise NotImplementedError("Asynchronous FL is not yet implemented.")
    else:
        raise ValueError(
            "Illegal value for argument `kind`. Must be either 'sync' or 'async'."
        )