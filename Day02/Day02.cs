class Program
{
    private static void Main()
    {
        string[] reports = File.ReadAllLines("reports.txt");
        int safeReports = 0;

        foreach (string report in reports)
        {
            string[] levels = report.Split(' ', StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries);

            if (IsReportSafe(levels))
            {
                safeReports++;
            }
            else if (IsReportSafeWithDampener(levels))
            {
                safeReports++;
            }
        }

        Console.WriteLine($"Number of safe reports -> {safeReports} out of {reports.Length} total");
    }

    private static bool IsReportSafe(string[] levels)
    {
        string direction = null;

        for (int i = 0; i < levels.Length - 1; i++)
        {
            int currentLevel = int.Parse(levels[i]);
            int nextLevel = int.Parse(levels[i + 1]);
            int difference = Math.Abs(currentLevel - nextLevel);

            if (difference < 1 || difference > 3)
            {
                return false;
            }

            if (direction == null)
            {
                direction = currentLevel < nextLevel ? "Ascending" : "Descending";
            }
            else
            {
                if ((direction == "Ascending" && currentLevel > nextLevel) || (direction == "Descending" && currentLevel < nextLevel))
                {
                    return false;
                }
            }
        }

        return true;
    }

    private static bool IsReportSafeWithDampener(string[] levels)
    {
        for (int i = 0; i < levels.Length; i++)
        {
            var newLevels = levels.Where((val, index) => index != i).ToArray();
            if (IsReportSafe(newLevels))
            {
                return true;
            }
        }
        return false;
    }
}
