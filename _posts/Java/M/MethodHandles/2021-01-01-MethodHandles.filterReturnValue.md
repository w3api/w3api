---
title: MethodHandles.filterReturnValue()
permalink: /Java/MethodHandles/filterReturnValue/
date: 2021-01-11
key: Java.M.MethodHandles
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandles.metodos valor="filterReturnValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MethodHandle filterReturnValue(MethodHandle target, MethodHandle filter)
~~~

## Parámetros
* **MethodHandle target**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle target" %}
* **MethodHandle filter**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle filter" %}

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
