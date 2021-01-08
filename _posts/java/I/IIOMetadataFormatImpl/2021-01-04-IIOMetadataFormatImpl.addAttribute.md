---
title: IIOMetadataFormatImpl.addAttribute()
permalink: Java/IIOMetadataFormatImpl/addAttribute
date: 2021-01-04
key: JavaJava.I.IIOMetadataFormatImpl
category: java
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
* **boolean required**,  {% include w3api/param_description.html metodo=_data parametro="boolean required" %}
* **int listMinLength**,  {% include w3api/param_description.html metodo=_data parametro="int listMinLength" %}
* **String maxValue**,  {% include w3api/param_description.html metodo=_data parametro="String maxValue" %}
* **String elementName**,  {% include w3api/param_description.html metodo=_data parametro="String elementName" %}
* **String attrName**,  {% include w3api/param_description.html metodo=_data parametro="String attrName" %}
* **String minValue**,  {% include w3api/param_description.html metodo=_data parametro="String minValue" %}
* **boolean maxInclusive**,  {% include w3api/param_description.html metodo=_data parametro="boolean maxInclusive" %}
* **int listMaxLength**,  {% include w3api/param_description.html metodo=_data parametro="int listMaxLength" %}
* **boolean minInclusive**,  {% include w3api/param_description.html metodo=_data parametro="boolean minInclusive" %}
* **List&lt;String&gt; enumeratedValues**,  {% include w3api/param_description.html metodo=_data parametro="List<String> enumeratedValues" %}
* **String defaultValue**,  {% include w3api/param_description.html metodo=_data parametro="String defaultValue" %}
* **int dataType**,  {% include w3api/param_description.html metodo=_data parametro="int dataType" %}

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
{%- for _ldc in site.data.Java.I.IIOMetadataFormatImpl.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
