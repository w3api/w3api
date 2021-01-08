---
title: BigInteger.modPow()
permalink: Java/BigInteger/modPow
date: 2021-01-04
key: JavaJava.B.BigInteger
category: java
tags: ['java se', 'java.math', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BigInteger.metodos valor="modPow" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BigInteger modPow(BigInteger exponent, BigInteger m)
~~~

## Parámetros
* **BigInteger m**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger m" %}
* **BigInteger exponent**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger exponent" %}

## Excepciones
[ArithmeticException](/Java/ArithmeticException/)

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
