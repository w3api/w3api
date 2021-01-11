---
title: DropShadow.DropShadow()
permalink: Java/DropShadow/DropShadow
date: 2021-01-11
key: JavaJava.D.DropShadow
category: java
tags: ['java se', 'javafx.scene.effect', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DropShadow.constructores valor="DropShadow" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DropShadow()
public DropShadow(double radius, double offsetX, double offsetY, Color color)
public DropShadow(double radius, Color color)
public DropShadow(BlurType blurType, Color color, double radius, double spread, double offsetX, double offsetY)
~~~

## Parámetros
* **double offsetY**,  {% include w3api/param_description.html metodo=_dato parametro="double offsetY" %}
* **double radius**,  {% include w3api/param_description.html metodo=_dato parametro="double radius" %}
* **BlurType blurType**,  {% include w3api/param_description.html metodo=_dato parametro="BlurType blurType" %}
* **double spread**,  {% include w3api/param_description.html metodo=_dato parametro="double spread" %}
* **double offsetX**,  {% include w3api/param_description.html metodo=_dato parametro="double offsetX" %}
* **Color color**,  {% include w3api/param_description.html metodo=_dato parametro="Color color" %}

## Clase Padre
[DropShadow](/Java/DropShadow/)

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
