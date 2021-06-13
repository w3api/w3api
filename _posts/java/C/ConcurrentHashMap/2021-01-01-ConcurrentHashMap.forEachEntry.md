---
title: ConcurrentHashMap.forEachEntry()
permalink: /Java/ConcurrentHashMap/forEachEntry/
date: 2021-01-11
key: Java.C.ConcurrentHashMap
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="forEachEntry" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void forEachEntry(long parallelismThreshold, Consumer<? super Map.Entry<K,V>> action)
<U> void forEachEntry(long parallelismThreshold, Function<Map.Entry<K,V>,? extends U> transformer, Consumer<? super U> action)
~~~

## Parámetros
* **Consumer&lt;? super U&gt; action**,  {% include w3api/param_description.html metodo=_dato parametro="Consumer<? super U> action" %}
* **V&gt;&gt; action**,  {% include w3api/param_description.html metodo=_dato parametro="V>> action" %}
* **Function&lt;Map.Entry&lt;K**,  {% include w3api/param_description.html metodo=_dato parametro="Function<Map.Entry<K" %}
* **V&gt;**,  {% include w3api/param_description.html metodo=_dato parametro="V>" %}
* **Consumer&lt;? super Map.Entry&lt;K**,  {% include w3api/param_description.html metodo=_dato parametro="Consumer<? super Map.Entry<K" %}
* **long parallelismThreshold**,  {% include w3api/param_description.html metodo=_dato parametro="long parallelismThreshold" %}
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
