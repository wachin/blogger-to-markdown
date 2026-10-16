# Blog to Markdown - Development Roadmap

## Project Vision
Create a comprehensive tool to download, convert, and archive blog posts to Markdown format with full internationalization support and multiple interfaces (GUI/CLI).

---

## ✅ Phase 1: Core Functionality (COMPLETED)

### [x] Basic CLI Tool
- [x] Download blog post HTML content
- [x] Extract post title and content
- [x] Download all images from post
- [x] Convert HTML to Markdown format
- [x] Organize files in folders
- [x] Create README.md with content
- [x] Update image links to local paths
- [x] Command-line argument support

### [x] Script Automation
- [x] Bash wrapper script (`descargar_blog.sh`)
- [x] Virtual environment auto-creation
- [x] Dependency auto-installation
- [x] User-friendly command interface

### [x] Documentation - CLI
- [x] Main README with usage instructions
- [x] Requirements.txt with dependencies
- [x] Usage examples document
- [x] Troubleshooting guide

---

## ✅ Phase 2: Graphical User Interface (COMPLETED)

### [x] PyQt5 GUI Application
- [x] Main window with modern interface
- [x] URL input field
- [x] Output folder selector with file browser
- [x] Auto-create folder option
- [x] Download button
- [x] Real-time progress log area
- [x] Status bar with current status
- [x] Success/Error message dialogs

### [x] Background Processing
- [x] Non-blocking download thread
- [x] Progress updates to UI
- [x] Error handling and reporting
- [x] Thread-safe operations

### [x] GUI Launch Scripts
- [x] `run_gui.sh` - Auto-setup and launch
- [x] Dependency verification
- [x] Virtual environment handling

---

## ✅ Phase 3: Internationalization (COMPLETED)

### [x] i18n Infrastructure
- [x] Qt translation system setup
- [x] `tr()` function implementation throughout code
- [x] Language selector in GUI
- [x] Translation file structure

### [x] English Translation (Base)
- [x] All UI elements in English
- [x] Error messages in English
- [x] Progress messages in English
- [x] Dialog messages in English
- [x] Translation file: `blog_downloader_en.ts`

### [x] Spanish Translation
- [x] All UI elements translated
- [x] Error messages translated
- [x] Progress messages translated
- [x] Dialog messages translated
- [x] Translation file: `blog_downloader_es.ts`

### [x] Translation Tools
- [x] Translation compilation script
- [x] Instructions for adding new languages

---

## ✅ Phase 4: Testing & Documentation (COMPLETED)

### [x] Testing
- [x] Dependency verification script (`test_gui.py`)
- [x] Import testing
- [x] PyQt5 functionality testing
- [x] Translation file verification
- [x] Successful test run with real blog post

### [x] Comprehensive Documentation
- [x] Main README.md (overview of all tools)
- [x] README_GUI.md (GUI documentation)
- [x] README_BLOG_DOWNLOADER.md (CLI documentation)
- [x] QUICK_START.md (quick start guide)
- [x] EJEMPLOS_USO.md (usage examples)
- [x] Translation documentation
- [x] Troubleshooting sections

### [x] Project Setup
- [x] .gitignore configuration
- [x] Desktop entry file for Linux
- [x] Requirements.txt with all dependencies
- [x] Project structure organization

---

## ✅ Phase 5: Date-based Naming (COMPLETED)

### [x] Extract Publication Date
- [x] Parse blog post publication date from HTML
- [x] Support multiple date formats
- [x] Handle different blog platforms (Blogger, WordPress, etc.)
- [x] Extract date from URL if not in content
- [x] Fallback to current date if unavailable

### [x] Date-based Folder Naming
- [x] Format: `YYYYMMDD-post-slug`
- [x] Example: `20231107-kwallet-configuracion`
- [x] Clean slug generation from title
- [x] Handle special characters in slugs
- [x] Option to enable/disable date prefix

### [x] GUI Enhancements for Dates
- [x] Checkbox: "Add date prefix to folder name"
- [x] Date format selector (YYYYMMDD, YYYY-MM-DD, etc.)
- [x] Preview of final folder name
- [x] Option to use custom date if auto-detection fails

### [x] CLI Enhancements for Dates
- [x] `--add-date` flag
- [x] `--date-format` option
- [x] `--custom-date` parameter
- [x] Date format in output

---

## 🚧 Phase 6: Full Blog Download (NEXT)

### [ ] Blog Discovery
- [ ] Detect blog platform (Blogger, WordPress, etc.)
- [ ] Find all blog post URLs
- [ ] Parse blog archive/sitemap
- [ ] Support for paginated post lists
- [ ] RSS/Atom feed parsing

### [ ] Blogger-Specific Support
- [ ] Parse Blogger archive page
- [ ] Extract all post URLs from `washingtonindacochea.blogspot.com`
- [ ] Handle Blogger URL patterns
- [ ] Support for draft/published filtering

### [ ] Batch Download Engine
- [ ] Queue system for multiple downloads
- [ ] Configurable download delay between posts
- [ ] Retry mechanism for failed downloads
- [ ] Resume capability for interrupted downloads
- [ ] Progress tracking (X of Y posts)

