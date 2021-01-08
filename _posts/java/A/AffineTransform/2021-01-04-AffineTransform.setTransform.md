---
title: AffineTransform.setTransform()
permalink: Java/AffineTransform/setTransform
date: 2021-01-04
key: JavaJava.A.AffineTransform
category: java
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
* **AffineTransform Tx**,  {% include w3api/param_description.html metodo=_data parametro="AffineTransform Tx" %}
* **double m12**,  {% include w3api/param_description.html metodo=_data parametro="double m12" %}
* **double m10**,  {% include w3api/param_description.html metodo=_data parametro="double m10" %}
* **double m01**,  {% include w3api/param_description.html metodo=_data parametro="double m01" %}
* **double m11**,  {% include w3api/param_description.html metodo=_data parametro="double m11" %}
* **double m02**,  {% include w3api/param_description.html metodo=_data parametro="double m02" %}
* **double m00**,  {% include w3api/param_description.html metodo=_data parametro="double m00" %}

## Clase Padre
[AffineTransform](/Java/AffineTransform/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AffineTransform.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
