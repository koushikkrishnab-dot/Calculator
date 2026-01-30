class Calculator
{
  public static void main(String args[])
  {
    int n1=Integer.parseInt(args[0]);
    int n2=Integer.parseInt(args[1]);
    int r1=n1+n2;
    int r2=n1-n2;
    int r3=n1*n2;
    int r4=n1/n2;
    System.out.println("Addition: "+r1);
    System.out.println("Subtraction: "+r2);
    System.out.println("Multiplication: "+r3);
    System.out.println("Division: "+r4);
  }
}
  
