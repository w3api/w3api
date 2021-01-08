---
title: ConcurrentHashMap.ConcurrentHashMap()
permalink: Java/ConcurrentHashMap/ConcurrentHashMap
date: 2021-01-04
key: JavaJava.C.ConcurrentHashMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.constructores valor="ConcurrentHashMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ConcurrentHashMap()
public ConcurrentHashMap(int initialCapacity)
public ConcurrentHashMap(int initialCapacity, float loadFactor)
public ConcurrentHashMap(int initialCapacity, float loadFactor, int concurrencyLevel)
public ConcurrentHashMap(Map<? extends K,? extends V> m)
~~~

## Parámetros
* **float loadFactor**,  {% include w3api/param_description.html metodo=_data parametro="float loadFactor" %}
* **int concurrencyLevel**,  {% include w3api/param_description.html metodo=_data parametro="int concurrencyLevel" %}
* **? extends V&gt; m**,  {% include w3api/param_description.html metodo=_data parametro="? extends V> m" %}
* **int initialCapacity**,  {% include w3api/param_description.html metodo=_data parametro="int initialCapacity" %}
* **Map&lt;? extends K**,  {% include w3api/param_description.html metodo=_data parametro="Map<? extends K" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ConcurrentHashMap](/Java/ConcurrentHashMap/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConcurrentHashMap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
