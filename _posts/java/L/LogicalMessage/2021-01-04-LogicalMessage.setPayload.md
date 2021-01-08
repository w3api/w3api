---
title: LogicalMessage.setPayload()
permalink: Java/LogicalMessage/setPayload
date: 2021-01-04
key: JavaJava.L.LogicalMessage
category: java
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
* **JAXBContext context**,  {% include w3api/param_description.html metodo=_data parametro="JAXBContext context" %}
* **Object payload**,  {% include w3api/param_description.html metodo=_data parametro="Object payload" %}
* **Source payload**,  {% include w3api/param_description.html metodo=_data parametro="Source payload" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [WebServiceException](/Java/WebServiceException/)

## Clase Padre
[LogicalMessage](/Java/LogicalMessage/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LogicalMessage.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
