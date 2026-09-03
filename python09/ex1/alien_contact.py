from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from typing_extensions import Self


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def business_rules(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        is_telepathic = self.contact_type == ContactType.telepathic
        if is_telepathic and self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )
        return self

    def show_info(self) -> None:
        print(
            f"ID: {self.contact_id}",
            f"Type: {self.contact_type.value}",
            f"Location: {self.location}",
            f"Signal: {self.signal_strength}/10",
            f"Duration: {self.duration_minutes} minutes",
            f"Witnesses: {self.witness_count}",
            f"Message: '{self.message_received}'",
            sep="\n",
        )


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    first_contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime.now(),
        location="Area 51, Nevada",
        contact_type=ContactType.radio,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
    )
    print("Valid contact report:")
    first_contact.show_info()

    print()

    print("======================================")
    print("Expected validation error:")
    try:
        second_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=1,
            message_received="Greetings from Zeta Reticuli",
        )
        second_contact.show_info()
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"].removeprefix("Value error, "))


if __name__ == "__main__":
    main()
