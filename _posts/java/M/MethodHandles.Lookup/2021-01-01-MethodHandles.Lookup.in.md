---
title: MethodHandles.Lookup.in()
permalink: /Java/MethodHandles/Lookup/in/
date: 2021-01-11
key: Java.M.MethodHandles.Lookup
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandles.Lookup.metodos valor="in" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MethodHandles.Lookup in(Class<?> requestedLookupClass)
~~~

## Parámetros
* **Class&lt;?&gt; requestedLookupClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> requestedLookupClass" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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
