using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Welcome to BMI Calc! Please input your height in cm.");
            double height = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Now please input your weight in kg.");
            double weight = Convert.ToDouble(Console.ReadLine());

            var currentDate = DateTime.Now;
            
            double BMI = Math.Round(weight * weight / height, 2);
            Console.WriteLine($"{Environment.NewLine}Hello, on {currentDate:d} at {currentDate:t}, your BMI is {BMI}!");
            Console.Write($"{Environment.NewLine}Press any key to exit...");
            Console.ReadKey(true);
        }
    }
}
