---
title: MethodHandles.reflectAs()
permalink: Java/MethodHandles/reflectAs
date: 2021-01-11
key: JavaJava.M.MethodHandles
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandles.metodos valor="reflectAs" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T extends Member>T reflectAs(Class<T> expected, MethodHandle target)
~~~

## Parámetros
* **MethodHandle target**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle target" %}
* **Class&lt;T&gt; expected**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> expected" %}

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
