"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import offerdetails as shared_offerdetails
from ..shared import offermeta as shared_offermeta
from ..shared import offertnc as shared_offertnc
from ..shared import offervalidations as shared_offervalidations
from dataclasses_json import Undefined, dataclass_json
from pg_latest import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OfferEntity:
    offer_details: Optional[shared_offerdetails.OfferDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('offer_details'), 'exclude': lambda f: f is None }})
    offer_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('offer_id'), 'exclude': lambda f: f is None }})
    offer_meta: Optional[shared_offermeta.OfferMeta] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('offer_meta'), 'exclude': lambda f: f is None }})
    offer_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('offer_status'), 'exclude': lambda f: f is None }})
    offer_tnc: Optional[shared_offertnc.OfferTnc] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('offer_tnc'), 'exclude': lambda f: f is None }})
    offer_validations: Optional[shared_offervalidations.OfferValidations] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('offer_validations'), 'exclude': lambda f: f is None }})
    

