---
title: AffineTransform.rotate()
permalink: Java/AffineTransform/rotate
date: 2021-01-10
key: JavaJava.A.AffineTransform
category: java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AffineTransform.metodos valor="rotate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void rotate(double theta)
public void rotate(double vecx, double vecy)
public void rotate(double theta, double anchorx, double anchory)
public void rotate(double vecx, double vecy, double anchorx, double anchory)
~~~

## Parámetros
* **double vecy**,  {% include w3api/param_description.html metodo=_dato parametro="double vecy" %}
* **double anchorx**,  {% include w3api/param_description.html metodo=_dato parametro="double anchorx" %}
* **double vecx**,  {% include w3api/param_description.html metodo=_dato parametro="double vecx" %}
* **double anchory**,  {% include w3api/param_description.html metodo=_dato parametro="double anchory" %}
* **double theta**,  {% include w3api/param_description.html metodo=_dato parametro="double theta" %}

## Clase Padre
[AffineTransform](/Java/AffineTransform/)

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
