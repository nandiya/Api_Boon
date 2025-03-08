import requests
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, Text, Enum
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.dialects.postgresql import ARRAY

Base = declarative_base()


class Namespace(Base):
    __tablename__ = 'namespace'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    path = Column(String)
    kind = Column(String)
    full_path = Column(String)
    parent_id = Column(Integer)
    avatar_url = Column(String)
    web_url = Column(String)
    
class Permission(Base):
    __tablename__ = 'permissions'
    id = Column(Integer, primary_key=True)
    project_access = Column(String)
    group_access = Column(String)

# Links table
class Links(Base):
    __tablename__ = 'links'
    id = Column(Integer, primary_key=True)
    self = Column(String)
    issues = Column(String)
    merge_requests = Column(String)
    repo_branches = Column(String)
    labels = Column(String)
    events = Column(String)
    members = Column(String)
    cluster_agents = Column(String)

# ContainerExpirationPolicy table
class ContainerExpirationPolicy(Base):
    __tablename__ = 'container_expiration_policy'
    id = Column(Integer, primary_key=True)
    cadence = Column(String)
    enabled = Column(Boolean)
    keep_n = Column(Integer)
    older_than = Column(String)
    name_regex = Column(String)
    name_regex_keep = Column(String)
    next_run_at = Column(DateTime)

# Project table with foreign keys
class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    description = Column(Text)
    name = Column(String)
    name_with_namespace = Column(String)
    path = Column(String)
    path_with_namespace = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    default_branch = Column(String)
    tag_list = Column(String)
    topics = Column(String)
    ssh_url_to_repo = Column(String)
    http_url_to_repo = Column(String)
    web_url = Column(String)
    avatar_url = Column(String)
    forks_count = Column(Integer)
    star_count = Column(Integer)
    last_activity_at = Column(DateTime)
    container_registry_image_prefix = Column(String)
    packages_enabled = Column(Boolean)
    empty_repo = Column(Boolean)
    archived = Column(Boolean)
    visibility = Column(String)
    resolve_outdated_diff_discussions = Column(Boolean)
    repository_object_format = Column(String)
    issues_enabled = Column(Boolean)
    merge_requests_enabled = Column(Boolean)
    wiki_enabled = Column(Boolean)
    jobs_enabled = Column(Boolean)
    snippets_enabled = Column(Boolean)
    container_registry_enabled = Column(Boolean)
    service_desk_enabled = Column(Boolean)
    can_create_merge_request_in = Column(Boolean)
    issues_access_level = Column(String)
    repository_access_level = Column(String)
    merge_requests_access_level = Column(String)
    forking_access_level = Column(String)
    wiki_access_level = Column(String)
    builds_access_level = Column(String)
    snippets_access_level = Column(String)
    pages_access_level = Column(String)
    analytics_access_level = Column(String)
    container_registry_access_level = Column(String)
    security_and_compliance_access_level = Column(String)
    releases_access_level = Column(String)
    environments_access_level = Column(String)
    feature_flags_access_level = Column(String)
    infrastructure_access_level = Column(String)
    monitor_access_level = Column(String)
    model_experiments_access_level = Column(String)
    model_registry_access_level = Column(String)
    emails_disabled = Column(Boolean)
    emails_enabled = Column(Boolean)
    shared_runners_enabled = Column(Boolean)
    lfs_enabled = Column(Boolean)
    creator_id = Column(Integer)
    import_status = Column(String)
    open_issues_count = Column(Integer)
    description_html = Column(String)
    updated_at = Column(DateTime)
    public_jobs = Column(Boolean)
    shared_with_groups = Column(String)
    only_allow_merge_if_pipeline_succeeds = Column(Boolean)
    allow_merge_on_skipped_pipeline = Column(Boolean)
    request_access_enabled = Column(Boolean)
    only_allow_merge_if_all_discussions_are_resolved = Column(Boolean)
    remove_source_branch_after_merge = Column(Boolean)
    printing_merge_request_link_enabled = Column(Boolean)
    merge_method = Column(String)
    squash_option = Column(String)
    enforce_auth_checks_on_uploads = Column(Boolean)
    suggestion_commit_message = Column(String)
    merge_commit_template = Column(String)
    squash_commit_template = Column(String)
    issue_branch_template = Column(String)
    warn_about_potentially_unwanted_characters = Column(Boolean)
    autoclose_referenced_issues = Column(Boolean)

        
    permissions_id = Column(Integer, ForeignKey('permissions.id'))
    # ContainerExpirationPolicy fields as foreign key
    container_expiration_policy_id = Column(Integer, ForeignKey('container_expiration_policy.id'))
    # Links table foreign key
    links_id = Column(Integer, ForeignKey('links.id'))
    # Namespace foreign key
    namespace_id = Column(Integer, ForeignKey('namespace.id'))




# Create an SQLite engine
engine = create_engine('sqlite:///projects.db', echo=True)

# Create tables
Base.metadata.create_all(engine)