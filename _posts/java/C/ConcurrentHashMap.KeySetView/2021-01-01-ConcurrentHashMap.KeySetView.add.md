---
title: ConcurrentHashMap.KeySetView.add()
permalink: /Java/ConcurrentHashMap/KeySetView/add/
date: 2021-01-11
key: Java.C.ConcurrentHashMap.KeySetView
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.KeySetView.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean add(K e)
~~~

## Parámetros
* **K e**,  {% include w3api/param_description.html metodo=_dato parametro="K e" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ConcurrentHashMap.KeySetView](/Java/ConcurrentHashMap/KeySetView/)

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
