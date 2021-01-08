---
title: SOAPFactory.createName()
permalink: Java/SOAPFactory/createName
date: 2021-01-04
key: JavaJava.S.SOAPFactory
category: java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPFactory.metodos valor="createName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Name createName(String localName) throws SOAPException
public abstract Name createName(String localName, String prefix, String uri) throws SOAPException
~~~

## Parámetros
* **String localName**,  {% include w3api/param_description.html metodo=_data parametro="String localName" %}
* **String prefix**,  {% include w3api/param_description.html metodo=_data parametro="String prefix" %}
* **String uri**,  {% include w3api/param_description.html metodo=_data parametro="String uri" %}

## Excepciones
[SOAPException](/Java/SOAPException/)

## Clase Padre
[SOAPFactory](/Java/SOAPFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SOAPFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
