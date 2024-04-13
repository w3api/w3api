---
title: IIOMetadataNode.setIdAttributeNode()
permalink: /Java/IIOMetadataNode/setIdAttributeNode/
date: 2021-01-11
key: Java.I.IIOMetadataNode
category: Java
tags: ['java se', 'javax.imageio.metadata', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOMetadataNode.metodos valor="setIdAttributeNode" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setIdAttributeNode(Attr idAttr, boolean isId) throws DOMException
~~~

## Parámetros
* **Attr idAttr**,  {% include w3api/param_description.html metodo=_dato parametro="Attr idAttr" %}
* **boolean isId**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isId" %}

## Excepciones
[DOMException](/Java/DOMException/)

## Clase Padre
[IIOMetadataNode](/Java/IIOMetadataNode/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
