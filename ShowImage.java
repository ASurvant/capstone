import java.awt.*;
import java.io.*;
import javax.swing.*;
import java.util.*;
public class ShowImage extends JComponent
{
	Color[][] pixels;
	public static void main(String[] args)
	{
		new ShowImage();
	}
	public ShowImage()
	{
		try
		{
			Scanner s=new Scanner(new FileReader("image.txt"));
			int w=s.nextInt();
			int h=s.nextInt();
			pixels=new Color[w][h];
			for (int i=0; i<w; i++)
			{
				for (int j=0; j<h; j++)
				{
					pixels[i][j]=new Color(s.nextInt(),s.nextInt(),s.nextInt());
				}
			}
			JFrame f=new JFrame();
			f.setSize(w,h);
			f.add(this);
			f.setVisible(true);
			}catch(IOException e){
		}
	}
	public void paintComponent(Graphics g)
	{
		for(int i=0; i<pixels.length; i++)
			for (int j=0; j<pixels[0].length; j++)
			{
				g.setColor(pixels[i][j]);
				g.fillRect(i,j,1,1);
			}
	}
}