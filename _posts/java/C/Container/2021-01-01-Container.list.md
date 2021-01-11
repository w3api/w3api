---
title: Container.list()
permalink: Java/Container/list
date: 2021-01-11
key: JavaJava.C.Container
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Container.metodos valor="list" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void list(PrintStream out, int indent)
public void list(PrintWriter out, int indent)
~~~

## Parámetros
* **PrintWriter out**,  {% include w3api/param_description.html metodo=_dato parametro="PrintWriter out" %}
* **int indent**,  {% include w3api/param_description.html metodo=_dato parametro="int indent" %}
* **PrintStream out**,  {% include w3api/param_description.html metodo=_dato parametro="PrintStream out" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Container](/Java/Container/)

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