---
title: PickResult.PickResult()
permalink: /Java/PickResult/PickResult/
date: 2021-01-11
key: Java.P.PickResult
category: Java
tags: ['java se', 'javafx.scene.input', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PickResult.constructores valor="PickResult" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PickResult(EventTarget target, double sceneX, double sceneY)
public PickResult(Node node, Point3D point, double distance)
public PickResult(Node node, Point3D point, double distance, int face, Point2D texCoord)
public PickResult(Node node, Point3D point, double distance, int face, Point3D normal, Point2D texCoord)
~~~

## Parámetros
* **double sceneY**,  {% include w3api/param_description.html metodo=_dato parametro="double sceneY" %}
* **Point2D texCoord**,  {% include w3api/param_description.html metodo=_dato parametro="Point2D texCoord" %}
* **double distance**,  {% include w3api/param_description.html metodo=_dato parametro="double distance" %}
* **Point3D normal**,  {% include w3api/param_description.html metodo=_dato parametro="Point3D normal" %}
* **Point3D point**,  {% include w3api/param_description.html metodo=_dato parametro="Point3D point" %}
* **Node node**,  {% include w3api/param_description.html metodo=_dato parametro="Node node" %}
* **int face**,  {% include w3api/param_description.html metodo=_dato parametro="int face" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_dato parametro="EventTarget target" %}
* **double sceneX**,  {% include w3api/param_description.html metodo=_dato parametro="double sceneX" %}

## Clase Padre
[PickResult](/Java/PickResult/)

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
