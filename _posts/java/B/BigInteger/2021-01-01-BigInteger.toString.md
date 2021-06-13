---
title: BigInteger.toString()
permalink: /Java/BigInteger/toString/
date: 2021-01-11
key: Java.B.BigInteger
category: java
tags: ['java se', 'java.math', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BigInteger.metodos valor="toString" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public String toString()
public String toString(int radix)
~~~

## Parámetros
* **int radix**,  {% include w3api/param_description.html metodo=_dato parametro="int radix" %}

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
