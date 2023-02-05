
# Way of Working

Documentation is a crucial part of Agora's offering to customers. This document describes how the EN doc team
plans and carries out documentation activities to make sure that everything on Agora's
[documentation website](docs.agora.io) is up to standard and released in a timely manner.

## EN doc team structure

Currently, the EN doc team includes the following roles and members:

* Documentation Architect: [Iain](https://github.com/billy-the-fish)
* Technical Writer Lead: [Saud](https://github.com/saudsami)
* Editor: [Anastasia](https://github.com/atovpeko)
* Technical Writers: [Dasun](https://github.com/nirm2009), [Hussain](https://github.com/hussain-khalid),
* [Pankaj](https://github.com/Pankajg123), and [Kishan](https://github.com/Kishan-Dhakan).

## Documentation work lifecycle

Working on documentation includes the following stages:

1. Documentation request
2. Project planning and management
3. Writing
4. Review
5. Publishing

### Prerequisites

Agora uses [Docusaurus](https://docusaurus.io/) to generate a static documentation website.
To be able to contribute to Agora documentation, follow [this procedure](https://github.com/AgoraIO/Docs/edit/staging/README.md)
and then clone [all other repositories](#repositories) that the EN doc team works in.

//Clarify environment setup for implementation per platform

### 1. Documentation request

The need to deliver new or update the existing documentation may arise from the [roadmap of product releases](insert link to the roadmap,
if possible), requests from product or development teams, customer feedback on documentation, or internal
documentation analysis.

//Insert a matrix of stakeholders (PMs, devs, etc.) with the products/areas they are responsible for.

### 2. Project planning and management

The TW Lead and Editor analyze the documentation request and, with help and consult of the Documentation Architect, plan and
assign the work in the form of milestones and related issues.

//Clarify whether we need to do costing before we start on a milestone

#### Milestones

The doc team uses GitHub [milestones](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/about-milestones)
to plan, track, and deliver documentation. A milestone represents the full list of documentation issues
associated with a certain project.

Milestone examples include:

* A new release of an existing Agora product. For example, release of Signaling v1.6.0.
* A new release of an existing Agora product for certain platforms only. For example, release of Video SDK v4.1.1 for web.
* A new Agora product release.
* Documentation improvements. For example, fixing broken links or aligning pricing pages across all docs.
* Generally, any combination of activities that would serve a single purpose.

#### Issues

After a milestone is created, the TW Lead and Editor create issues for each smaller documentation task using
the following logic:

//Do we create a separate issue for each platform or one issue with subtasks for each platform? Clarify general
logic of splitting up work into issues.

#### Branches

The milestone creator also creates a milestone branch from the `staging` branch and specifies it in the milestone description.
It usually follows this naming convention:

`milestone-<number>-<milestone_name>`

For example, `milestone-45-video-sdk-4.1.1-native`.

//Specify how long we need to keep milestones after they are merged.

TWs create branches for their assigned issues from
the milestone branch and raise PRs back into it. Issue branches usually follow this naming convention:

`<issue_number>-<doc_type>_<platform>`

For example, `1064-quickstart-android`. When all the issue branches are merged, the milestone branch is then merged to
`staging`.

//Clarify how and when it goes to `main`.

#### Repositories

//Insert a list of repositories with submodules and nuances and whether we create milestones in all of them.

#### Assignment

Issues in a milestone are assigned to TWs depending on their areas of responsibility and rotation.

Every platform has a primary writer and a backup writer who is assigned the ticket if the primary writer is unavailable.
The backup writer also acts as a primary reviewer.

Backup writers change their platform every quarter.

| Platform                                        | Primary writer                               | Backup writer/Primary reviewer               |
|-------------------------------------------------|----------------------------------------------|----------------------------------------------|
| Android                                         | [Saud](https://github.com/saudsami)          | TBC                                          |
| Flutter                                         | [Saud](https://github.com/saudsami)          | TBC                                          |
| iOS                                             | [Dasun](https://github.com/nirm2009)         | [Iain](https://github.com/billy-the-fish)    |
| macOS                                           | [Dasun](https://github.com/nirm2009)         | [Iain](https://github.com/billy-the-fish)    |
| Unity                                           | [Hussain](https://github.com/hussain-khalid) | TBC                                          |
| Windows C++                                     | [Pankaj](https://github.com/Pankajg123)      | [Hussain](https://github.com/hussain-khalid) |     
| Windows C#                                      | [Pankaj](https://github.com/Pankajg123)      | [Hussain](https://github.com/hussain-khalid) |
| Web                                             | [Kishan](https://github.com/Kishan-Dhakan)   | [Hussain](https://github.com/hussain-khalid) | 
| Electron                                        | [Kishan](https://github.com/Kishan-Dhakan)   ||
| React Native                                    | [Kishan](https://github.com/Kishan-Dhakan)   ||
| Linux Java                                      | TBC                                          | TBC                                          |
| Linux C++                                       | TBC                                          | TBC                                          |
| General improvement tickets                     | Every TW in turn                             | Every TW in turn                             |                |
| Release notes, API reference, and SDK downloads | [Anastasia](https://github.com/atovpeko)     | [Dasun](https://github.com/nirm2009)         |

### Writing

All Agora documentation is written in a clear, consistent American English,
following [Google developer documentation style guide](https://developers.google.com/style).

For issues that require technical implementation, the doc team follows this process:

1. The TW Lead develops implementation for their platform, raises a PR, and requests a review from the Documentation Architect and the Editor.
2. Once all possible comments have been addressed and technical/language review is passed, the TW Lead passes
   their implementation to other TWs who then adapt the implementation for their respective platforms.

For issues that do not require technical implementation, TWs use their judgement or input from dev teams or other SMEs.

For API reference, if the HTML files are not provided by SMEs, the TWs follow this procedure to generate them:

//Clarify the procedure and criteria for when the HTML files have to be re-generated.

### Review

The review stage includes self-review, team review, and PM review, if needed.

#### Self-review

Before raising a PR, every TW does a self-review in the local build:

//Clarify the procedure with `yarn start`/`yarn build`/`yarn clear`

#### Team review

Each TW raises a PR and requests reviews following this logic:

| Review type | Reviewer | Mandatory or optional                                      |
| ----------- | -------- |------------------------------------------------------------|
| Language    | Editor   | Mandatory                                                  |
| Technical   | Primary writer requests a review from the backup writer for their platform. Backup writer requests a review from the primary writer, if available, or the Documentation Architect.| Mandatory for issues that require technical implementation |

#### Stakeholder review

//Clarify requirements for PM review
//Clarify Vercel procedure

### Publishing

//Clarify publishing procedure





















