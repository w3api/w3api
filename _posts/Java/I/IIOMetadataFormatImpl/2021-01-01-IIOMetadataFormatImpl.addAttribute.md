---
title: IIOMetadataFormatImpl.addAttribute()
permalink: /Java/IIOMetadataFormatImpl/addAttribute/
date: 2021-01-11
key: Java.I.IIOMetadataFormatImpl
category: Java
tags: ['java se', 'javax.imageio.metadata', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOMetadataFormatImpl.metodos valor="addAttribute" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void addAttribute(String elementName, String attrName, int dataType, boolean required, int listMinLength, int listMaxLength)
protected void addAttribute(String elementName, String attrName, int dataType, boolean required, String defaultValue)
protected void addAttribute(String elementName, String attrName, int dataType, boolean required, String defaultValue, String minValue, String maxValue, boolean minInclusive, boolean maxInclusive)
protected void addAttribute(String elementName, String attrName, int dataType, boolean required, String defaultValue, List<String> enumeratedValues)
~~~

## Parámetros
* **String defaultValue**,  {% include w3api/param_description.html metodo=_dato parametro="String defaultValue" %}
* **String minValue**,  {% include w3api/param_description.html metodo=_dato parametro="String minValue" %}
* **String maxValue**,  {% include w3api/param_description.html metodo=_dato parametro="String maxValue" %}
* **int listMaxLength**,  {% include w3api/param_description.html metodo=_dato parametro="int listMaxLength" %}
* **int dataType**,  {% include w3api/param_description.html metodo=_dato parametro="int dataType" %}
* **boolean minInclusive**,  {% include w3api/param_description.html metodo=_dato parametro="boolean minInclusive" %}
* **String elementName**,  {% include w3api/param_description.html metodo=_dato parametro="String elementName" %}
* **List&lt;String&gt; enumeratedValues**,  {% include w3api/param_description.html metodo=_dato parametro="List<String> enumeratedValues" %}
* **boolean required**,  {% include w3api/param_description.html metodo=_dato parametro="boolean required" %}
* **boolean maxInclusive**,  {% include w3api/param_description.html metodo=_dato parametro="boolean maxInclusive" %}
* **String attrName**,  {% include w3api/param_description.html metodo=_dato parametro="String attrName" %}
* **int listMinLength**,  {% include w3api/param_description.html metodo=_dato parametro="int listMinLength" %}

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
