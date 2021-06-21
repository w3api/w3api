---
title: ColumnConstraints.ColumnConstraints()
permalink: /Java/ColumnConstraints/ColumnConstraints/
date: 2021-01-11
key: Java.C.ColumnConstraints
category: Java
tags: ['java se', 'javafx.scene.layout', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ColumnConstraints.constructores valor="ColumnConstraints" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ColumnConstraints()
public ColumnConstraints(double width)
public ColumnConstraints(double minWidth, double prefWidth, double maxWidth)
public ColumnConstraints(double minWidth, double prefWidth, double maxWidth, Priority hgrow, HPos halignment, boolean fillWidth)
~~~

## Parámetros
* **double minWidth**,  {% include w3api/param_description.html metodo=_dato parametro="double minWidth" %}
* **double maxWidth**,  {% include w3api/param_description.html metodo=_dato parametro="double maxWidth" %}
* **boolean fillWidth**,  {% include w3api/param_description.html metodo=_dato parametro="boolean fillWidth" %}
* **double prefWidth**,  {% include w3api/param_description.html metodo=_dato parametro="double prefWidth" %}
* **double width**,  {% include w3api/param_description.html metodo=_dato parametro="double width" %}
* **HPos halignment**,  {% include w3api/param_description.html metodo=_dato parametro="HPos halignment" %}
* **Priority hgrow**,  {% include w3api/param_description.html metodo=_dato parametro="Priority hgrow" %}

## Clase Padre
[ColumnConstraints](/Java/ColumnConstraints/)

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
