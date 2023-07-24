terraform {
  cloud {
    organization = "example-org-db64c5"

    workspaces {
      name = "karas-project-template"
    }
  }
}
