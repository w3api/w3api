---
title: MemoryUsage.from()
permalink: /Java/MemoryUsage/from/
date: 2021-01-11
key: Java.M.MemoryUsage
category: Java
tags: ['java se', 'java.lang.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MemoryUsage.metodos valor="from" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MemoryUsage from(CompositeData cd)
~~~

## Parámetros
* **CompositeData cd**,  {% include w3api/param_description.html metodo=_dato parametro="CompositeData cd" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MemoryUsage](/Java/MemoryUsage/)

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
