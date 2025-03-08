from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class NamespaceBase(BaseModel):
    name: str
    path: str
    kind: str
    full_path: str
    parent_id: Optional[int] = None
    avatar_url: Optional[str] = None
    web_url: str

    class Config:
        orm_mode = True


class PermissionBase(BaseModel):
    project_access: str
    group_access: str

    class Config:
        orm_mode = True


class LinksBase(BaseModel):
    self: str
    issues: str
    merge_requests: str
    repo_branches: str
    labels: str
    events: str
    members: str
    cluster_agents: str

    class Config:
        orm_mode = True


class ContainerExpirationPolicyBase(BaseModel):
    cadence: str
    enabled: bool
    keep_n: int
    older_than: str
    name_regex: str
    name_regex_keep: Optional[str] = None
    next_run_at: datetime

    class Config:
        orm_mode = True


class ProjectBase(BaseModel):
    description: Optional[str] = None
    name: str
    name_with_namespace: str
    path: str
    path_with_namespace: str
    created_at: datetime
    updated_at: datetime
    default_branch: str
    tag_list: str
    topics: str
    ssh_url_to_repo: str
    http_url_to_repo: str
    web_url: str
    avatar_url: Optional[str] = None
    forks_count: int
    star_count: int
    last_activity_at: datetime
    container_registry_image_prefix: str
    packages_enabled: bool
    empty_repo: bool
    archived: bool
    visibility: str
    resolve_outdated_diff_discussions: bool
    repository_object_format: str
    issues_enabled: bool
    merge_requests_enabled: bool
    wiki_enabled: bool
    jobs_enabled: bool
    snippets_enabled: bool
    container_registry_enabled: bool
    service_desk_enabled: bool
    can_create_merge_request_in: bool
    issues_access_level: str
    repository_access_level: str
    merge_requests_access_level: str
    forking_access_level: str
    wiki_access_level: str
    builds_access_level: str
    snippets_access_level: str
    pages_access_level: str
    analytics_access_level: str
    container_registry_access_level: str
    security_and_compliance_access_level: str
    releases_access_level: str
    environments_access_level: str
    feature_flags_access_level: str
    infrastructure_access_level: str
    monitor_access_level: str
    model_experiments_access_level: str
    model_registry_access_level: str
    emails_disabled: bool
    emails_enabled: bool
    shared_runners_enabled: bool
    lfs_enabled: bool
    creator_id: int
    import_status: str
    open_issues_count: int
    description_html: Optional[str] = None
    updated_at: datetime
    public_jobs: bool
    shared_with_groups: str
    only_allow_merge_if_pipeline_succeeds: bool
    allow_merge_on_skipped_pipeline: Optional[bool] = None
    request_access_enabled: bool
    only_allow_merge_if_all_discussions_are_resolved: bool
    remove_source_branch_after_merge: bool
    printing_merge_request_link_enabled: bool
    merge_method: str
    squash_option: str
    enforce_auth_checks_on_uploads: bool
    suggestion_commit_message: Optional[str] = None
    merge_commit_template: Optional[str] = None
    squash_commit_template: Optional[str] = None
    issue_branch_template: Optional[str] = None
    warn_about_potentially_unwanted_characters: bool
    autoclose_referenced_issues: bool

    permissions_id: Optional[int] = None
    container_expiration_policy_id: Optional[int] = None
    links_id: Optional[int] = None
    namespace_id: Optional[int] = None

    class Config:
        orm_mode = True


# Models for insertion (optional)
class NamespaceCreate(NamespaceBase):
    pass


class PermissionCreate(PermissionBase):
    pass


class LinksCreate(LinksBase):
    pass


class ContainerExpirationPolicyCreate(ContainerExpirationPolicyBase):
    pass


class ProjectCreate(ProjectBase):
    pass


# Model for responses (Optional)
class NamespaceResponse(NamespaceBase):
    id: int


class PermissionResponse(PermissionBase):
    id: int


class LinksResponse(LinksBase):
    id: int


class ContainerExpirationPolicyResponse(ContainerExpirationPolicyBase):
    id: int


class ProjectResponse(ProjectBase):
    id: int


