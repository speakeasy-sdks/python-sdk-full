"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .offerdetails import OfferDetails
from .offermeta import OfferMeta
from .offertnc import OfferTnc
from .offervalidations import OfferValidations
from dataclasses_json import Undefined, dataclass_json
from pg_latest import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateOfferBackendRequest:
    offer_details: OfferDetails = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('offer_details') }})
    offer_meta: OfferMeta = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('offer_meta') }})
    offer_tnc: OfferTnc = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('offer_tnc') }})
    offer_validations: OfferValidations = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('offer_validations') }})
    

