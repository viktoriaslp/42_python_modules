from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from typing_extensions import Self


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def safety_requirements(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        correct_ranking = any(
            crew_member.rank in (Rank.commander, Rank.captain)
            for crew_member in self.crew
        )
        if not correct_ranking:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        exp_count = sum(
            crew_member.years_experience >= 5
            for crew_member in self.crew
        )
        if self.duration_days > 365 and exp_count * 2 < len(self.crew):
            raise ValueError(
                "Long missions (> 365 days)"
                " need 50% experienced crew (5+ years)"
            )
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self

    def show_info(self) -> None:
        print(
            f"Mission: {self.mission_name}",
            f"ID: {self.mission_id}",
            f"Destination: {self.destination}",
            f"Duration: {self.duration_days} days",
            f"Budget: ${self.budget_millions:.1f}M",
            f"Crew size: {len(self.crew)}",
            "Crew members:",
            sep="\n"
        )
        for member in self.crew:
            print(
                f"- {member.name} ({member.rank.value}) "
                f"- {member.specialization}"
            )


def main() -> None:
    sarah = CrewMember(
        member_id="001",
        name="Sarah Connor",
        rank=Rank.commander,
        age=55,
        specialization="Mission Command",
        years_experience=25,
        is_active=True,
    )

    john = CrewMember(
        member_id="002",
        name="John Smith",
        rank=Rank.lieutenant,
        age=60,
        specialization="Navigation",
        years_experience=15,
        is_active=True,
    )

    alice = CrewMember(
        member_id="003",
        name="Alice Johnson",
        rank=Rank.officer,
        age=35,
        specialization="Engineering",
        years_experience=12,
        is_active=True,
    )

    mars_mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime.now(),
        duration_days=900,
        crew=[sarah, john, alice],
        budget_millions=2500,
    )

    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    mars_mission.show_info()

    print()
    print("=========================================")
    print("Expected validation error:")
    try:
        venus_mission = SpaceMission(
            mission_id="M2024_Venus",
            mission_name="Venus Colony Establishment",
            destination="Venus",
            launch_date=datetime.now(),
            duration_days=200,
            crew=[john, alice],
            budget_millions=1900,
        )
        venus_mission.show_info()
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"].removeprefix("Value error, "))


if __name__ == "__main__":
    main()
