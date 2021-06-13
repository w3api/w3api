---
title: Introspector.flushFromCaches()
permalink: /Java/Introspector/flushFromCaches/
date: 2021-01-11
key: Java.I.Introspector
category: Java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.Introspector.metodos valor="flushFromCaches" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void flushFromCaches(Class<?> clz)
~~~

## Parámetros
* **Class&lt;?&gt; clz**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> clz" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Introspector](/Java/Introspector/)

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
