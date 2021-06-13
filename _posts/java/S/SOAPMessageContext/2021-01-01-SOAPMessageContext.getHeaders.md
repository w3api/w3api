---
title: SOAPMessageContext.getHeaders()
permalink: /Java/SOAPMessageContext/getHeaders/
date: 2021-01-11
key: Java.S.SOAPMessageContext
category: Java
tags: ['java se', 'javax.xml.ws.handler.soap', 'java.xml.ws', 'metodo java', 'Java 1.6', 'JAX-WS 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPMessageContext.metodos valor="getHeaders" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object[] getHeaders(QName header, JAXBContext context, boolean allRoles)
~~~

## Parámetros
* **boolean allRoles**,  {% include w3api/param_description.html metodo=_dato parametro="boolean allRoles" %}
* **JAXBContext context**,  {% include w3api/param_description.html metodo=_dato parametro="JAXBContext context" %}
* **QName header**,  {% include w3api/param_description.html metodo=_dato parametro="QName header" %}

## Excepciones
[WebServiceException](/Java/WebServiceException/)

## Clase Padre
[SOAPMessageContext](/Java/SOAPMessageContext/)

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
