from ..models.document import Document
from .project_service import get_project


_documents: dict[tuple[str, str], Document] = {}


def create_document(project_name: str, title: str, content: str) -> Document:
	"""Create and store a document for an existing project in memory."""
	project = get_project(project_name)
	document_key = (project_name, title)
	if document_key in _documents:
		raise ValueError(f"Document already exists: {title}")

	document = Document(title=title, content=content)
	_documents[document_key] = document
	project.documents.append(document)
	return document


def get_document(project_name: str, title: str) -> Document:
	"""Return a stored document by project name and title."""
	try:
		return _documents[(project_name, title)]
	except KeyError as error:
		raise KeyError(f"Document not found: {title}") from error
