from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, ConfigDict, Field

from .models.project import Project
from .services.project_service import create_project, list_projects


class ProjectCreate(BaseModel):
	"""Payload for creating a project."""

	name: str = Field(min_length=1)
	description: str = ""


class DocumentResponse(BaseModel):
	"""Public document representation."""

	model_config = ConfigDict(from_attributes=True)

	title: str
	content: str


class ProjectResponse(BaseModel):
	"""Public project representation."""

	model_config = ConfigDict(from_attributes=True)

	name: str
	description: str
	documents: list[DocumentResponse]


app = FastAPI(title="AI Architect Knowledge Assistant")


@app.get("/health")
def health() -> dict[str, str]:
	return {"status": "ok"}


@app.get("/projects", response_model=list[ProjectResponse])
def get_projects() -> list[Project]:
	return list_projects()


@app.post(
	"/project",
	response_model=ProjectResponse,
	status_code=status.HTTP_201_CREATED,
)
def post_project(payload: ProjectCreate) -> Project:
	try:
		return create_project(payload.name, payload.description)
	except ValueError as error:
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail=str(error),
		) from error


def main() -> None:
	"""Start the AI Architect Knowledge Assistant."""
	import uvicorn

	uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
	main()
