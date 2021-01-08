---
title: Collections.frequency()
permalink: Java/Collections/frequency
date: 2021-01-04
key: JavaJava.C.Collections
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="frequency" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static int frequency(Collection<?> c, Object o)
~~~

## Parámetros
* **Object o**,  {% include w3api/param_description.html metodo=_data parametro="Object o" %}
* **Collection&lt;?&gt; c**,  {% include w3api/param_description.html metodo=_data parametro="Collection<?> c" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Collections](/Java/Collections/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Collections.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
