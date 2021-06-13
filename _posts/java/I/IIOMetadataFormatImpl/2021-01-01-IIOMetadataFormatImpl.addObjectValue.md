---
title: IIOMetadataFormatImpl.addObjectValue()
permalink: /Java/IIOMetadataFormatImpl/addObjectValue/
date: 2021-01-11
key: Java.I.IIOMetadataFormatImpl
category: Java
tags: ['java se', 'javax.imageio.metadata', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOMetadataFormatImpl.metodos valor="addObjectValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void addObjectValue(String elementName, Class<?> classType, int arrayMinLength, int arrayMaxLength)
protected <T> void addObjectValue(String elementName, Class<T> classType, boolean required, T defaultValue)
protected <T> void addObjectValue(String elementName, Class<T> classType, boolean required, T defaultValue, List<? extends T> enumeratedValues)
protected <T extends Object & Comparable<? super T>>void addObjectValue(String elementName, Class<T> classType, T defaultValue, Comparable<? super T> minValue, Comparable<? super T> maxValue, boolean minInclusive, boolean maxInclusive)
~~~

## Parámetros
* **Class&lt;T&gt; classType**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> classType" %}
* **T defaultValue**,  {% include w3api/param_description.html metodo=_dato parametro="T defaultValue" %}
* **List&lt;? extends T&gt; enumeratedValues**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends T> enumeratedValues" %}
* **Comparable&lt;? super T&gt; maxValue**,  {% include w3api/param_description.html metodo=_dato parametro="Comparable<? super T> maxValue" %}
* **boolean minInclusive**,  {% include w3api/param_description.html metodo=_dato parametro="boolean minInclusive" %}
* **int arrayMaxLength**,  {% include w3api/param_description.html metodo=_dato parametro="int arrayMaxLength" %}
* **String elementName**,  {% include w3api/param_description.html metodo=_dato parametro="String elementName" %}
* **boolean maxInclusive**,  {% include w3api/param_description.html metodo=_dato parametro="boolean maxInclusive" %}
* **int arrayMinLength**,  {% include w3api/param_description.html metodo=_dato parametro="int arrayMinLength" %}
* **boolean required**,  {% include w3api/param_description.html metodo=_dato parametro="boolean required" %}
* **Comparable&lt;? super T&gt; minValue**,  {% include w3api/param_description.html metodo=_dato parametro="Comparable<? super T> minValue" %}
* **Class&lt;?&gt; classType**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> classType" %}

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
