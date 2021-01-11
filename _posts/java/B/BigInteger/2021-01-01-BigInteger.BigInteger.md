---
title: BigInteger.BigInteger()
permalink: Java/BigInteger/BigInteger
date: 2021-01-11
key: JavaJava.B.BigInteger
category: java
tags: ['java se', 'java.math', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BigInteger.constructores valor="BigInteger" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BigInteger(byte[] val)
public BigInteger(byte[] val, int off, int len)
public BigInteger(int signum, byte[] magnitude)
public BigInteger(int signum, byte[] magnitude, int off, int len)
public BigInteger(int bitLength, int certainty, Random rnd)
public BigInteger(int numBits, Random rnd)
public BigInteger(String val)
public BigInteger(String val, int radix)
~~~

## Parámetros
* **int certainty**,  {% include w3api/param_description.html metodo=_dato parametro="int certainty" %}
* **int numBits**,  {% include w3api/param_description.html metodo=_dato parametro="int numBits" %}
* **byte[] val**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] val" %}
* **String val**,  {% include w3api/param_description.html metodo=_dato parametro="String val" %}
* **byte[] magnitude**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] magnitude" %}
* **int bitLength**,  {% include w3api/param_description.html metodo=_dato parametro="int bitLength" %}
* **int signum**,  {% include w3api/param_description.html metodo=_dato parametro="int signum" %}
* **Random rnd**,  {% include w3api/param_description.html metodo=_dato parametro="Random rnd" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **int radix**,  {% include w3api/param_description.html metodo=_dato parametro="int radix" %}
* **int off**,  {% include w3api/param_description.html metodo=_dato parametro="int off" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [NumberFormatException](/Java/NumberFormatException/), [ArithmeticException](/Java/ArithmeticException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[BigInteger](/Java/BigInteger/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
