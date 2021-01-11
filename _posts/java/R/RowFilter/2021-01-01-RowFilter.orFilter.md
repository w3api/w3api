---
title: RowFilter.orFilter()
permalink: Java/RowFilter/orFilter
date: 2021-01-11
key: JavaJava.R.RowFilter
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RowFilter.metodos valor="orFilter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <M,I> RowFilter<M,I> orFilter(Iterable<? extends RowFilter<? super M,? super I>> filters)
~~~

## Parámetros
* **Iterable&lt;? extends RowFilter&lt;? super M**,  {% include w3api/param_description.html metodo=_dato parametro="Iterable<? extends RowFilter<? super M" %}
* **? super I&gt;&gt; filters**,  {% include w3api/param_description.html metodo=_dato parametro="? super I>> filters" %}

## Clase Padre
[RowFilter](/Java/RowFilter/)

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
