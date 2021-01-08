---
title: ConcurrentSkipListMap.ConcurrentSkipListMap()
permalink: Java/ConcurrentSkipListMap/ConcurrentSkipListMap
date: 2021-01-04
key: JavaJava.C.ConcurrentSkipListMap
category: java
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
* **Comparator&lt;? super K&gt; comparator**,  {% include w3api/param_description.html metodo=_data parametro="Comparator<? super K> comparator" %}
* **? extends V&gt; m**,  {% include w3api/param_description.html metodo=_data parametro="? extends V> m" %}
* **Map&lt;? extends K**,  {% include w3api/param_description.html metodo=_data parametro="Map<? extends K" %}
* **SortedMap&lt;K**,  {% include w3api/param_description.html metodo=_data parametro="SortedMap<K" %}

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
{%- for _ldc in site.data.Java.C.ConcurrentSkipListMap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
