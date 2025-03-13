using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;    // 添加这个命名空间以使用UI组件


public class PlayerMove : MonoBehaviour
{
    public int score = 0;
    public Rigidbody rb;
    public Text scoreText;
    public GameObject winText;    // 注意这里要设置激活与否，所以这里声明的是它的父类-GameObject
    void Start()
    {
        rb = GetComponent<Rigidbody>();
        Debug.Log("start the game !");
    }


    void Update()
    {
        float force_h = Input.GetAxis("Horizontal");
        float force_v = Input.GetAxis("Vertical");
        rb.AddForce(new Vector3(force_h, 0, force_v) * 50);
    }

    private void OnTriggerEnter(Collider other)
    {
        Debug.Log("发生了碰撞");
        if (other.gameObject.tag == "Food")
        {   
            Destroy(other.gameObject);
            score++;
            Debug.Log("当前得分：" + score);
            scoreText.text = "当前得分：" + score;
        }

        if (score == 7)
        {
            Debug.Log("win!!!");
            winText.SetActive(true);
        }

    }
}
