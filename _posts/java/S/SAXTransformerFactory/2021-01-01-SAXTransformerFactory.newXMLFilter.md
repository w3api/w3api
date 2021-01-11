---
title: SAXTransformerFactory.newXMLFilter()
permalink: Java/SAXTransformerFactory/newXMLFilter
date: 2021-01-11
key: JavaJava.S.SAXTransformerFactory
category: java
tags: ['java se', 'javax.xml.transform.sax', 'java.xml', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SAXTransformerFactory.metodos valor="newXMLFilter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract XMLFilter newXMLFilter(Source src) throws TransformerConfigurationException
public abstract XMLFilter newXMLFilter(Templates templates) throws TransformerConfigurationException
~~~

## Parámetros
* **Source src**,  {% include w3api/param_description.html metodo=_dato parametro="Source src" %}
* **Templates templates**,  {% include w3api/param_description.html metodo=_dato parametro="Templates templates" %}

## Excepciones
[TransformerConfigurationException](/Java/TransformerConfigurationException/)

## Clase Padre
[SAXTransformerFactory](/Java/SAXTransformerFactory/)

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
