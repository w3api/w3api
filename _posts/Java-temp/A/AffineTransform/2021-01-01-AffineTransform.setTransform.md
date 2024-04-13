---
title: AffineTransform.setTransform()
permalink: /Java/AffineTransform/setTransform/
date: 2021-01-11
key: Java.A.AffineTransform
category: Java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AffineTransform.metodos valor="setTransform" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setTransform(double m00, double m10, double m01, double m11, double m02, double m12)
public void setTransform(AffineTransform Tx)
~~~

## Parámetros
* **double m00**,  {% include w3api/param_description.html metodo=_dato parametro="double m00" %}
* **AffineTransform Tx**,  {% include w3api/param_description.html metodo=_dato parametro="AffineTransform Tx" %}
* **double m10**,  {% include w3api/param_description.html metodo=_dato parametro="double m10" %}
* **double m12**,  {% include w3api/param_description.html metodo=_dato parametro="double m12" %}
* **double m01**,  {% include w3api/param_description.html metodo=_dato parametro="double m01" %}
* **double m11**,  {% include w3api/param_description.html metodo=_dato parametro="double m11" %}
* **double m02**,  {% include w3api/param_description.html metodo=_dato parametro="double m02" %}

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
