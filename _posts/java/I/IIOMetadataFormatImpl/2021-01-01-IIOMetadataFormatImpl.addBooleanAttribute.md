---
title: IIOMetadataFormatImpl.addBooleanAttribute()
permalink: Java/IIOMetadataFormatImpl/addBooleanAttribute
date: 2021-01-11
key: JavaJava.I.IIOMetadataFormatImpl
category: java
tags: ['java se', 'javax.imageio.metadata', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOMetadataFormatImpl.metodos valor="addBooleanAttribute" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void addBooleanAttribute(String elementName, String attrName, boolean hasDefaultValue, boolean defaultValue)
~~~

## Parámetros
* **String attrName**,  {% include w3api/param_description.html metodo=_dato parametro="String attrName" %}
* **boolean hasDefaultValue**,  {% include w3api/param_description.html metodo=_dato parametro="boolean hasDefaultValue" %}
* **String elementName**,  {% include w3api/param_description.html metodo=_dato parametro="String elementName" %}
* **boolean defaultValue**,  {% include w3api/param_description.html metodo=_dato parametro="boolean defaultValue" %}

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
