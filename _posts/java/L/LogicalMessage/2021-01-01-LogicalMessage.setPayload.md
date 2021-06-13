---
title: LogicalMessage.setPayload()
permalink: /Java/LogicalMessage/setPayload/
date: 2021-01-11
key: Java.L.LogicalMessage
category: Java
tags: ['java se', 'javax.xml.ws', 'java.xml.ws', 'metodo java', 'Java 1.6', 'JAX-WS 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LogicalMessage.metodos valor="setPayload" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setPayload(Object payload, JAXBContext context)
void setPayload(Source payload)
~~~

## Parámetros
* **Source payload**,  {% include w3api/param_description.html metodo=_dato parametro="Source payload" %}
* **Object payload**,  {% include w3api/param_description.html metodo=_dato parametro="Object payload" %}
* **JAXBContext context**,  {% include w3api/param_description.html metodo=_dato parametro="JAXBContext context" %}

## Excepciones
[WebServiceException](/Java/WebServiceException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

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
