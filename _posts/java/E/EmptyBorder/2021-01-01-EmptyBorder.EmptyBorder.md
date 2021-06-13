---
title: EmptyBorder.EmptyBorder()
permalink: /Java/EmptyBorder/EmptyBorder/
date: 2021-01-11
key: Java.E.EmptyBorder
category: Java
tags: ['java se', 'javax.swing.border', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EmptyBorder.constructores valor="EmptyBorder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public EmptyBorder(int top, int left, int bottom, int right)
@ConstructorProperties("borderInsets") public EmptyBorder(Insets borderInsets)
~~~

## Parámetros
* **Insets borderInsets**,  {% include w3api/param_description.html metodo=_dato parametro="Insets borderInsets" %}
* **int top**,  {% include w3api/param_description.html metodo=_dato parametro="int top" %}
* **int right**,  {% include w3api/param_description.html metodo=_dato parametro="int right" %}
* **int left**,  {% include w3api/param_description.html metodo=_dato parametro="int left" %}
* **int bottom**,  {% include w3api/param_description.html metodo=_dato parametro="int bottom" %}

## Clase Padre
[EmptyBorder](/Java/EmptyBorder/)

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
