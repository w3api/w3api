---
title: Properties.list()
permalink: /Java/Properties/list/
date: 2021-01-11
key: Java.P.Properties
category: Java
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
* **PrintWriter out**,  {% include w3api/param_description.html metodo=_dato parametro="PrintWriter out" %}
* **PrintStream out**,  {% include w3api/param_description.html metodo=_dato parametro="PrintStream out" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
