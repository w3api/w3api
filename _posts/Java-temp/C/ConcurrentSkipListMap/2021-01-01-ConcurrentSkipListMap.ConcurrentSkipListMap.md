---
title: ConcurrentSkipListMap.ConcurrentSkipListMap()
permalink: /Java/ConcurrentSkipListMap/ConcurrentSkipListMap/
date: 2021-01-11
key: Java.C.ConcurrentSkipListMap
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentSkipListMap.constructores valor="ConcurrentSkipListMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ConcurrentSkipListMap()
public ConcurrentSkipListMap(Comparator<? super K> comparator)
public ConcurrentSkipListMap(Map<? extends K,? extends V> m)
public ConcurrentSkipListMap(SortedMap<K,? extends V> m)
~~~

## Parámetros
* **Comparator&lt;? super K&gt; comparator**,  {% include w3api/param_description.html metodo=_dato parametro="Comparator<? super K> comparator" %}
* **SortedMap&lt;K**,  {% include w3api/param_description.html metodo=_dato parametro="SortedMap<K" %}
* **Map&lt;? extends K**,  {% include w3api/param_description.html metodo=_dato parametro="Map<? extends K" %}
* **? extends V&gt; m**,  {% include w3api/param_description.html metodo=_dato parametro="? extends V> m" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ConcurrentSkipListMap](/Java/ConcurrentSkipListMap/)

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
