using System.Text.RegularExpressions;

class Program
{
    public static void Main()
    {
        int r = 0;

        string[] input = File.ReadAllLines("input.txt");

        string pattern = @"(mul[(][0-9]{1,3}[,][0-9]{1,3}[)])";
        foreach (string line in input)
        {
            MatchCollection ws = Regex.Matches(line, pattern, RegexOptions.Multiline);
            foreach (Match w in ws)
            {
                string p = @"([0-9]{1,3})";
                MatchCollection ms = Regex.Matches(w.Value, p);

                r += (int.Parse(ms[0].Value) * int.Parse(ms[1].Value));
            }
        }
        Console.WriteLine($"r -> {r}");
    }
}
