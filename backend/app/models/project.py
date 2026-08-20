from dataclasses import dataclass, field

from .document import Document


@dataclass
class Project:
	"""A project and its associated documents."""

	name: str
	description: str = ""
	documents: list[Document] = field(default_factory=list)
