---
title: MethodHandles.filterReturnValue()
permalink: Java/MethodHandles/filterReturnValue
date: 2021-01-04
key: JavaJava.M.MethodHandles
category: java
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
* **MethodHandle target**,  {% include w3api/param_description.html metodo=_data parametro="MethodHandle target" %}
* **MethodHandle filter**,  {% include w3api/param_description.html metodo=_data parametro="MethodHandle filter" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MethodHandles](/Java/MethodHandles/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MethodHandles.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
