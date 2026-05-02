class Solution {
    public String complexNumberMultiply(String a, String b) {
        int[] x = parse(a), y = parse(b);

        int real = x[0]*y[0] - x[1]*y[1];
        int imag = x[0]*y[1] + x[1]*y[0];

        return real + "+" + imag + "i";
    }

    private int[] parse(String s) {
        int plus = s.indexOf('+');
        int real = Integer.parseInt(s.substring(0, plus));
        int imag = Integer.parseInt(s.substring(plus + 1, s.length() - 1));
        return new int[]{real, imag};
    }
}