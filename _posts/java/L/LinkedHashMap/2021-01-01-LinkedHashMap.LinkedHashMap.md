---
title: LinkedHashMap.LinkedHashMap()
permalink: Java/LinkedHashMap/LinkedHashMap
date: 2021-01-11
key: Java.L.LinkedHashMap
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LinkedHashMap.constructores valor="LinkedHashMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LinkedHashMap()
public LinkedHashMap(int initialCapacity)
public LinkedHashMap(int initialCapacity, float loadFactor)
public LinkedHashMap(int initialCapacity, float loadFactor, boolean accessOrder)
public LinkedHashMap(Map<? extends K,? extends V> m)
~~~

## Parámetros
* **boolean accessOrder**,  {% include w3api/param_description.html metodo=_dato parametro="boolean accessOrder" %}
* **Map&lt;? extends K**,  {% include w3api/param_description.html metodo=_dato parametro="Map<? extends K" %}
* **int initialCapacity**,  {% include w3api/param_description.html metodo=_dato parametro="int initialCapacity" %}
* **float loadFactor**,  {% include w3api/param_description.html metodo=_dato parametro="float loadFactor" %}
* **? extends V&gt; m**,  {% include w3api/param_description.html metodo=_dato parametro="? extends V> m" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[LinkedHashMap](/Java/LinkedHashMap/)

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
