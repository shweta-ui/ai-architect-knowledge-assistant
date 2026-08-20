from dataclasses import dataclass


@dataclass
class Document:
	"""A document belonging to a project."""

	title: str
	content: str


@dataclass
class ArchitecturDocument(Document):
	"""A document containing architectural knowledge."""

	architecture: str = ""
