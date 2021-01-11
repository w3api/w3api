---
title: IIOMetadataFormatImpl.IIOMetadataFormatImpl()
permalink: Java/IIOMetadataFormatImpl/IIOMetadataFormatImpl
date: 2021-01-11
key: JavaJava.I.IIOMetadataFormatImpl
category: java
tags: ['java se', 'javax.imageio.metadata', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOMetadataFormatImpl.constructores valor="IIOMetadataFormatImpl" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public IIOMetadataFormatImpl(String rootName, int childPolicy)
public IIOMetadataFormatImpl(String rootName, int minChildren, int maxChildren)
~~~

## Parámetros
* **int maxChildren**,  {% include w3api/param_description.html metodo=_dato parametro="int maxChildren" %}
* **int childPolicy**,  {% include w3api/param_description.html metodo=_dato parametro="int childPolicy" %}
* **int minChildren**,  {% include w3api/param_description.html metodo=_dato parametro="int minChildren" %}
* **String rootName**,  {% include w3api/param_description.html metodo=_dato parametro="String rootName" %}

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
