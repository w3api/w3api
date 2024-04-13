---
title: Collections.fill()
permalink: /Java/Collections/fill/
date: 2021-01-11
key: Java.C.Collections
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="fill" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> void fill(List<? super T> list, T obj)
~~~

## Parámetros
* **T obj**,  {% include w3api/param_description.html metodo=_dato parametro="T obj" %}
* **List&lt;? super T&gt; list**,  {% include w3api/param_description.html metodo=_dato parametro="List<? super T> list" %}

## Clase Padre
[Collections](/Java/Collections/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
