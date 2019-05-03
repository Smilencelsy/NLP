
package sentiment;

import com.hankcs.hanlp.HanLP;

import java.io.*;


public class Segment
{
    public static void main(String[] args) throws IOException
    {
        FileReader fr = new FileReader("data_phase2.txt");
        LineNumberReader reader = new LineNumberReader(fr);
        reader.skip(Long.MAX_VALUE);
        int lines = reader.getLineNumber();
        System.out.println(lines);
        reader.close();
        fr = new FileReader("data_phase2.txt");
        BufferedReader br = new BufferedReader(fr);

        for(int i = 0  ; i < lines; i++){
            String str = br.readLine();
            String[] block = str.split(" ");
            String block_1 = HanLP.segment(block[1]).toString();
            FileWriter fw = new FileWriter("data_phase3.txt",true);
            PrintWriter pw = new PrintWriter(fw);
            pw.write(block[0]+" "+block_1+" "+block[2]+"\n");
            pw.flush();
            fw.flush();
            fw.close();
            pw.close();
        }


        //System.out.println(HanLP.segment("你好，欢迎使用HanLP汉语处理包！"));

    }
}