import java.lang.reflect.Field;

class Edit
{
	public static void main(String[] args)
	{
		Main c = new Main();
		Game g = new Game(900, 568);
		Field[] fields = Main.class.getDeclaredFields();
		Field[] gams = Game.class.getDeclaredFields();

		try
		{
			gams[11].setAccessible(true);
			gams[11].set(g, true);
			fields[2].setAccessible(true);
			fields[2].set(c, g);
			c.main(null);
		} catch (Exception e) {}
		
	}
}
