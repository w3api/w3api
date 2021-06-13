---
title: LinkedHashSet.LinkedHashSet()
permalink: /Java/LinkedHashSet/LinkedHashSet/
date: 2021-01-11
key: Java.L.LinkedHashSet
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LinkedHashSet.constructores valor="LinkedHashSet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LinkedHashSet()
public LinkedHashSet(int initialCapacity)
public LinkedHashSet(int initialCapacity, float loadFactor)
public LinkedHashSet(Collection<? extends E> c)
~~~

## Parámetros
* **float loadFactor**,  {% include w3api/param_description.html metodo=_dato parametro="float loadFactor" %}
* **int initialCapacity**,  {% include w3api/param_description.html metodo=_dato parametro="int initialCapacity" %}
* **Collection&lt;? extends E&gt; c**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<? extends E> c" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[LinkedHashSet](/Java/LinkedHashSet/)

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
