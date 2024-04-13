---
title: InnerShadow.InnerShadow()
permalink: /Java/InnerShadow/InnerShadow/
date: 2021-01-11
key: Java.I.InnerShadow
category: Java
tags: ['java se', 'javafx.scene.effect', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InnerShadow.constructores valor="InnerShadow" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public InnerShadow()
public InnerShadow(double radius, double offsetX, double offsetY, Color color)
public InnerShadow(double radius, Color color)
public InnerShadow(BlurType blurType, Color color, double radius, double choke, double offsetX, double offsetY)
~~~

## Parámetros
* **double offsetY**,  {% include w3api/param_description.html metodo=_dato parametro="double offsetY" %}
* **double choke**,  {% include w3api/param_description.html metodo=_dato parametro="double choke" %}
* **double radius**,  {% include w3api/param_description.html metodo=_dato parametro="double radius" %}
* **BlurType blurType**,  {% include w3api/param_description.html metodo=_dato parametro="BlurType blurType" %}
* **double offsetX**,  {% include w3api/param_description.html metodo=_dato parametro="double offsetX" %}
* **Color color**,  {% include w3api/param_description.html metodo=_dato parametro="Color color" %}

## Clase Padre
[InnerShadow](/Java/InnerShadow/)

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
