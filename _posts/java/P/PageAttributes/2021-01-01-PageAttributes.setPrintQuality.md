---
title: PageAttributes.setPrintQuality()
permalink: Java/PageAttributes/setPrintQuality
date: 2021-01-11
key: JavaJava.P.PageAttributes
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PageAttributes.metodos valor="setPrintQuality" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setPrintQuality(int printQuality)
public void setPrintQuality(PageAttributes.PrintQualityType printQuality)
~~~

## Parámetros
* **PageAttributes.PrintQualityType printQuality**,  {% include w3api/param_description.html metodo=_dato parametro="PageAttributes.PrintQualityType printQuality" %}
* **int printQuality**,  {% include w3api/param_description.html metodo=_dato parametro="int printQuality" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
