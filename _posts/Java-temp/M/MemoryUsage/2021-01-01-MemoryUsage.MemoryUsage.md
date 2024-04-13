---
title: MemoryUsage.MemoryUsage()
permalink: /Java/MemoryUsage/MemoryUsage/
date: 2021-01-11
key: Java.M.MemoryUsage
category: Java
tags: ['java se', 'java.lang.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MemoryUsage.constructores valor="MemoryUsage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MemoryUsage(long init, long used, long committed, long max)
~~~

## Parámetros
* **long used**,  {% include w3api/param_description.html metodo=_dato parametro="long used" %}
* **long init**,  {% include w3api/param_description.html metodo=_dato parametro="long init" %}
* **long committed**,  {% include w3api/param_description.html metodo=_dato parametro="long committed" %}
* **long max**,  {% include w3api/param_description.html metodo=_dato parametro="long max" %}

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
