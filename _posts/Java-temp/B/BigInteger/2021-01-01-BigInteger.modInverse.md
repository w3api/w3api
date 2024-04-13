---
title: BigInteger.modInverse()
permalink: /Java/BigInteger/modInverse/
date: 2021-01-11
key: Java.B.BigInteger
category: Java
tags: ['java se', 'java.math', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BigInteger.metodos valor="modInverse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BigInteger modInverse(BigInteger m)
~~~

## Parámetros
* **BigInteger m**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger m" %}

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
