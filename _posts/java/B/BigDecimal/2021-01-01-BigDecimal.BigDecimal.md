---
title: BigDecimal.BigDecimal()
permalink: /Java/BigDecimal/BigDecimal/
date: 2021-01-11
key: Java.B.BigDecimal
category: Java
tags: ['java se', 'java.math', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BigDecimal.constructores valor="BigDecimal" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BigDecimal(char[] in)
public BigDecimal(char[] in, int offset, int len)
public BigDecimal(char[] in, int offset, int len, MathContext mc)
public BigDecimal(char[] in, MathContext mc)
public BigDecimal(double val)
public BigDecimal(double val, MathContext mc)
public BigDecimal(int val)
public BigDecimal(int val, MathContext mc)
public BigDecimal(long val)
public BigDecimal(long val, MathContext mc)
public BigDecimal(String val)
public BigDecimal(String val, MathContext mc)
public BigDecimal(BigInteger val)
public BigDecimal(BigInteger unscaledVal, int scale)
public BigDecimal(BigInteger unscaledVal, int scale, MathContext mc)
public BigDecimal(BigInteger val, MathContext mc)
~~~

## Parámetros
* **long val**,  {% include w3api/param_description.html metodo=_dato parametro="long val" %}
* **String val**,  {% include w3api/param_description.html metodo=_dato parametro="String val" %}
* **BigInteger unscaledVal**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger unscaledVal" %}
* **MathContext mc**,  {% include w3api/param_description.html metodo=_dato parametro="MathContext mc" %}
* **BigInteger val**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger val" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **char[] in**,  {% include w3api/param_description.html metodo=_dato parametro="char[] in" %}
* **double val**,  {% include w3api/param_description.html metodo=_dato parametro="double val" %}
* **int scale**,  {% include w3api/param_description.html metodo=_dato parametro="int scale" %}
* **int val**,  {% include w3api/param_description.html metodo=_dato parametro="int val" %}

## Excepciones
[NumberFormatException](/Java/NumberFormatException/), [ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[BigDecimal](/Java/BigDecimal/)

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
