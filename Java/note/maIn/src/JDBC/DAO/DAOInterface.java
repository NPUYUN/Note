package JDBC.DAO;

import java.util.List;

public interface DAOInterface {
    // 增加
    public void add(Human man);

    // 修改
    public void update(Human man);

    // 删除
    public void delete(Human man);

    // 获取
    public Human get(int id);

    // 查询
    public List<Human> search();
    // 分页查询
    public List<Human> search(int start , int end);
}
