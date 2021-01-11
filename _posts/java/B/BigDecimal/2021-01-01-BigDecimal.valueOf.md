---
title: BigDecimal.valueOf()
permalink: Java/BigDecimal/valueOf
date: 2021-01-11
key: JavaJava.B.BigDecimal
category: java
tags: ['java se', 'java.math', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BigDecimal.metodos valor="valueOf" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static BigDecimal valueOf(double val)
public static BigDecimal valueOf(long val)
public static BigDecimal valueOf(long unscaledVal, int scale)
~~~

## Parámetros
* **long val**,  {% include w3api/param_description.html metodo=_dato parametro="long val" %}
* **double val**,  {% include w3api/param_description.html metodo=_dato parametro="double val" %}
* **int scale**,  {% include w3api/param_description.html metodo=_dato parametro="int scale" %}
* **long unscaledVal**,  {% include w3api/param_description.html metodo=_dato parametro="long unscaledVal" %}

## Excepciones
[NumberFormatException](/Java/NumberFormatException/)

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
