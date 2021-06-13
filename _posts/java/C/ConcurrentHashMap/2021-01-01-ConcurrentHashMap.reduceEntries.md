---
title: ConcurrentHashMap.reduceEntries()
permalink: /Java/ConcurrentHashMap/reduceEntries/
date: 2021-01-11
key: Java.C.ConcurrentHashMap
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="reduceEntries" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Map.Entry<K,V> reduceEntries(long parallelismThreshold, BiFunction<Map.Entry<K,V>,Map.Entry<K,V>,? extends Map.Entry<K,V>> reducer)
<U> U reduceEntries(long parallelismThreshold, Function<Map.Entry<K,V>,? extends U> transformer, BiFunction<? super U,? super U,? extends U> reducer)
~~~

## Parámetros
* **V&gt;&gt; reducer**,  {% include w3api/param_description.html metodo=_dato parametro="V>> reducer" %}
* **Function&lt;Map.Entry&lt;K**,  {% include w3api/param_description.html metodo=_dato parametro="Function<Map.Entry<K" %}
* **V&gt;**,  {% include w3api/param_description.html metodo=_dato parametro="V>" %}
* **? super U**,  {% include w3api/param_description.html metodo=_dato parametro="? super U" %}
* **BiFunction&lt;Map.Entry&lt;K**,  {% include w3api/param_description.html metodo=_dato parametro="BiFunction<Map.Entry<K" %}
* **long parallelismThreshold**,  {% include w3api/param_description.html metodo=_dato parametro="long parallelismThreshold" %}
* **BiFunction&lt;? super U**,  {% include w3api/param_description.html metodo=_dato parametro="BiFunction<? super U" %}
* **? extends U&gt; reducer**,  {% include w3api/param_description.html metodo=_dato parametro="? extends U> reducer" %}
* **? extends Map.Entry&lt;K**,  {% include w3api/param_description.html metodo=_dato parametro="? extends Map.Entry<K" %}
* **Map.Entry&lt;K**,  {% include w3api/param_description.html metodo=_dato parametro="Map.Entry<K" %}
* **? extends U&gt; transformer**,  {% include w3api/param_description.html metodo=_dato parametro="? extends U> transformer" %}

## Clase Padre
[ConcurrentHashMap](/Java/ConcurrentHashMap/)

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
