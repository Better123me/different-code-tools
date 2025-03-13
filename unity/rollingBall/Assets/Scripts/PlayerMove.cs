using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;    // �����������ռ���ʹ��UI���


public class PlayerMove : MonoBehaviour
{
    public int score = 0;
    public Rigidbody rb;
    public Text scoreText;
    public GameObject winText;    // ע������Ҫ���ü�������������������������ĸ���-GameObject
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
        Debug.Log("��������ײ");
        if (other.gameObject.tag == "Food")
        {   
            Destroy(other.gameObject);
            score++;
            Debug.Log("��ǰ�÷֣�" + score);
            scoreText.text = "��ǰ�÷֣�" + score;
        }

        if (score == 7)
        {
            Debug.Log("win!!!");
            winText.SetActive(true);
        }

    }
}
