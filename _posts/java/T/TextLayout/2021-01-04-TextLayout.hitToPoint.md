---
title: TextLayout.hitToPoint()
permalink: Java/TextLayout/hitToPoint
date: 2021-01-04
key: JavaJava.T.TextLayout
category: java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TextLayout.metodos valor="hitToPoint" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void hitToPoint(TextHitInfo hit, Point2D point)
~~~

## Parámetros
* **TextHitInfo hit**,  {% include w3api/param_description.html metodo=_data parametro="TextHitInfo hit" %}
* **Point2D point**,  {% include w3api/param_description.html metodo=_data parametro="Point2D point" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[TextLayout](/Java/TextLayout/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TextLayout.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
