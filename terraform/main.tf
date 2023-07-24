terraform {
  cloud {
    organization = "your-organization-name"  # from terraform cloud

    workspaces {
      name = "your-workspace-name"  # from terraform cloud
    }
  }
}
