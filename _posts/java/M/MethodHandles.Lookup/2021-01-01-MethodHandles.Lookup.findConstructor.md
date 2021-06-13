---
title: MethodHandles.Lookup.findConstructor()
permalink: Java/MethodHandles/Lookup/findConstructor
date: 2021-01-11
key: JavaJava.M.MethodHandles.Lookup
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandles.Lookup.metodos valor="findConstructor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MethodHandle findConstructor(Class<?> refc, MethodType type) throws NoSuchMethodException, IllegalAccessException
~~~

## Parámetros
* **Class&lt;?&gt; refc**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> refc" %}
* **MethodType type**,  {% include w3api/param_description.html metodo=_dato parametro="MethodType type" %}

## Excepciones
[NoSuchMethodException](/Java/NoSuchMethodException/), [SecurityException](/Java/SecurityException/), [IllegalAccessException](/Java/IllegalAccessException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[MethodHandles.Lookup](/Java/MethodHandles/Lookup/)

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
