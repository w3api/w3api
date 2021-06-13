---
title: MethodHandles.loop()
permalink: /Java/MethodHandles/loop/
date: 2021-01-11
key: Java.M.MethodHandles
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandles.metodos valor="loop" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MethodHandle loop(MethodHandle[]... clauses)
~~~

## Parámetros
* **MethodHandle[]... clauses**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle[]... clauses" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