### [ ] GUI for Full Blog Download
- [ ] "Download Entire Blog" mode/button
- [ ] Blog URL input (main blog URL)
- [ ] Post list preview before download
- [ ] Select/deselect individual posts
- [ ] Batch progress bar
- [ ] Overall progress percentage
- [ ] Estimated time remaining
- [ ] Cancel/Pause functionality

### [ ] CLI for Full Blog Download
- [ ] `--full-blog` flag
- [ ] `--blog-url` parameter
- [ ] `--delay` option (seconds between downloads)
- [ ] `--max-posts` limit option
- [ ] Progress output to console
- [ ] Log file generation

### [ ] Organization
- [ ] Master folder for entire blog
- [ ] Individual folders per post with dates
- [ ] Index/TOC generation (list of all posts)
- [ ] Category-based organization (optional)
- [ ] Chronological sorting

---

## 📋 Phase 7: Advanced Features (FUTURE)

### [ ] Content Filtering
- [ ] Download posts by date range
- [ ] Download posts by category/tag
- [ ] Download posts by keyword search
- [ ] Exclude specific posts

### [ ] Enhanced Markdown
- [ ] Preserve more HTML formatting
- [ ] Table support
- [ ] Code block syntax highlighting hints
- [ ] Footnote support
- [ ] Custom CSS/styling options

### [ ] Media Handling
- [ ] Video download support
- [ ] Audio file support
- [ ] PDF attachment downloads
- [ ] Embedded content handling
- [ ] Optional image resizing/optimization

### [ ] Export Formats
- [ ] Plain text export
- [ ] HTML export (offline version)
- [ ] PDF generation
- [ ] EPUB for e-readers
- [ ] Jekyll/Hugo compatible format

### [ ] Platform Support
- [ ] WordPress blog support
- [ ] Medium article support
- [ ] Ghost blog support
- [ ] Custom blog platform detection
- [ ] Generic HTML page support

---

## 🌟 Phase 8: Polish & Distribution (FUTURE)

### [ ] Performance Optimization
- [ ] Parallel image downloads
- [ ] Caching mechanism
- [ ] Memory usage optimization
- [ ] Large blog handling

### [ ] User Experience
- [ ] Settings/preferences system
- [ ] Recent URLs history
- [ ] Favorite blogs quick access
- [ ] Keyboard shortcuts
- [ ] Dark mode theme

### [ ] Distribution
- [ ] PyPI package publication
- [ ] Snap package for Linux
- [ ] Flatpak package
- [ ] Windows installer (.exe)
- [ ] macOS application bundle (.app)
- [ ] AUR package (Arch Linux)

### [ ] Additional Languages
- [ ] French translation
- [ ] German translation
- [ ] Portuguese translation
- [ ] Italian translation
- [ ] Chinese translation

---

## 🐛 Bug Fixes & Maintenance (ONGOING)

### [~] Known Issues
- [x] PyQt5 dependency installation
- [x] Virtual environment setup
- [ ] Handle blogs with authentication
- [ ] Support for lazy-loaded images
- [ ] Handle infinite scroll blogs

### [ ] Testing
- [ ] Unit tests for core functions
- [ ] Integration tests for full workflow
- [ ] GUI automated testing
- [ ] Cross-platform testing
- [ ] Different blog platform testing

### [ ] Code Quality
- [ ] Type hints throughout codebase
- [ ] Docstring completion
- [ ] Code linting (pylint/flake8)
- [ ] Security audit
- [ ] Performance profiling

---

## 📊 Success Metrics

### Current Status
- ✅ CLI tool: Fully functional
- ✅ GUI tool: Fully functional
- ✅ Translations: English + Spanish complete
- ✅ Documentation: Comprehensive
- ✅ Test coverage: Basic functionality verified
- ✅ Date-based naming: **COMPLETED**
- ⏳ Full blog download: Not implemented

### Next Milestone Goals
1. ~~**Date-based naming**~~ - ✅ **COMPLETED**
2. **Full blog download** - Core feature for complete blog archiving
3. **Blogger platform optimization** - Priority for user's specific need

---

## 🎯 Immediate Next Steps (For New Session)

1. ~~**Implement Date Extraction**~~ - ✅ **COMPLETED**
   - ✅ Parse publication date from blog HTML
   - ✅ Format: `YYYYMMDD-post-slug`
   - ✅ Test with: `https://facilitarelsoftwarelibre.blogspot.com/2023/11/como-configurar-la-cartera-kwallet-de-KDE.html`
   - ✅ Result: Successfully extracted date 2023-07-16

2. **Implement Full Blog Downloader**
   - Parse all posts from `https://washingtonindacochea.blogspot.com/`
   - Download each post with date-based naming
   - Add progress tracking
   - Create index/table of contents

3. **Update GUI**
   - Add "Download Entire Blog" button/mode
   - ✅ Add date prefix option checkbox
   - ✅ Show batch download progress

4. **Update CLI**
   - Add `--full-blog` flag
   - ✅ Add `--add-date` flag
   - ✅ Update documentation

---

## 📝 Notes

- Focus on Blogger platform first (user's primary use case)
- Maintain backward compatibility with existing features
- Keep internationalization for all new features
- Update all documentation with new features
- Test with real blogs before marking complete

---

**Last Updated:** 2026-10-16
**Current Version:** 1.1.0 (CLI + GUI + i18n + Date-based naming)
**Next Version:** 1.2.0 (Full blog download)
