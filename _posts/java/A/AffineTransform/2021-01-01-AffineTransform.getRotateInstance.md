---
title: AffineTransform.getRotateInstance()
permalink: /Java/AffineTransform/getRotateInstance/
date: 2021-01-11
key: Java.A.AffineTransform
category: Java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AffineTransform.metodos valor="getRotateInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static AffineTransform getRotateInstance(double theta)
public static AffineTransform getRotateInstance(double vecx, double vecy)
public static AffineTransform getRotateInstance(double theta, double anchorx, double anchory)
public static AffineTransform getRotateInstance(double vecx, double vecy, double anchorx, double anchory)
~~~

## Parámetros
* **double vecy**,  {% include w3api/param_description.html metodo=_dato parametro="double vecy" %}
* **double vecx**,  {% include w3api/param_description.html metodo=_dato parametro="double vecx" %}
* **double anchory**,  {% include w3api/param_description.html metodo=_dato parametro="double anchory" %}
* **double theta**,  {% include w3api/param_description.html metodo=_dato parametro="double theta" %}
* **double anchorx**,  {% include w3api/param_description.html metodo=_dato parametro="double anchorx" %}

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
