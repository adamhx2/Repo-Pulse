# RepoPulse Roadmap

## 1. Define the widget

- Decide what the widget displays.
- Sketch the compact player layout.
- Create the four color options: green, purple, black, and white.

## 2. Build the widget

- Build the widget with HTML, CSS, and JavaScript.
- Make it responsive and easy to insert into another website.
- Start with sample project data before connecting it to GitHub.

## 3. Connect project data

- Read recent activity from a public GitHub repository.
- Pull the latest useful change, update date, and release.
- Allow the project owner to set a short status and current message.

## 4. Generate the pulse

- Combine the owner settings and GitHub activity.
- Save the result as a small `pulse.json` file.
- Have the widget load and display that file.

## 5. Automate updates

- Add a GitHub Action that regenerates `pulse.json`.
- Run it when the project changes or a release is published.
- Keep GitHub credentials out of the website.

## 6. Test it on AtomHUD

- Add RepoPulse to the Workshop.
- Make sure it adds useful context without crowding the project entries.
- Adjust the layout and information based on real use.

## 7. Make it shareable

- Write simple setup instructions.
- Provide copy-and-paste embed code.
- Include an example configuration and demo page.
- Publish the first version.

## Later

- Custom color picker
- More widget layouts
- Multiple projects in one feed
- GitLab support
- Private repository support
