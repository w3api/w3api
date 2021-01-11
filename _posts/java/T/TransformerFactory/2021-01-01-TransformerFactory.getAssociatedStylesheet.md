---
title: TransformerFactory.getAssociatedStylesheet()
permalink: Java/TransformerFactory/getAssociatedStylesheet
date: 2021-01-11
key: JavaJava.T.TransformerFactory
category: java
tags: ['java se', 'javax.xml.transform', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TransformerFactory.metodos valor="getAssociatedStylesheet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Source getAssociatedStylesheet(Source source, String media, String title, String charset) throws TransformerConfigurationException
~~~

## Parámetros
* **String charset**,  {% include w3api/param_description.html metodo=_dato parametro="String charset" %}
* **Source source**,  {% include w3api/param_description.html metodo=_dato parametro="Source source" %}
* **String media**,  {% include w3api/param_description.html metodo=_dato parametro="String media" %}
* **String title**,  {% include w3api/param_description.html metodo=_dato parametro="String title" %}

## Excepciones
[TransformerConfigurationException](/Java/TransformerConfigurationException/)

## Clase Padre
[TransformerFactory](/Java/TransformerFactory/)

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
