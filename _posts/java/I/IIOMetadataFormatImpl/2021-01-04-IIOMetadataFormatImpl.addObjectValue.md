---
title: IIOMetadataFormatImpl.addObjectValue()
permalink: Java/IIOMetadataFormatImpl/addObjectValue
date: 2021-01-04
key: JavaJava.I.IIOMetadataFormatImpl
category: java
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
* **boolean required**,  {% include w3api/param_description.html metodo=_data parametro="boolean required" %}
* **T defaultValue**,  {% include w3api/param_description.html metodo=_data parametro="T defaultValue" %}
* **String elementName**,  {% include w3api/param_description.html metodo=_data parametro="String elementName" %}
* **Comparable&lt;? super T&gt; maxValue**,  {% include w3api/param_description.html metodo=_data parametro="Comparable<? super T> maxValue" %}
* **List&lt;? extends T&gt; enumeratedValues**,  {% include w3api/param_description.html metodo=_data parametro="List<? extends T> enumeratedValues" %}
* **Comparable&lt;? super T&gt; minValue**,  {% include w3api/param_description.html metodo=_data parametro="Comparable<? super T> minValue" %}
* **Class&lt;?&gt; classType**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> classType" %}
* **Class&lt;T&gt; classType**,  {% include w3api/param_description.html metodo=_data parametro="Class<T> classType" %}
* **boolean maxInclusive**,  {% include w3api/param_description.html metodo=_data parametro="boolean maxInclusive" %}
* **boolean minInclusive**,  {% include w3api/param_description.html metodo=_data parametro="boolean minInclusive" %}
* **int arrayMaxLength**,  {% include w3api/param_description.html metodo=_data parametro="int arrayMaxLength" %}
* **int arrayMinLength**,  {% include w3api/param_description.html metodo=_data parametro="int arrayMinLength" %}

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
