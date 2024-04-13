---
title: Component.list()
permalink: /Java/Component/list/
date: 2021-01-11
key: Java.C.Component
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Component.metodos valor="list" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void list()
public void list(PrintStream out)
public void list(PrintStream out, int indent)
public void list(PrintWriter out)
public void list(PrintWriter out, int indent)
~~~

## Parámetros
* **PrintWriter out**,  {% include w3api/param_description.html metodo=_dato parametro="PrintWriter out" %}
* **int indent**,  {% include w3api/param_description.html metodo=_dato parametro="int indent" %}
* **PrintStream out**,  {% include w3api/param_description.html metodo=_dato parametro="PrintStream out" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Component](/Java/Component/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
