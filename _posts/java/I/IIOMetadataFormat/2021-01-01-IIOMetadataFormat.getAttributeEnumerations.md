---
title: IIOMetadataFormat.getAttributeEnumerations()
permalink: Java/IIOMetadataFormat/getAttributeEnumerations
date: 2021-01-11
key: JavaJava.I.IIOMetadataFormat
category: java
tags: ['java se', 'javax.imageio.metadata', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOMetadataFormat.metodos valor="getAttributeEnumerations" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
String[] getAttributeEnumerations(String elementName, String attrName)
~~~

## Parámetros
* **String attrName**,  {% include w3api/param_description.html metodo=_dato parametro="String attrName" %}
* **String elementName**,  {% include w3api/param_description.html metodo=_dato parametro="String elementName" %}

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
