---
title: IIOMetadataNode.setIdAttributeNS()
permalink: Java/IIOMetadataNode/setIdAttributeNS
date: 2021-01-04
key: JavaJava.I.IIOMetadataNode
category: java
tags: ['java se', 'javax.imageio.metadata', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOMetadataNode.metodos valor="setIdAttributeNS" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setIdAttributeNS(String namespaceURI, String localName, boolean isId) throws DOMException
~~~

## Parámetros
* **String localName**,  {% include w3api/param_description.html metodo=_data parametro="String localName" %}
* **String namespaceURI**,  {% include w3api/param_description.html metodo=_data parametro="String namespaceURI" %}
* **boolean isId**,  {% include w3api/param_description.html metodo=_data parametro="boolean isId" %}

## Excepciones
[DOMException](/Java/DOMException/)

## Clase Padre
[IIOMetadataNode](/Java/IIOMetadataNode/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IIOMetadataNode.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
