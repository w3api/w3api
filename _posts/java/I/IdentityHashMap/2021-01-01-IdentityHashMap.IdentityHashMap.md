---
title: IdentityHashMap.IdentityHashMap()
permalink: /Java/IdentityHashMap/IdentityHashMap/
date: 2021-01-11
key: Java.I.IdentityHashMap
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IdentityHashMap.constructores valor="IdentityHashMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public IdentityHashMap()
public IdentityHashMap(int expectedMaxSize)
public IdentityHashMap(Map<? extends K,? extends V> m)
~~~

## Parámetros
* **int expectedMaxSize**,  {% include w3api/param_description.html metodo=_dato parametro="int expectedMaxSize" %}
* **Map&lt;? extends K**,  {% include w3api/param_description.html metodo=_dato parametro="Map<? extends K" %}
* **? extends V&gt; m**,  {% include w3api/param_description.html metodo=_dato parametro="? extends V> m" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[IdentityHashMap](/Java/IdentityHashMap/)

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
