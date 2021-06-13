---
title: BigInteger.divideAndRemainder()
permalink: /Java/BigInteger/divideAndRemainder/
date: 2021-01-11
key: Java.B.BigInteger
category: java
tags: ['java se', 'java.math', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BigInteger.metodos valor="divideAndRemainder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BigInteger[] divideAndRemainder(BigInteger val)
~~~

## Parámetros
* **BigInteger val**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger val" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
