from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated

from config.city_tier import tier_1_cities, tier_2_cities


class UserInput(BaseModel):

    age: Annotated[
        int,
        Field(
            gt=0,
            description="Age of the user",
            example=30
        )
    ]

    weight: Annotated[
        float,
        Field(
            gt=0,
            description="Weight of the user in kilograms",
            example=70.5
        )
    ]

    height: Annotated[
        float,
        Field(
            gt=0,
            description="Height of the user",
            example=1.75
        )
    ]

    income_lpa: Annotated[
        float,
        Field(
            gt=0,
            description="Income of the user in LPA",
            example=5.5
        )
    ]

    smoker: Annotated[
        Literal["yes", "no"],
        Field(
            description="Whether the user is a smoker or not",
            example="no"
        )
    ]

    city: Annotated[
        str,
        Field(
            description="City where the user lives",
            example="Kathmandu"
        )
    ]

    occupation: Annotated[
        Literal[
            "retired",
            "freelancer",
            "student",
            "government_job",
            "business_owner",
            "unemployed",
            "private_job"
        ],
        Field(
            description="Occupation of the user"
        )
    ]

    @field_validator("city")
    @classmethod
    def normalize_city(cls, value: str) -> str:
        value = value.strip().title()
        return value

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi

    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker == "yes" and self.bmi > 30:
            return "high"
        elif self.smoker == "yes" or self.bmi > 27:
            return "medium"
        else:
            return "low"

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"

    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3