function run() {
    var app = Application.currentApplication();
    app.includeStandardAdditions = true;
    var content = app.read(Path('/Users/egokoro/Desktop/タイピングソフト/index.html'));
    var match = content.match(/const typingData = (\{[\s\S]*?\});/);
    if (match) {
        var str = match[1];
        var idx = str.indexOf('\\<');
        if (idx !== -1) {
            var lines = str.substring(0, idx).split('\n');
            return "Line number in JSON: " + lines.length + " context: " + str.substring(idx-30, idx+30);
        }
    }
}
