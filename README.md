# Storing HHS Network Configs 

## Problem

Each Op Div in HHS has and maintains its own network. Details about the network are opaque for HHS leadership. A propsoed
first step towards fixing this problem is to capture some metadata about each network in GitHub. 

To achieve that, Skylight is tasked with proposing a repo structure that is:
- Scalable: Multiple teams should be able to contribute to this repo without causing unnecessary conflict.
- Maintainable: Adding/updating the repo should be easy (assuming users know how to use `git`).
- Extendable: While the current scope of the project is to capture the network details, the structure should lend itself 
  to capturing details about other infrastructure components too.

## Solution

### Repo Structure
This repo demonstrates 2 options for storing network configuration details: `by_division` or `by_infrastructure_component`.

The purpose of each is to orient the info either by the divisions within HHS or by the infrastructure being tracked (Network/IDP/etc). 

| Orientation | Pro                                                                                              | Con                                                               |
|-------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| By Division | - Easy for teams to find their info <br> - Team's details are self-contained                     | - Folders sprawl <br> - Master list doesn't live with the details |
| By Infra Component | - Easy to know which component is used by each team <br> - Master list lives next to the details | - Hard to know all components used by a team                      |

### GitHub Workflows To Create A Master List

`.github/workflows/ci.yml` has an outline of a workflow that creates a master list of all the network configs. 
This master list is then fed into the HTML table linked in the next section.

### PoC Showing The Info In A Human Friendly Format

The JSON blocks have been transformed into a simple HTML table at [Sample HHS Network Outline](https://avaishnav-skylight.github.io/hhs_storing_configs/).

## What Is Not Covered

This repo does not mimic the "best practices" structure of an Infrastructure As Code (IaC) tool (Terraform/Terragrunt).

If (& when) HHS adopts them, it will be better to start a new repo and define its structure at that time.