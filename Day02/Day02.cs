class Program
{
    private static void Main()
    {
        string[] reports = File.ReadAllLines("reports.txt");
        int safeReport = 0;
        int safeDampenerReport = 0;
        int mistake = 0;

        foreach (string report in reports)
        {
            string[] levels = report.Split(" ", StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries);
            // if (IsReportSafe(report))
            // {
            //     safeReport++;
            // }
            if (IsDampenerSafe(levels, mistake))
            {
                Console.WriteLine(report);
                safeDampenerReport++;
            }
        }
        Console.WriteLine($"Number of safe report -> {safeReport} out of -> {reports.Count()} total");
        Console.WriteLine($"Number of safe report with dampener suystem -> {safeDampenerReport} out of -> {reports.Count()} total");
    }

    private static bool IsReportSafe(string report)
    {
        string direction;

        string[] levels = report.Split(" ", StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries);

        if (levels[0] != null && levels[1] != null)
        {
            direction = int.Parse(levels[0]) > int.Parse(levels[1]) ? "Descending" : "Ascending";
        }
        else
        {
            throw new Exception("Something's wrong with the report");
        }

        for (int i = 0; i < levels.Count() - 1; i++)
        {
            int level = int.Parse(levels[i]);
            int next_level;
            int difference;

            if (levels[i + 1] != null)
            {
                next_level = int.Parse(levels[i + 1]);
                difference = Math.Abs(level - next_level);

                if (direction == "Ascending" && level > next_level)
                {
                    return false;
                }
                else if (direction == "Descending" && level < next_level)
                {
                    return false;
                }

                if (difference > 3 || difference == 0)
                {
                    return false;
                }

            }
        }
        return true;
    }

    private static bool SafeCheck(int level, int next_level, string direction)
    {
        int difference = Math.Abs(level - next_level);

        if (direction == "Ascending" && level > next_level)
        {
            return false;
        }
        else if (direction == "Descending" && level < next_level)
        {
            return false;
        }

        if (difference > 3 || difference == 0)
        {
            return false;
        }

        return true;
    }

    private static bool IsDampenerSafe(string[] levels, int mistake)
    {
        string direction;

        if (levels[0] != null && levels[1] != null)
        {
            direction = int.Parse(levels[0]) > int.Parse(levels[1]) ? "Descending" : "Ascending";
            Console.WriteLine($"direction -> {direction}");
        }
        else
        {
            throw new Exception("Something's wrong with the report");
        }

        for (int i = 0; i < levels.Count() - 1; i++)
        {
            int level = int.Parse(levels[i]);
            int next_level;

            Console.WriteLine($"level {level} has been parsed");
            if (i + 1 < levels.Count())
            {
                next_level = int.Parse(levels[i + 1]);
                Console.WriteLine($"next_level {next_level} has been parsed");
                if (!SafeCheck(level, next_level, direction))
                {
                    if (mistake == 0)
                    {
                        List<string> tmp = new List<string>(levels);
                        tmp.RemoveAt(i);
                        string[] new_levels = tmp.ToArray();
                        if (!IsDampenerSafe(new_levels, mistake + 1))
                        {
                            List<string> tmp_2 = new List<string>(levels);
                            tmp_2.RemoveAt(i + 1);
                            string[] new_levels_2 = tmp_2.ToArray();
                            return IsDampenerSafe(new_levels_2, mistake + 1);
                        }
                        else
                        {
                            return true;
                        }
                    }
                    else
                    {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}
