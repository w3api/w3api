---
title: MethodHandles.spreadInvoker()
permalink: Java/MethodHandles/spreadInvoker
date: 2021-01-11
key: JavaJava.M.MethodHandles
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandles.metodos valor="spreadInvoker" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MethodHandle spreadInvoker(MethodType type, int leadingArgCount)
~~~

## Parámetros
* **MethodType type**,  {% include w3api/param_description.html metodo=_dato parametro="MethodType type" %}
* **int leadingArgCount**,  {% include w3api/param_description.html metodo=_dato parametro="int leadingArgCount" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[MethodHandles](/Java/MethodHandles/)

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
