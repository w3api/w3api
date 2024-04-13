---
title: ConcurrentMap.replace()
permalink: /Java/ConcurrentMap/replace/
date: 2021-01-11
key: Java.C.ConcurrentMap
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentMap.metodos valor="replace" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
V replace(K key, V value)
boolean replace(K key, V oldValue, V newValue)
~~~

## Parámetros
* **V value**,  {% include w3api/param_description.html metodo=_dato parametro="V value" %}
* **V newValue**,  {% include w3api/param_description.html metodo=_dato parametro="V newValue" %}
* **K key**,  {% include w3api/param_description.html metodo=_dato parametro="K key" %}
* **V oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="V oldValue" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/), [ClassCastException](/Java/ClassCastException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[ConcurrentMap](/Java/ConcurrentMap/)

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
