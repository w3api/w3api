---
title: BigDecimal.BigDecimal()
permalink: Java/BigDecimal/BigDecimal
date: 2021-01-04
key: JavaJava.B.BigDecimal
category: java
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
* **char[] in**,  {% include w3api/param_description.html metodo=_data parametro="char[] in" %}
* **BigInteger unscaledVal**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger unscaledVal" %}
* **BigInteger val**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger val" %}
* **MathContext mc**,  {% include w3api/param_description.html metodo=_data parametro="MathContext mc" %}
* **long val**,  {% include w3api/param_description.html metodo=_data parametro="long val" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **String val**,  {% include w3api/param_description.html metodo=_data parametro="String val" %}
* **int scale**,  {% include w3api/param_description.html metodo=_data parametro="int scale" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **int val**,  {% include w3api/param_description.html metodo=_data parametro="int val" %}
* **double val**,  {% include w3api/param_description.html metodo=_data parametro="double val" %}

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
{%- for _ldc in site.data.Java.B.BigDecimal.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
