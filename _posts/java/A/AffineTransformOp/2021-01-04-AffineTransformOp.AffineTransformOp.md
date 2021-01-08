---
title: AffineTransformOp.AffineTransformOp()
permalink: Java/AffineTransformOp/AffineTransformOp
date: 2021-01-04
key: JavaJava.A.AffineTransformOp
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AffineTransformOp.constructores valor="AffineTransformOp" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public AffineTransformOp(AffineTransform xform, int interpolationType)
public AffineTransformOp(AffineTransform xform, RenderingHints hints)
~~~

## Parámetros
* **RenderingHints hints**,  {% include w3api/param_description.html metodo=_data parametro="RenderingHints hints" %}
* **AffineTransform xform**,  {% include w3api/param_description.html metodo=_data parametro="AffineTransform xform" %}
* **int interpolationType**,  {% include w3api/param_description.html metodo=_data parametro="int interpolationType" %}

## Excepciones
[ImagingOpException](/Java/ImagingOpException/)

## Clase Padre
[AffineTransformOp](/Java/AffineTransformOp/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AffineTransformOp.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
