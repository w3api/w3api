---
title: SOAPFactory.createElement()
permalink: Java/SOAPFactory/createElement
date: 2021-01-04
key: JavaJava.S.SOAPFactory
category: java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPFactory.metodos valor="createElement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract SOAPElement createElement(String localName) throws SOAPException
public abstract SOAPElement createElement(String localName, String prefix, String uri) throws SOAPException
public SOAPElement createElement(QName qname) throws SOAPException
public abstract SOAPElement createElement(Name name) throws SOAPException
public SOAPElement createElement(Element domElement) throws SOAPException
~~~

## Parámetros
* **QName qname**,  {% include w3api/param_description.html metodo=_data parametro="QName qname" %}
* **String localName**,  {% include w3api/param_description.html metodo=_data parametro="String localName" %}
* **String prefix**,  {% include w3api/param_description.html metodo=_data parametro="String prefix" %}
* **String uri**,  {% include w3api/param_description.html metodo=_data parametro="String uri" %}
* **Element domElement**,  {% include w3api/param_description.html metodo=_data parametro="Element domElement" %}
* **Name name**,  {% include w3api/param_description.html metodo=_data parametro="Name name" %}

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
