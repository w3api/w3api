---
title: SOAPEnvelope.createName()
permalink: /Java/SOAPEnvelope/createName/
date: 2021-01-11
key: Java.S.SOAPEnvelope
category: Java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPEnvelope.metodos valor="createName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Name createName(String localName) throws SOAPException
Name createName(String localName, String prefix, String uri) throws SOAPException
~~~

## Parámetros
* **String uri**,  {% include w3api/param_description.html metodo=_dato parametro="String uri" %}
* **String localName**,  {% include w3api/param_description.html metodo=_dato parametro="String localName" %}
* **String prefix**,  {% include w3api/param_description.html metodo=_dato parametro="String prefix" %}

## Excepciones
[SOAPException](/Java/SOAPException/)

## Clase Padre
[SOAPEnvelope](/Java/SOAPEnvelope/)

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
