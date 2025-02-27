# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Convention:
 - Do not include any `_TYPE` suffix
 - Types used in public hooks (as those in the `LightningModule` and `Callback`) should be public (no leading `_`)
"""
from pathlib import Path
from typing import Any, Dict, Iterator, List, Mapping, Optional, Sequence, Type, Union

import torch
from torch.optim import Optimizer
from torch.utils.data import DataLoader
from torchmetrics import Metric
from typing_extensions import TypedDict

_NUMBER = Union[int, float]
_METRIC = Union[Metric, torch.Tensor, _NUMBER]
_METRIC_COLLECTION = Union[_METRIC, Mapping[str, _METRIC]]
STEP_OUTPUT = Union[torch.Tensor, Dict[str, Any]]
EPOCH_OUTPUT = List[STEP_OUTPUT]
_EVALUATE_OUTPUT = List[Dict[str, float]]  # 1 dict per DataLoader
_PREDICT_OUTPUT = Union[List[Any], List[List[Any]]]
_PARAMETERS = Iterator[torch.nn.Parameter]
_PATH = Union[str, Path]
TRAIN_DATALOADERS = Union[
    DataLoader,
    Sequence[DataLoader],
    Sequence[Sequence[DataLoader]],
    Sequence[Dict[str, DataLoader]],
    Dict[str, DataLoader],
    Dict[str, Dict[str, DataLoader]],
    Dict[str, Sequence[DataLoader]],
]
EVAL_DATALOADERS = Union[DataLoader, Sequence[DataLoader]]


# Copied from `torch.optim.lr_scheduler.pyi`
# Missing attributes were added to improve typing
class _LRScheduler:
    optimizer: Optimizer

    def __init__(self, optimizer: Optimizer, last_epoch: int = ...) -> None:
        ...

    def state_dict(self) -> dict:
        ...

    def load_state_dict(self, state_dict: dict) -> None:
        ...

    def get_last_lr(self) -> List[float]:
        ...

    def get_lr(self) -> float:
        ...

    def step(self, epoch: Optional[int] = ...) -> None:
        ...


# Copied from `torch.optim.lr_scheduler.pyi`
# Missing attributes were added to improve typing
class ReduceLROnPlateau:
    in_cooldown: bool
    optimizer: Optimizer

    def __init__(
        self,
        optimizer: Optimizer,
        mode: str = ...,
        factor: float = ...,
        patience: int = ...,
        verbose: bool = ...,
        threshold: float = ...,
        threshold_mode: str = ...,
        cooldown: int = ...,
        min_lr: float = ...,
        eps: float = ...,
    ) -> None:
        ...

    def step(self, metrics: Any, epoch: Optional[int] = ...) -> None:
        ...

    def state_dict(self) -> dict:
        ...

    def load_state_dict(self, state_dict: dict) -> None:
        ...


# todo: improve LRSchedulerType naming/typing
LRSchedulerTypeTuple = (torch.optim.lr_scheduler._LRScheduler, torch.optim.lr_scheduler.ReduceLROnPlateau)
LRSchedulerTypeUnion = Union[torch.optim.lr_scheduler._LRScheduler, torch.optim.lr_scheduler.ReduceLROnPlateau]
LRSchedulerType = Union[Type[torch.optim.lr_scheduler._LRScheduler], Type[torch.optim.lr_scheduler.ReduceLROnPlateau]]


class LRSchedulerConfig(TypedDict):
    scheduler: Union[_LRScheduler, ReduceLROnPlateau]
    name: Optional[str]
    interval: str
    frequency: int
    reduce_on_plateau: bool
    monitor: Optional[str]
    strict: bool
    opt_idx: Optional[int]
