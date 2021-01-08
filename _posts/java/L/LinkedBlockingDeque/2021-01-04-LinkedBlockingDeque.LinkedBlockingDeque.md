---
title: LinkedBlockingDeque.LinkedBlockingDeque()
permalink: Java/LinkedBlockingDeque/LinkedBlockingDeque
date: 2021-01-04
key: JavaJava.L.LinkedBlockingDeque
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LinkedBlockingDeque.constructores valor="LinkedBlockingDeque" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LinkedBlockingDeque()
public LinkedBlockingDeque(int capacity)
public LinkedBlockingDeque(Collection<? extends E> c)
~~~

## Parámetros
* **Collection&lt;? extends E&gt; c**,  {% include w3api/param_description.html metodo=_data parametro="Collection<? extends E> c" %}
* **int capacity**,  {% include w3api/param_description.html metodo=_data parametro="int capacity" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[LinkedBlockingDeque](/Java/LinkedBlockingDeque/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LinkedBlockingDeque.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
