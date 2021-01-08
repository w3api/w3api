---
title: PickResult.PickResult()
permalink: Java/PickResult/PickResult
date: 2021-01-04
key: JavaJava.P.PickResult
category: java
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
* **Point3D point**,  {% include w3api/param_description.html metodo=_data parametro="Point3D point" %}
* **double sceneY**,  {% include w3api/param_description.html metodo=_data parametro="double sceneY" %}
* **Node node**,  {% include w3api/param_description.html metodo=_data parametro="Node node" %}
* **int face**,  {% include w3api/param_description.html metodo=_data parametro="int face" %}
* **double distance**,  {% include w3api/param_description.html metodo=_data parametro="double distance" %}
* **Point3D normal**,  {% include w3api/param_description.html metodo=_data parametro="Point3D normal" %}
* **Point2D texCoord**,  {% include w3api/param_description.html metodo=_data parametro="Point2D texCoord" %}
* **double sceneX**,  {% include w3api/param_description.html metodo=_data parametro="double sceneX" %}
* **EventTarget target**,  {% include w3api/param_description.html metodo=_data parametro="EventTarget target" %}

## Clase Padre
[PickResult](/Java/PickResult/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PickResult.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
