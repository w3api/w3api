---
title: IIOMetadataFormatImpl.addElement()
permalink: /Java/IIOMetadataFormatImpl/addElement/
date: 2021-01-11
key: Java.I.IIOMetadataFormatImpl
category: Java
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
* **int maxChildren**,  {% include w3api/param_description.html metodo=_dato parametro="int maxChildren" %}
* **int childPolicy**,  {% include w3api/param_description.html metodo=_dato parametro="int childPolicy" %}
* **String elementName**,  {% include w3api/param_description.html metodo=_dato parametro="String elementName" %}
* **String parentName**,  {% include w3api/param_description.html metodo=_dato parametro="String parentName" %}
* **int minChildren**,  {% include w3api/param_description.html metodo=_dato parametro="int minChildren" %}

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
