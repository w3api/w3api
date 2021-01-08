---
title: InnerShadow.InnerShadow()
permalink: Java/InnerShadow/InnerShadow
date: 2021-01-04
key: JavaJava.I.InnerShadow
category: java
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
* **double radius**,  {% include w3api/param_description.html metodo=_data parametro="double radius" %}
* **double offsetX**,  {% include w3api/param_description.html metodo=_data parametro="double offsetX" %}
* **Color color**,  {% include w3api/param_description.html metodo=_data parametro="Color color" %}
* **BlurType blurType**,  {% include w3api/param_description.html metodo=_data parametro="BlurType blurType" %}
* **double choke**,  {% include w3api/param_description.html metodo=_data parametro="double choke" %}
* **double offsetY**,  {% include w3api/param_description.html metodo=_data parametro="double offsetY" %}

## Clase Padre
[InnerShadow](/Java/InnerShadow/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.InnerShadow.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
