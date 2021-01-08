---
title: Container.list()
permalink: Java/Container/list
date: 2021-01-04
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
* **int indent**,  {% include w3api/param_description.html metodo=_data parametro="int indent" %}
* **PrintStream out**,  {% include w3api/param_description.html metodo=_data parametro="PrintStream out" %}
* **PrintWriter out**,  {% include w3api/param_description.html metodo=_data parametro="PrintWriter out" %}

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
{%- for _ldc in site.data.Java.C.Container.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
