---
title: Collections.disjoint()
permalink: Java/Collections/disjoint
date: 2021-01-11
key: JavaJava.C.Collections
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="disjoint" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static boolean disjoint(Collection<?> c1, Collection<?> c2)
~~~

## Parámetros
* **Collection&lt;?&gt; c2**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<?> c2" %}
* **Collection&lt;?&gt; c1**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<?> c1" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

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
