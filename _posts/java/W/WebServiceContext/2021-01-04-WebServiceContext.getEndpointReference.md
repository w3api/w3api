---
title: WebServiceContext.getEndpointReference()
permalink: Java/WebServiceContext/getEndpointReference
date: 2021-01-04
key: JavaJava.W.WebServiceContext
category: java
tags: ['java se', 'javax.xml.ws', 'java.xml.ws', 'metodo java', 'Java 1.6', 'JAX-WS 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WebServiceContext.metodos valor="getEndpointReference" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T extends EndpointReference>T getEndpointReference(Class<T> clazz, Element... referenceParameters)
EndpointReference getEndpointReference(Element... referenceParameters)
~~~

## Parámetros
* **Class&lt;T&gt; clazz**,  {% include w3api/param_description.html metodo=_data parametro="Class<T> clazz" %}
* **Element... referenceParameters**,  {% include w3api/param_description.html metodo=_data parametro="Element... referenceParameters" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[WebServiceContext](/Java/WebServiceContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.WebServiceContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
