---
title: IIOMetadataNode.getFeature()
permalink: /Java/IIOMetadataNode/getFeature/
date: 2021-01-11
key: Java.I.IIOMetadataNode
category: Java
tags: ['java se', 'javax.imageio.metadata', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOMetadataNode.metodos valor="getFeature" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object getFeature(String feature, String version) throws DOMException
~~~

## Parámetros
* **String feature**,  {% include w3api/param_description.html metodo=_dato parametro="String feature" %}
* **String version**,  {% include w3api/param_description.html metodo=_dato parametro="String version" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
