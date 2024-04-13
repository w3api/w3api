---
title: Collections.unmodifiableSortedMap()
permalink: /Java/Collections/unmodifiableSortedMap/
date: 2021-01-11
key: Java.C.Collections
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="unmodifiableSortedMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <K,V> SortedMap<K,V> unmodifiableSortedMap(SortedMap<K,? extends V> m)
~~~

## Parámetros
* **SortedMap&lt;K**,  {% include w3api/param_description.html metodo=_dato parametro="SortedMap<K" %}
* **? extends V&gt; m**,  {% include w3api/param_description.html metodo=_dato parametro="? extends V> m" %}

## Clase Padre
[Collections](/Java/Collections/)

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
