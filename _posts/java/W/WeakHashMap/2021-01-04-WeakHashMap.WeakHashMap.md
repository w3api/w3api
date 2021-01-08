---
title: WeakHashMap.WeakHashMap()
permalink: Java/WeakHashMap/WeakHashMap
date: 2021-01-04
key: JavaJava.W.WeakHashMap
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WeakHashMap.constructores valor="WeakHashMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public WeakHashMap()
public WeakHashMap(int initialCapacity)
public WeakHashMap(int initialCapacity, float loadFactor)
public WeakHashMap(Map<? extends K,? extends V> m)
~~~

## Parámetros
* **? extends V&gt; m**,  {% include w3api/param_description.html metodo=_data parametro="? extends V> m" %}
* **Map&lt;? extends K**,  {% include w3api/param_description.html metodo=_data parametro="Map<? extends K" %}
* **int initialCapacity**,  {% include w3api/param_description.html metodo=_data parametro="int initialCapacity" %}
* **float loadFactor**,  {% include w3api/param_description.html metodo=_data parametro="float loadFactor" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[WeakHashMap](/Java/WeakHashMap/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.WeakHashMap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
