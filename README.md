# SCG — THE MAZE / Blender CGI

An independent procedural 3D project for Stage Craft Group Instagram Reels. No paid AI generation required. The included `assets/scg-logo.png` is the provided SCG mark; it is **not yet composited into the test render**.

## First run on GitHub (iPhone compatible)

1. Unzip this archive using Files on iPhone.
2. Open your `kxvln-lgtm/SCG-MOTION` repository in GitHub and upload the **contents** of this folder, keeping `.github/workflows/scg-maze.yml` and `blender/maze.py` at those exact paths. GitHub's browser uploader may be cumbersome with hidden folders on iPhone; an alternative is to create those two files in GitHub's web editor and paste their contents.
3. Open **Actions → SCG The Maze / Blender Preview → Run workflow**, choose `preview`.
4. Download artifact **SCG-The-Maze-preview** after successful completion. The archive contains MP4 and an editable .blend.
5. Choose `full` only after preview review. Full mode can be very slow or exceed free runner capacity.

## Specs
- Preview: 5 sec, 360×640, 24fps, Cycles CPU 8 samples.
- Full render: 30 sec, 720×1280, 24fps, Cycles CPU 16 samples.
- 9:16 portrait, original procedural maze, animated FPV camera.
- This is **stage 1: CGI test**, not the final graded, sound-designed 1080×1920/60fps film.

## Limitations / next production stages
The generated path is smooth but requires visual QA to detect wall clipping, corner clearance, and shot pacing. The preview is intentionally low resolution. Later passes will include geometry transformation, final logo composite, typography, sound, and 1080×1920 master. Blender has not been run in the ChatGPT execution environment; the GitHub workflow is the first integration test.
