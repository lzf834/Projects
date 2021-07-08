using System;

namespace C_dotnet_playarea
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello and welcome to the C# number guessing game");
            Console.WriteLine("Please enter your name!");
            string name = Console.ReadLine();

            int maxTries = 10;
            int tries = 0;

            Random rnd = new Random();
            int randomNum = rnd.Next(1, 100);

            Console.WriteLine("Hi " + name + "!" + " Guess a number between 1 and 100");

            while (tries < maxTries) {
                string answer = Console.ReadLine();
                int numAnswer = Int16.Parse(answer);

                if (numAnswer == randomNum) {
                    Console.WriteLine("Congratulations " + name + "!" + " You guessed it!");
                    Console.WriteLine("Press any key to continue");
                    Console.ReadLine();
                    return;
                } else if (numAnswer < randomNum) {
                    Console.WriteLine("Sorry " + name + "!" + " That's not the right answer, try something higher!");
                    Console.WriteLine("You have " + (maxTries-1) + " chances left");
                } else if (numAnswer > randomNum) {
                    Console.WriteLine("Sorry " + name + "!" + " That's not the right answer, try something lower!");
                    Console.WriteLine("You have " + (maxTries-1) + " chances left");                    
                }

                maxTries--;
            }

            Console.WriteLine("Sorry " + name + "!" + " You have used up all your tries!");
            Console.WriteLine("Press any key to continue");
            Console.ReadLine();
        }
    }
}
