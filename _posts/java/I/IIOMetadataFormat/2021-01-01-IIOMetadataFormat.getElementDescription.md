---
title: IIOMetadataFormat.getElementDescription()
permalink: Java/IIOMetadataFormat/getElementDescription
date: 2021-01-11
key: JavaJava.I.IIOMetadataFormat
category: java
tags: ['java se', 'javax.imageio.metadata', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOMetadataFormat.metodos valor="getElementDescription" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
String getElementDescription(String elementName, Locale locale)
~~~

## Parámetros
* **String elementName**,  {% include w3api/param_description.html metodo=_dato parametro="String elementName" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[IIOMetadataFormat](/Java/IIOMetadataFormat/)

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
