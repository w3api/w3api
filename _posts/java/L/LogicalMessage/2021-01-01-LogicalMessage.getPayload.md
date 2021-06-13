---
title: LogicalMessage.getPayload()
permalink: Java/LogicalMessage/getPayload
date: 2021-01-11
key: Java.L.LogicalMessage
category: java
tags: ['java se', 'javax.xml.ws', 'java.xml.ws', 'metodo java', 'Java 1.6', 'JAX-WS 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LogicalMessage.metodos valor="getPayload" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Source getPayload()
Object getPayload(JAXBContext context)
~~~

## Parámetros
* **JAXBContext context**,  {% include w3api/param_description.html metodo=_dato parametro="JAXBContext context" %}

## Excepciones
[WebServiceException](/Java/WebServiceException/)

## Clase Padre
[LogicalMessage](/Java/LogicalMessage/)

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
