---
title: XMLSignatureFactory.newXMLObject()
permalink: Java/XMLSignatureFactory/newXMLObject
date: 2021-01-11
key: JavaJava.X.XMLSignatureFactory
category: java
tags: ['java se', 'javax.xml.crypto.dsig', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLSignatureFactory.metodos valor="newXMLObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract XMLObject newXMLObject(List<? extends XMLStructure> content, String id, String mimeType, String encoding)
~~~

## Parámetros
* **String mimeType**,  {% include w3api/param_description.html metodo=_dato parametro="String mimeType" %}
* **String encoding**,  {% include w3api/param_description.html metodo=_dato parametro="String encoding" %}
* **String id**,  {% include w3api/param_description.html metodo=_dato parametro="String id" %}
* **List&lt;? extends XMLStructure&gt; content**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends XMLStructure> content" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/)

## Clase Padre
[XMLSignatureFactory](/Java/XMLSignatureFactory/)

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
