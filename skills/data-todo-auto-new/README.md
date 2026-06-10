# Data Todo Auto New - Skill Documentation

## Overview

Automatically creates monthly todo lists in Apple Notes with standardized formatting. This skill generates well-structured monthly plans organized by weeks (Monday-Sunday) and days, handling cross-month periods correctly.

## Features

✅ **Automatic Week Calculation**: Generates Monday-Sunday weeks for any month
✅ **Proper Formatting**: 24px large text for headers, bold dates, checklist items
✅ **Cross-Month Support**: Handles weeks spanning multiple months
✅ **Apple Notes Integration**: Direct creation in your "备忘录" folder
✅ **Duplicate Handling**: Automatically replaces existing monthly notes
✅ **Year 2026 Support**: Pre-configured calendar data for 2026

## When to Use

Use this skill when you need to:
- Create a new monthly planning document in Apple Notes
- Maintain consistent formatting across monthly todo lists
- Structure your month by weeks (Monday-Sunday pattern)
- Replace an existing monthly note with fresh structure

## Usage

### Basic Usage
```bash
# Using the script directly
node ~/.agents/skills/data-todo-auto-new/scripts/generate-monthly-todo.js <month>

# Example: Create April todo list
node ~/.agents/skills/data-todo-auto-new/scripts/generate-monthly-todo.js 4

# Example: Create May todo list
node ~/.agents/skills/data-todo-auto-new/scripts/generate-monthly-todo.js 5
```

### Via Claude Code

When interacting with Claude Code, simply say:
- "创建4月的待办清单"
- "Generate May todo list"
- "New monthly plan for June"

Claude will invoke this skill automatically based on these triggers.

## Output Format

The generated note follows this exact structure:

```
【X月】
第1周（M.D-M.D）
X.D（星期）
- [ ]
- [ ]
- [ ]
...
```

**Formatting Details:**
- Month header: 24px large bold text
- Week headers: 24px large bold text with date range
- Date headers: Bold text with weekday indicator
- Todo items: Empty checklist boxes (☐)

## 2026 Month Templates

### April 2026
- Week 1: 4.1-4.5 (周三-周日)
- Week 2: 4.6-4.12 (周一-周日)
- Week 3: 4.13-4.19 (周一-周日)
- Week 4: 4.20-4.26 (周一-周日)
- Week 5: 4.27-5.3 (周一-周日, includes May dates)

### May 2026
- Week 1: 5.4-5.10 (周一-周日)
- Week 2: 5.11-5.17 (周一-周日)
- Week 3: 5.18-5.24 (周一-周日)
- Week 4: 5.25-5.31 (周一-周日)

## File Structure

```
~/.agents/skills/data-todo-auto-new/
├── SKILL.md                              # Main skill instructions
├── README.md                             # This file
├── quick-reference.md                     # Quick start guide
└── scripts/
    └── generate-monthly-todo.js          # Main generation script
```

## Technical Details

### HTML Format Used

```html
<div><b><span style="font-size: 24px">【X月】</span></b><br></div>
<div><br></div>
<div><b><span style="font-size: 24px">第X周（M.D-M.D）</span></b><br></div>
<div><b>M.D（星期）</b><br></div>
<ul>
<li></li>
<li></li>
<li></li>
</ul>
```

### AppleScript Process

1. **Delete existing note** (if `【X月】` already exists)
2. **Create new note** in "我的Mac" account → "Notes" folder
3. **Set title** to `【X月】`
4. **Set body** to generated HTML content
5. **Return status** to user

### Node.js Script

- **ESM syntax**: Modern import/export
- **Date calculations**: JavaScript Date object
- **Week logic**: Monday-Sunday pattern
- **HTML generation**: Template literals
- **AppleScript execution**: child_process.execSync()

## Requirements

- **macOS**: Apple Notes app
- **Node.js**: v24+ (for ESM support)
- **Permissions**: Full disk access for Apple Notes
- **Account**: "我的Mac" account with "Notes" folder

## Troubleshooting

### Note Not Appearing

**Symptom**: Script runs successfully but note not visible in Notes app

**Solutions**:
1. Restart Notes app
2. Check "Recently Deleted" folder
3. Wait for iCloud sync (if using)
4. Verify account name is "我的Mac"

### Formatting Issues

**Symptom**: HTML tags visible in note

**Solutions**:
1. Check console output for errors
2. Verify HTML generation (check `/tmp/create_month_todo.applescript`)
3. Run AppleScript manually: `osascript /tmp/create_month_todo.applescript`

### Wrong Weekday Indicators

**Symptom**: Day doesn't match actual weekday

**Solutions**:
1. Verify system date/time settings
2. Check timezone configuration
3. Ensure 2026 calendar is correct

### Permission Errors

**Symptom**: Apple Notes permission denied

**Solutions**:
1. Open System Preferences → Security & Privacy → Privacy
2. Add Terminal to Full Disk Access
3. Restart Notes app

## Testing

### Test Script
```bash
# Test with May 2026
node ~/.agents/skills/data-todo-auto-new/scripts/generate-monthly-todo.js 5

# Verify note creation
osascript -e 'tell application "Notes" to get name of every note of folder "Notes" of account "我的Mac"' | grep "【5月】"
```

### Manual AppleScript Execution
```bash
# Generate AppleScript only
node ~/.agents/skills/data-todo-auto-new/scripts/generate-monthly-todo.js 5 > /tmp/test.applescript

# Execute manually
osascript /tmp/test.applescript
```

## Extending the Skill

### Add Custom Item Templates

Edit `scripts/generate-monthly-todo.js` line 76-78:

```javascript
html += `<ul>\n`;
html += `<li>Priority task</li>\n`;
html += `<li>Meeting</li>\n`;
html += `<li>Learning</li>\n`;
html += `</ul>\n`;
```

### Add Additional Months

The script automatically handles any month (1-12). For specific year adjustments, modify the year in line 17:

```javascript
const currentYear = new Date().getFullYear(); // Change to fixed year if needed
```

### Change Font Sizes

Modify the `font-size` value in the HTML templates:

```javascript
html += `<div><b><span style="font-size: 32px">${month}</span></b>...`;
```

## Support

For issues or questions:
1. Check this README for common problems
2. Review quick-reference.md for usage examples
3. Examine SKILL.md for detailed instructions
4. Verify Apple Notes permissions

## Changelog

### Version 1.0 (2026-04-01)
- Initial release
- Support for 2026 calendar
- Automatic week calculation (Monday-Sunday)
- Cross-month period handling
- Apple Notes integration
- HTML formatting with 24px headers
- Checklist format (3 items per day)
- Automatic duplicate replacement