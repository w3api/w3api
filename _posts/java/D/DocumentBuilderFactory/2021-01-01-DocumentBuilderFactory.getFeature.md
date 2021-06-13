---
title: DocumentBuilderFactory.getFeature()
permalink: /Java/DocumentBuilderFactory/getFeature/
date: 2021-01-11
key: Java.D.DocumentBuilderFactory
category: Java
tags: ['java se', 'javax.xml.parsers', 'java.xml', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocumentBuilderFactory.metodos valor="getFeature" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract boolean getFeature(String name) throws ParserConfigurationException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[ParserConfigurationException](/Java/ParserConfigurationException/)

## Clase Padre
[DocumentBuilderFactory](/Java/DocumentBuilderFactory/)

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
