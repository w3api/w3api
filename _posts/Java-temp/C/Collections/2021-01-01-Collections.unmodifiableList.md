---
title: Collections.unmodifiableList()
permalink: /Java/Collections/unmodifiableList/
date: 2021-01-11
key: Java.C.Collections
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="unmodifiableList" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> List<T> unmodifiableList(List<? extends T> list)
~~~

## Parámetros
* **List&lt;? extends T&gt; list**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends T> list" %}

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
