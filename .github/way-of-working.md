
## Way of Working

This document describes how the EN doc team plans and carries out 
documentation activities. 

### Milestones 

The doc team uses GitHub [milestones](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/about-milestones) 
to plan, track, and deliver documentation. A milestone represents the full list of documentation issues 
associated with a certain project. 

Project examples include: 

* A new release of an existing Agora product. For example, release of Signaling v1.6.0.
* A new release of an existing Agora product for certain platforms only. For example, release of Video SDK v4.1.1 for web.
* A new Agora product release. 
* Documentation improvements. For example, fixing broken links or aligning pricing pages across all docs.
* Generally, any combination of activities that would serve a single purpose. 

The need to start a documentation project may rise from the roadmap of product releases, requests from product or 
development teams, customer feedback on documentation, documentation analysis, or else. 

### Branches

When a milestone is created, an associated branch is created from the `staging` branch as well. 
It usually follows the following naming convention: 

`milestone-<number>-<milestone_name>`

For example, `milestone-45-video-sdk-4.1.1-native`. Branches for every issue in the milestone are created from 
the milestone branch and PRs are raised back into it. 

### Planning the work

Whenever a need arises to start a documentation project, the responsible TWs (currently [Saud](https://github.com/saudsami) and 
[Anastasia](https://github.com/atovpeko)) with help and supervision from the TW leading the EN doc team 
(currently [Iain](https://github.com/billy-the-fish)) create a milestone, open related issues, and assign those depending 
on the areas of responsibility:

* <Platform 1>: <Name>
* <Platform 2>: <Name>
* <Platform 3>: <Name>
* General improvement tickets: <Name>
* Release notes, API reference, and SDK downloads: <Name>

### Writing and reviewing 

The review process ideally includes the lead technical reviewer (currently [Saud](https://github.com/saudsami)), 
a language reviewer (currently [Anastasia](https://github.com/atovpeko)), and a PM reviewer on the need-only basis.

//Clarify requirements for PM review and a list of PMs to talk to 

For issues that require technical implementation, the doc team follows this process:

1. The lead technical reviewer (currently [Saud](https://github.com/saudsami) develops implementation for their platform,  
   raises a PR, and requests a language review from the language reviewer.  
2. Once all possible comments have been addressed and language review is passed, the lead technical reviewer passes 
   their implementation to other TWs who then adapt the implementation for their respective platforms. 
3. Each TW then raises a PR and requests a review from the lead technical reviewer and the language reviewer. 

For issues that do not require technical implementation, for example, adding release notes, only language review is required. 

Once all the issues in the milestone have been closed and PRs merged, <insert_role> raises a PR from the milestone branch 
to the staging branch and does the final visual check. <insert_role> reviews the PR. 

//Specify when and how it then goes to `main`.










