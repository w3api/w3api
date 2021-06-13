---
title: IIOMetadataFormatImpl.getAttributeDescription()
permalink: /Java/IIOMetadataFormatImpl/getAttributeDescription/
date: 2021-01-11
key: Java.I.IIOMetadataFormatImpl
category: Java
tags: ['java se', 'javax.imageio.metadata', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOMetadataFormatImpl.metodos valor="getAttributeDescription" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public String getAttributeDescription(String elementName, String attrName, Locale locale)
~~~

## Parámetros
* **String attrName**,  {% include w3api/param_description.html metodo=_dato parametro="String attrName" %}
* **String elementName**,  {% include w3api/param_description.html metodo=_dato parametro="String elementName" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[IIOMetadataFormatImpl](/Java/IIOMetadataFormatImpl/)

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
