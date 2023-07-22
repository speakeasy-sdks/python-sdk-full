"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from pg_latest import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class FetchSettlementReconRequestFilters:
    r"""Specify either the Settlement ID, Settlement UTR, or start date and end date to fetch the settlement details."""
    cf_settlement_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cf_settlement_ids'), 'exclude': lambda f: f is None }})
    r"""List of settlement IDs for which you want the settlement reconciliation details."""
    end_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'exclude': lambda f: f is None }})
    r"""Specify the end date till when you want the settlement reconciliation details."""
    settlement_utrs: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('settlement_utrs'), 'exclude': lambda f: f is None }})
    r"""List of settlement UTRs for which you want the settlement reconciliation details."""
    start_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'exclude': lambda f: f is None }})
    r"""Specify the start date from when you want the settlement reconciliation details."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class FetchSettlementReconRequestPagination:
    r"""To fetch the next set of settlements, pass the cursor received in the response to the next API call.
     To receive the data for the first time, pass the cursor as null. 
     Limit would be number of settlements that you want to receive.
    """
    limit: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('limit') }})
    r"""The number of settlements you want to fetch. Maximum limit is 1000, default value is 10."""
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cursor'), 'exclude': lambda f: f is None }})
    r"""Specifies from where the next set of settlement details should be fetched."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class FetchSettlementReconRequest:
    filters: FetchSettlementReconRequestFilters = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filters') }})
    r"""Specify either the Settlement ID, Settlement UTR, or start date and end date to fetch the settlement details."""
    pagination: FetchSettlementReconRequestPagination = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pagination') }})
    r"""To fetch the next set of settlements, pass the cursor received in the response to the next API call.
     To receive the data for the first time, pass the cursor as null. 
     Limit would be number of settlements that you want to receive.
    """
    

