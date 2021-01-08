---
title: BigInteger.BigInteger()
permalink: Java/BigInteger/BigInteger
date: 2021-01-04
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
* **int off**,  {% include w3api/param_description.html metodo=_data parametro="int off" %}
* **int radix**,  {% include w3api/param_description.html metodo=_data parametro="int radix" %}
* **int certainty**,  {% include w3api/param_description.html metodo=_data parametro="int certainty" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **byte[] magnitude**,  {% include w3api/param_description.html metodo=_data parametro="byte[] magnitude" %}
* **int signum**,  {% include w3api/param_description.html metodo=_data parametro="int signum" %}
* **int bitLength**,  {% include w3api/param_description.html metodo=_data parametro="int bitLength" %}
* **Random rnd**,  {% include w3api/param_description.html metodo=_data parametro="Random rnd" %}
* **String val**,  {% include w3api/param_description.html metodo=_data parametro="String val" %}
* **byte[] val**,  {% include w3api/param_description.html metodo=_data parametro="byte[] val" %}
* **int numBits**,  {% include w3api/param_description.html metodo=_data parametro="int numBits" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NumberFormatException](/Java/NumberFormatException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[BigInteger](/Java/BigInteger/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BigInteger.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
