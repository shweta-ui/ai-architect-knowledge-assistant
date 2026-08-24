from ..models.project import Project


_projects: dict[str, Project] = {}


def list_projects() -> list[Project]:
	"""Return all stored projects."""
	return list(_projects.values())


def create_project(name: str, description: str = "") -> Project:
	"""Create and store a project in memory."""
	if name in _projects:
		raise ValueError(f"Project already exists: {name}")

	project = Project(name=name, description=description)
	_projects[name] = project
	return project


def get_project(name: str) -> Project:
	"""Return a stored project by name."""
	try:
		return _projects[name]
	except KeyError as error:
		raise KeyError(f"Project not found: {name}") from error
