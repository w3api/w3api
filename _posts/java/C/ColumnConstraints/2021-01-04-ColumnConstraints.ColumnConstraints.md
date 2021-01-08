---
title: ColumnConstraints.ColumnConstraints()
permalink: Java/ColumnConstraints/ColumnConstraints
date: 2021-01-04
key: JavaJava.C.ColumnConstraints
category: java
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
* **HPos halignment**,  {% include w3api/param_description.html metodo=_data parametro="HPos halignment" %}
* **double width**,  {% include w3api/param_description.html metodo=_data parametro="double width" %}
* **boolean fillWidth**,  {% include w3api/param_description.html metodo=_data parametro="boolean fillWidth" %}
* **double maxWidth**,  {% include w3api/param_description.html metodo=_data parametro="double maxWidth" %}
* **double prefWidth**,  {% include w3api/param_description.html metodo=_data parametro="double prefWidth" %}
* **double minWidth**,  {% include w3api/param_description.html metodo=_data parametro="double minWidth" %}
* **Priority hgrow**,  {% include w3api/param_description.html metodo=_data parametro="Priority hgrow" %}

## Clase Padre
[ColumnConstraints](/Java/ColumnConstraints/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ColumnConstraints.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
