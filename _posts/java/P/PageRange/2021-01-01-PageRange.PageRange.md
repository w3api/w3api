---
title: PageRange.PageRange()
permalink: /Java/PageRange/PageRange/
date: 2021-01-11
key: Java.P.PageRange
category: Java
tags: ['java se', 'javafx.print', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PageRange.constructores valor="PageRange" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PageRange(int startPage, int endPage)
~~~

## Parámetros
* **int startPage**,  {% include w3api/param_description.html metodo=_dato parametro="int startPage" %}
* **int endPage**,  {% include w3api/param_description.html metodo=_dato parametro="int endPage" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PageRange](/Java/PageRange/)

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
