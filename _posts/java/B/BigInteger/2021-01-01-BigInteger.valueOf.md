---
title: BigInteger.valueOf()
permalink: /Java/BigInteger/valueOf/
date: 2021-01-11
key: Java.B.BigInteger
category: Java
tags: ['java se', 'java.math', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BigInteger.metodos valor="valueOf" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static BigInteger valueOf(long val)
~~~

## Parámetros
* **long val**,  {% include w3api/param_description.html metodo=_dato parametro="long val" %}

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
