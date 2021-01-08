---
title: Hashtable.Hashtable()
permalink: Java/Hashtable/Hashtable
date: 2021-01-04
key: JavaJava.H.Hashtable
category: java
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
* **? extends V&gt; t**,  {% include w3api/param_description.html metodo=_data parametro="? extends V> t" %}
* **Map&lt;? extends K**,  {% include w3api/param_description.html metodo=_data parametro="Map<? extends K" %}
* **int initialCapacity**,  {% include w3api/param_description.html metodo=_data parametro="int initialCapacity" %}
* **float loadFactor**,  {% include w3api/param_description.html metodo=_data parametro="float loadFactor" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Hashtable](/Java/Hashtable/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.Hashtable.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
