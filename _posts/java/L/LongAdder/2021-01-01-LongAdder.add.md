---
title: LongAdder.add()
permalink: /Java/LongAdder/add/
date: 2021-01-11
key: Java.L.LongAdder
category: Java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LongAdder.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void add(long x)
~~~

## Parámetros
* **long x**,  {% include w3api/param_description.html metodo=_dato parametro="long x" %}

## Clase Padre
[LongAdder](/Java/LongAdder/)

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
