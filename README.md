# Website of the REAL group

Hey everyone!

This repo contains the REAL group's website. It is built using Wowchemy's academic template. [You can read the documentation for Wowchemy here](https://wowchemy.com/docs/). The website is hosted on netlify, and Thomas has access to it. Contact him if your changes are not being reflected!

# How-to
## How to add a new profile

Here is a template profile:

```md
---
# Display name 
# MODIFY:
title: Your name here

# MODIFY:
authors:
- Your name here

# Is this the primary user of the site?
superuser: false

# Role/position/tagline
# MODIFY:
role: Postdoc
user_groups: ["Postdocs"]

# Organizations/Affiliations to show in About widget
organizations:
- name: IT University of Copenhagen
  url: https://www.itu.dk/

# Short bio (displayed in user profile at end of posts)
# MODIFY:
bio: Working on self-driving vehicle safety.

# Interests to show in About widget
# MODIFY:
interests:
- Emergence
- Reinforcement Learning
- Safety

# Education to show in About widget
# UNCOMMENT AND MODIFY IF YOU WANT TO:
# education:
#   courses:
#   - course: PhD in Artificial Intelligence
#     institution: Stanford University
#     year: 2012
#   - course: MEng in Artificial Intelligence
#     institution: Massachusetts Institute of Technology
#     year: 2009
#   - course: BSc in Artificial Intelligence
#     institution: Massachusetts Institute of Technology
#     year: 2008

# Social/Academic Networking
# For available icons, see: https://sourcethemes.com/academic/docs/page-builder/#icons
#   For an email link, use "fas" icon pack, "envelope" icon, and a link in the
#   form "mailto:your-email@example.com" or "/#contact" for contact widget.
# MODIFY: add your mail, pure and Google Scholar if you want.
social:
- icon: envelope
  icon_pack: fas
  link: mailto:YOUR-MAIL-HERE
- icon: external-link-alt
  icon_pack: fas
  link: YOUR-LINK-TO-PURE-HERE
# - icon: graduation-cap  # Alternatively, use `google-scholar` icon from `ai` icon pack
#   icon_pack: fas
#   link: https://scholar.google.dk/citations?user=smoQomYAAAAJ&hl=da
# Enter email to display Gravatar (if Gravatar enabled in Config)
email: ""

# Highlight the author in author lists? (true/false)
highlight_name: false
---

WRITE A SHORT BIO HERE.
```

In `./content/authors` find someone who shares a similar role to you (be it professor, phd student or posdoc) and
1. copy-paste their profile folder and change its name to yours.
2. Change `avatar.png` to a photo of you, but **keep the name `avatar.png`**.
3. Modify `_index.md` by adding your information.

All of the active roles can be found in `./home/people`:

```yaml
content:
  # Choose which groups/teams of users to display.
  #   Edit `user_groups` in each user's profile to add them to one or more of these groups.
  user_groups:
    - Professors
    - Postdocs
    - PhD Students
    - Visiting PhD Students
    - Research Assistants
```

## How to move someone to previous members

When someone leaves our lab:
1. Find their folder in `./content/authors` and open their `_index.md`.
2. Replace whatever is inside `user_groups` with only `["Previous Members"]`
3. Copy and paste the following bit right after if you don't want a profile page to be built:

```yaml
# Add this to former members
_build:
  render: never
cascade:
  _build:
    render: never
    list: always
```

## How to add a new project

In `./content/project`, you can
1. copy-paste `Flora Robotica`, rename it to your project's name.
2. change the `featured.jpg` to another image (but **keeping the same name**).
3. Modify whatever is in `index.md` to your project's contents.

## How to add a new course

In `./content/education` you can
1. Copy-paste `Modern AI`, rename it to your course's name.
2. change the `featured.jpg` to another image (but **keeping the same name**).
3. Modify `index.md` by adding a summary of the course, and the external link to the LearnIT page.

# More instructions
## Instructions if you want to debug locally

1. [Install `hugo`](https://wowchemy.com/docs/getting-started/install-hugo-extended/#prerequisites).
2. In the repo itself, run `hugo server`. That way, you can see changes live in `localhost:1313`.

## Where to find good documentation

This site is built using `wowchemy`, and their documentation site is really good: https://wowchemy.com/docs/getting-started/get-started/

  
