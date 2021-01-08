---
title: Properties.list()
permalink: Java/Properties/list
date: 2021-01-04
key: JavaJava.P.Properties
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Properties.metodos valor="list" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void list(PrintStream out)
public void list(PrintWriter out)
~~~

## Parámetros
* **PrintStream out**,  {% include w3api/param_description.html metodo=_data parametro="PrintStream out" %}
* **PrintWriter out**,  {% include w3api/param_description.html metodo=_data parametro="PrintWriter out" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/)

## Clase Padre
[Properties](/Java/Properties/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.Properties.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
