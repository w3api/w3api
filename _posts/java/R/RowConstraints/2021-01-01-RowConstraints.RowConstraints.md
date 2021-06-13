---
title: RowConstraints.RowConstraints()
permalink: /Java/RowConstraints/RowConstraints/
date: 2021-01-11
key: Java.R.RowConstraints
category: Java
tags: ['java se', 'javafx.scene.layout', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RowConstraints.constructores valor="RowConstraints" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RowConstraints()
public RowConstraints(double height)
public RowConstraints(double minHeight, double prefHeight, double maxHeight)
public RowConstraints(double minHeight, double prefHeight, double maxHeight, Priority vgrow, VPos valignment, boolean fillHeight)
~~~

## Parámetros
* **Priority vgrow**,  {% include w3api/param_description.html metodo=_dato parametro="Priority vgrow" %}
* **double minHeight**,  {% include w3api/param_description.html metodo=_dato parametro="double minHeight" %}
* **boolean fillHeight**,  {% include w3api/param_description.html metodo=_dato parametro="boolean fillHeight" %}
* **double prefHeight**,  {% include w3api/param_description.html metodo=_dato parametro="double prefHeight" %}
* **VPos valignment**,  {% include w3api/param_description.html metodo=_dato parametro="VPos valignment" %}
* **double maxHeight**,  {% include w3api/param_description.html metodo=_dato parametro="double maxHeight" %}
* **double height**,  {% include w3api/param_description.html metodo=_dato parametro="double height" %}

## Clase Padre
[RowConstraints](/Java/RowConstraints/)

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
