---
title: IIOMetadataFormatImpl.addElement()
permalink: Java/IIOMetadataFormatImpl/addElement
date: 2021-01-04
key: JavaJava.I.IIOMetadataFormatImpl
category: java
tags: ['java se', 'javax.imageio.metadata', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOMetadataFormatImpl.metodos valor="addElement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void addElement(String elementName, String parentName, int childPolicy)
protected void addElement(String elementName, String parentName, int minChildren, int maxChildren)
~~~

## Parámetros
* **int maxChildren**,  {% include w3api/param_description.html metodo=_data parametro="int maxChildren" %}
* **String parentName**,  {% include w3api/param_description.html metodo=_data parametro="String parentName" %}
* **String elementName**,  {% include w3api/param_description.html metodo=_data parametro="String elementName" %}
* **int minChildren**,  {% include w3api/param_description.html metodo=_data parametro="int minChildren" %}
* **int childPolicy**,  {% include w3api/param_description.html metodo=_data parametro="int childPolicy" %}

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
