---
title: SOAPElementFactory.create()
permalink: Java/SOAPElementFactory/create
date: 2021-01-11
key: JavaJava.S.SOAPElementFactory
category: java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPElementFactory.metodos valor="create" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SOAPElement create(String localName) throws SOAPException
public SOAPElement create(String localName, String prefix, String uri) throws SOAPException
public SOAPElement create(Name name) throws SOAPException
~~~

## Parámetros
* **Name name**,  {% include w3api/param_description.html metodo=_dato parametro="Name name" %}
* **String uri**,  {% include w3api/param_description.html metodo=_dato parametro="String uri" %}
* **String localName**,  {% include w3api/param_description.html metodo=_dato parametro="String localName" %}
* **String prefix**,  {% include w3api/param_description.html metodo=_dato parametro="String prefix" %}

## Excepciones
[SOAPException](/Java/SOAPException/)

## Clase Padre
[SOAPElementFactory](/Java/SOAPElementFactory/)

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
