---
title: IIOMetadataFormat.canNodeAppear()
permalink: /Java/IIOMetadataFormat/canNodeAppear/
date: 2021-01-11
key: Java.I.IIOMetadataFormat
category: Java
tags: ['java se', 'javax.imageio.metadata', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOMetadataFormat.metodos valor="canNodeAppear" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean canNodeAppear(String elementName, ImageTypeSpecifier imageType)
~~~

## Parámetros
* **ImageTypeSpecifier imageType**,  {% include w3api/param_description.html metodo=_dato parametro="ImageTypeSpecifier imageType" %}
* **String elementName**,  {% include w3api/param_description.html metodo=_dato parametro="String elementName" %}

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
