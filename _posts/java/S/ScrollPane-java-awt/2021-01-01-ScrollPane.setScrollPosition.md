---
title: ScrollPane.setScrollPosition()
permalink: Java/ScrollPane-java-awt/setScrollPosition
date: 2021-01-11
key: JavaJava.S.ScrollPane-java-awt
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScrollPane-java-awt.metodos valor="setScrollPosition" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setScrollPosition(int x, int y)
public void setScrollPosition(Point p)
~~~

## Parámetros
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **Point p**,  {% include w3api/param_description.html metodo=_dato parametro="Point p" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ScrollPane](/Java/ScrollPane-java-awt/)

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
