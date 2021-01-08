---
title: SequenceInputStream.SequenceInputStream()
permalink: Java/SequenceInputStream/SequenceInputStream
date: 2021-01-04
key: JavaJava.S.SequenceInputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SequenceInputStream.constructores valor="SequenceInputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SequenceInputStream(InputStream s1, InputStream s2)
public SequenceInputStream(Enumeration<? extends InputStream> e)
~~~

## Parámetros
* **InputStream s1**,  {% include w3api/param_description.html metodo=_data parametro="InputStream s1" %}
* **Enumeration&lt;? extends InputStream&gt; e**,  {% include w3api/param_description.html metodo=_data parametro="Enumeration<? extends InputStream> e" %}
* **InputStream s2**,  {% include w3api/param_description.html metodo=_data parametro="InputStream s2" %}

## Clase Padre
[SequenceInputStream](/Java/SequenceInputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SequenceInputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
