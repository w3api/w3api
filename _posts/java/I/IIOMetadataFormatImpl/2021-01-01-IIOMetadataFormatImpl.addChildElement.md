---
title: IIOMetadataFormatImpl.addChildElement()
permalink: Java/IIOMetadataFormatImpl/addChildElement
date: 2021-01-11
key: JavaJava.I.IIOMetadataFormatImpl
category: java
tags: ['java se', 'javax.imageio.metadata', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOMetadataFormatImpl.metodos valor="addChildElement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void addChildElement(String elementName, String parentName)
~~~

## Parámetros
* **String parentName**,  {% include w3api/param_description.html metodo=_dato parametro="String parentName" %}
* **String elementName**,  {% include w3api/param_description.html metodo=_dato parametro="String elementName" %}

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
