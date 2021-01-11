---
title: DocumentBuilderFactory.setFeature()
permalink: Java/DocumentBuilderFactory/setFeature
date: 2021-01-11
key: JavaJava.D.DocumentBuilderFactory
category: java
tags: ['java se', 'javax.xml.parsers', 'java.xml', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocumentBuilderFactory.metodos valor="setFeature" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setFeature(String name, boolean value) throws ParserConfigurationException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **boolean value**,  {% include w3api/param_description.html metodo=_dato parametro="boolean value" %}

## Excepciones
[ParserConfigurationException](/Java/ParserConfigurationException/), [NullPointerException](/Java/NullPointerException/)

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
