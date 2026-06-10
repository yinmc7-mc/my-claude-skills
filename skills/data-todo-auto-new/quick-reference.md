# Quick Reference: Data Todo Auto New

## Quick Start

### Create Monthly Todo List
```bash
node ~/.agents/skills/data-todo-auto-new/scripts/generate-monthly-todo.js <month>
```

**Examples:**
```bash
# Create April todo list
node ~/.agents/skills/data-todo-auto-new/scripts/generate-monthly-todo.js 4

# Create May todo list  
node ~/.agents/skills/data-todo-auto-new/scripts/generate-monthly-todo.js 5
```

## How It Works

1. **Calculates Weeks**: Automatically determines Monday-Sunday weeks for the month
2. **Handles Cross-Month**: Includes next month's dates if needed (e.g., 4.27-5.3)
3. **Generates HTML**: Creates properly formatted HTML with 24px headers, bold dates, checklists
4. **Creates AppleScript**: Generates script to insert into Apple Notes
5. **Executes Automatically**: Runs AppleScript to create note in your "备忘录"

## Output Format

```
【4月】
第1周（4.1-4.5）
4.1（三）
- [ ]
- [ ]
- [ ]
...
```

## Verification

After running the script:

1. **Open Notes app** on your Mac
2. **Look for** note titled `【X月】` in "备忘录" folder
3. **Check formatting**:
   - Month header should be large (24px)
   - Week headers should be large (24px)
   - Dates should be bold
   - Items should be empty checkboxes

## Troubleshooting

### Note Not Visible
- Restart Notes app
- Wait a few seconds for iCloud sync
- Check "Recently Deleted" folder

### Formatting Shows HTML Tags
- HTML generation error - check console output
- Try running script again

### Wrong Weekday Indicators
- Calendar calculation may need adjustment
- Verify system date/time settings

## Manual AppleScript Execution

If automatic execution fails, run manually:

```bash
osascript /tmp/create_month_todo.applescript
```

## Customization

### Modify Checklist Items
Edit `generate-monthly-todo.js` line 76-78 to change default number of items per day:

```javascript
html += `<ul>\n`;
html += `<li></li>\n`;  // Add more lines for more items
html += `</ul>\n`;
```

### Change Formatting
Modify HTML templates in `generate-monthly-todo.js` function `generateHTML()`:

```javascript
html += `<div><b><span style="font-size: 24px">${month}</span></b>...`;
```

## Integration with Claude Code

When this skill is invoked, Claude will:

1. Parse your request (e.g., "创建4月待办清单")
2. Extract month number (4)
3. Run the Node.js script
4. Report success/failure
5. Provide troubleshooting if needed