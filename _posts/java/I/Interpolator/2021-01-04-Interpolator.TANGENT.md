---
title: Interpolator.TANGENT()
permalink: Java/Interpolator/TANGENT
date: 2021-01-04
key: JavaJava.I.Interpolator
category: java
tags: ['java se', 'javafx.animation', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.Interpolator.metodos valor="TANGENT" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Interpolator TANGENT(Duration t, double v)
public static Interpolator TANGENT(Duration t1, double v1, Duration t2, double v2)
~~~

## Parámetros
* **double v**,  {% include w3api/param_description.html metodo=_data parametro="double v" %}
* **Duration t1**,  {% include w3api/param_description.html metodo=_data parametro="Duration t1" %}
* **Duration t**,  {% include w3api/param_description.html metodo=_data parametro="Duration t" %}
* **double v1**,  {% include w3api/param_description.html metodo=_data parametro="double v1" %}
* **double v2**,  {% include w3api/param_description.html metodo=_data parametro="double v2" %}
* **Duration t2**,  {% include w3api/param_description.html metodo=_data parametro="Duration t2" %}

## Clase Padre
[Interpolator](/Java/Interpolator/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.Interpolator.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
