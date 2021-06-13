---
title: IIOMetadataNode.setAttributeNS()
permalink: /Java/IIOMetadataNode/setAttributeNS/
date: 2021-01-11
key: Java.I.IIOMetadataNode
category: Java
tags: ['java se', 'javax.imageio.metadata', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOMetadataNode.metodos valor="setAttributeNS" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setAttributeNS(String namespaceURI, String qualifiedName, String value)
~~~

## Parámetros
* **String value**,  {% include w3api/param_description.html metodo=_dato parametro="String value" %}
* **String qualifiedName**,  {% include w3api/param_description.html metodo=_dato parametro="String qualifiedName" %}
* **String namespaceURI**,  {% include w3api/param_description.html metodo=_dato parametro="String namespaceURI" %}

## Clase Padre
[IIOMetadataNode](/Java/IIOMetadataNode/)

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
