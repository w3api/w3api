---
title: ConcurrentHashMap.forEachEntry()
permalink: Java/ConcurrentHashMap/forEachEntry
date: 2021-01-04
key: JavaJava.C.ConcurrentHashMap
category: java
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
* **V&gt;**,  {% include w3api/param_description.html metodo=_data parametro="V>" %}
* **long parallelismThreshold**,  {% include w3api/param_description.html metodo=_data parametro="long parallelismThreshold" %}
* **Consumer&lt;? super U&gt; action**,  {% include w3api/param_description.html metodo=_data parametro="Consumer<? super U> action" %}
* **Function&lt;Map.Entry&lt;K**,  {% include w3api/param_description.html metodo=_data parametro="Function<Map.Entry<K" %}
* **V&gt;&gt; action**,  {% include w3api/param_description.html metodo=_data parametro="V>> action" %}
* **? extends U&gt; transformer**,  {% include w3api/param_description.html metodo=_data parametro="? extends U> transformer" %}
* **Consumer&lt;? super Map.Entry&lt;K**,  {% include w3api/param_description.html metodo=_data parametro="Consumer<? super Map.Entry<K" %}

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
