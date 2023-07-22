"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from pg_latest import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class FetchPGReconRequestFilters:
    end_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date') }})
    r"""Specify the end date till when you want the settlement reconciliation details."""
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    r"""Specify the start date from when you want the settlement reconciliation details."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class FetchPGReconRequestPagination:
    r"""To fetch the next set of settlements, pass the cursor received in the response to the next API call.
     To receive the data for the first time, pass the cursor as null. 
     Limit would be number of settlements that you want to receive.
    """
    limit: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('limit') }})
    r"""Number of settlements you want to fetch in the next iteration. Maximum limit is 1000, default value is 10."""
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cursor'), 'exclude': lambda f: f is None }})
    r"""Specifies from where the next set of settlement details should be fetched."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class FetchPGReconRequest:
    filters: FetchPGReconRequestFilters = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filters') }})
    pagination: FetchPGReconRequestPagination = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pagination') }})
    r"""To fetch the next set of settlements, pass the cursor received in the response to the next API call.
     To receive the data for the first time, pass the cursor as null. 
     Limit would be number of settlements that you want to receive.
    """
    

