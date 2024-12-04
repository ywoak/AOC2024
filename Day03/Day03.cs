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
            MatchCollection ws = Regex.Matches(line, pattern);
            foreach (Match w in ws)
            {
                string p = @"([0-9]{1,3})";
                MatchCollection ms = Regex.Matches(w.Value, p);

                r += (int.Parse(ms[0].Value) * int.Parse(ms[1].Value));
            }
        }
        Console.WriteLine($"r -> {r}");
        //Part2(input);
    }

    private static void Part2(string[] input)
    {
        int r = 0;
        bool no_flag = false;

        string p = @"(don\'t\(\))|(do\(\))|(mul[(][0-9]{1,3}[,][0-9]{1,3}[)])";
        foreach (string l in input)
        {
            MatchCollection m = Regex.Matches(l, p);
            foreach (Match w in m)
            {
                switch (w.Value)
                {
                    case "don't()":
                        no_flag = true;
                        break;
                    case "do()":
                        no_flag = false;
                        break;
                    default:
                        if (no_flag == false)
                        {
                            string p2 = @"([0-9]{1,3})";
                            MatchCollection ms = Regex.Matches(w.Value, p2);

                            r += (int.Parse(ms[0].Value) * int.Parse(ms[1].Value));
                        }
                        break;
                }
            }
        }
        Console.WriteLine($"r -> {r}");
    }

}
