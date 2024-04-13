---
title: Hashtable.Hashtable()
permalink: /Java/Hashtable/Hashtable/
date: 2021-01-11
key: Java.H.Hashtable
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.Hashtable.constructores valor="Hashtable" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Hashtable()
public Hashtable(int initialCapacity)
public Hashtable(int initialCapacity, float loadFactor)
public Hashtable(Map<? extends K,? extends V> t)
~~~

## Parámetros
* **Map&lt;? extends K**,  {% include w3api/param_description.html metodo=_dato parametro="Map<? extends K" %}
* **float loadFactor**,  {% include w3api/param_description.html metodo=_dato parametro="float loadFactor" %}
* **int initialCapacity**,  {% include w3api/param_description.html metodo=_dato parametro="int initialCapacity" %}
* **? extends V&gt; t**,  {% include w3api/param_description.html metodo=_dato parametro="? extends V> t" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Hashtable](/Java/Hashtable/)

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
