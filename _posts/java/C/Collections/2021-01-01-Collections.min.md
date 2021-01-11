---
title: Collections.min()
permalink: Java/Collections/min
date: 2021-01-11
key: JavaJava.C.Collections
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="min" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T extends Object & Comparable<? super T>>T min(Collection<? extends T> coll)
static <T> T min(Collection<? extends T> coll, Comparator<? super T> comp)
~~~

## Parámetros
* **Comparator&lt;? super T&gt; comp**,  {% include w3api/param_description.html metodo=_dato parametro="Comparator<? super T> comp" %}
* **Collection&lt;? extends T&gt; coll**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<? extends T> coll" %}

## Clase Padre
[Collections](/Java/Collections/)

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
