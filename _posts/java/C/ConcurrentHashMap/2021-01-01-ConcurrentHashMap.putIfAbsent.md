---
title: ConcurrentHashMap.putIfAbsent()
permalink: /Java/ConcurrentHashMap/putIfAbsent/
date: 2021-01-11
key: Java.C.ConcurrentHashMap
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="putIfAbsent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public V putIfAbsent(K key, V value)
~~~

## Parámetros
* **V value**,  {% include w3api/param_description.html metodo=_dato parametro="V value" %}
* **K key**,  {% include w3api/param_description.html metodo=_dato parametro="K key" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ConcurrentHashMap](/Java/ConcurrentHashMap/)

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
