---
title: Component.list()
permalink: Java/Component/list
date: 2021-01-04
key: JavaJava.C.Component
category: java
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
* **int indent**,  {% include w3api/param_description.html metodo=_data parametro="int indent" %}
* **PrintStream out**,  {% include w3api/param_description.html metodo=_data parametro="PrintStream out" %}
* **PrintWriter out**,  {% include w3api/param_description.html metodo=_data parametro="PrintWriter out" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Component](/Java/Component/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Component.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
