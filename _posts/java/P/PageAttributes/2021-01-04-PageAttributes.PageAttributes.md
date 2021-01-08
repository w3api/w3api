---
title: PageAttributes.PageAttributes()
permalink: Java/PageAttributes/PageAttributes
date: 2021-01-04
key: JavaJava.P.PageAttributes
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PageAttributes.constructores valor="PageAttributes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PageAttributes()
public PageAttributes(PageAttributes obj)
public PageAttributes(PageAttributes.ColorType color, PageAttributes.MediaType media, PageAttributes.OrientationRequestedType orientationRequested, PageAttributes.OriginType origin, PageAttributes.PrintQualityType printQuality, int[] printerResolution)
~~~

## Parámetros
* **int[] printerResolution**,  {% include w3api/param_description.html metodo=_data parametro="int[] printerResolution" %}
* **PageAttributes.MediaType media**,  {% include w3api/param_description.html metodo=_data parametro="PageAttributes.MediaType media" %}
* **PageAttributes.PrintQualityType printQuality**,  {% include w3api/param_description.html metodo=_data parametro="PageAttributes.PrintQualityType printQuality" %}
* **PageAttributes.OrientationRequestedType orientationRequested**,  {% include w3api/param_description.html metodo=_data parametro="PageAttributes.OrientationRequestedType orientationRequested" %}
* **PageAttributes obj**,  {% include w3api/param_description.html metodo=_data parametro="PageAttributes obj" %}
* **PageAttributes.OriginType origin**,  {% include w3api/param_description.html metodo=_data parametro="PageAttributes.OriginType origin" %}
* **PageAttributes.ColorType color**,  {% include w3api/param_description.html metodo=_data parametro="PageAttributes.ColorType color" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PageAttributes](/Java/PageAttributes/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PageAttributes.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
