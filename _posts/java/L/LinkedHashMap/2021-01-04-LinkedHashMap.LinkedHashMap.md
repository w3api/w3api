---
title: LinkedHashMap.LinkedHashMap()
permalink: Java/LinkedHashMap/LinkedHashMap
date: 2021-01-04
key: JavaJava.L.LinkedHashMap
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
* **boolean accessOrder**,  {% include w3api/param_description.html metodo=_data parametro="boolean accessOrder" %}
* **float loadFactor**,  {% include w3api/param_description.html metodo=_data parametro="float loadFactor" %}
* **? extends V&gt; m**,  {% include w3api/param_description.html metodo=_data parametro="? extends V> m" %}
* **int initialCapacity**,  {% include w3api/param_description.html metodo=_data parametro="int initialCapacity" %}
* **Map&lt;? extends K**,  {% include w3api/param_description.html metodo=_data parametro="Map<? extends K" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[LinkedHashMap](/Java/LinkedHashMap/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LinkedHashMap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
