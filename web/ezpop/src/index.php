<?php

class A
{
    public $ad1;
    public $ad2;

    function evil() {
        echo new $this->ad1($this->ad2);
    }

    public function __invoke()
    {
        $this->ad1->change();
    }
}

class B
{
    public $func;

    public function __destruct()
    {
        echo $this->func . 'Itisok';
    }

    public function sear()
    {
        ($this->func)();
    }

    public function __call($a, $b)
    {
        echo $this->func->get_flag();
    }

}

class C
{
    public $stt;

    public function __toString()
    {
        $this->stt->sear();
        return 'fine';
    }
}
class D
{
    public $args;

    public function sear()
    {
        ($this->args)();
    }

    public function get_flag()
    {
        eval('#' . $this->args);
    }

}

if (isset($_POST['cmd'])) {
    unserialize(base64_decode($_POST['cmd']));
} else {
    highlight_file(__FILE__);
}
