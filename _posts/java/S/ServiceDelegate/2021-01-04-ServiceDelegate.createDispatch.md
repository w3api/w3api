---
title: ServiceDelegate.createDispatch()
permalink: Java/ServiceDelegate/createDispatch
date: 2021-01-04
key: JavaJava.S.ServiceDelegate
category: java
tags: ['java se', 'javax.xml.ws.spi', 'java.xml.ws', 'metodo java', 'Java 1.6', 'JAX-WS 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServiceDelegate.metodos valor="createDispatch" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
abstract <T> Dispatch<T> createDispatch(QName portName, Class<T> type, Service.Mode mode)
abstract <T> Dispatch<T> createDispatch(QName portName, Class<T> type, Service.Mode mode, WebServiceFeature... features)
public abstract Dispatch<Object> createDispatch(QName portName, JAXBContext context, Service.Mode mode)
public abstract Dispatch<Object> createDispatch(QName portName, JAXBContext context, Service.Mode mode, WebServiceFeature... features)
abstract <T> Dispatch<T> createDispatch(EndpointReference endpointReference, Class<T> type, Service.Mode mode, WebServiceFeature... features)
public abstract Dispatch<Object> createDispatch(EndpointReference endpointReference, JAXBContext context, Service.Mode mode, WebServiceFeature... features)
~~~

## Parámetros
* **QName portName**,  {% include w3api/param_description.html metodo=_data parametro="QName portName" %}
* **Class&lt;T&gt; type**,  {% include w3api/param_description.html metodo=_data parametro="Class<T> type" %}
* **Service.Mode mode**,  {% include w3api/param_description.html metodo=_data parametro="Service.Mode mode" %}
* **WebServiceFeature... features**,  {% include w3api/param_description.html metodo=_data parametro="WebServiceFeature... features" %}
* **JAXBContext context**,  {% include w3api/param_description.html metodo=_data parametro="JAXBContext context" %}
* **EndpointReference endpointReference**,  {% include w3api/param_description.html metodo=_data parametro="EndpointReference endpointReference" %}

## Excepciones
[WebServiceException](/Java/WebServiceException/)

## Clase Padre
[ServiceDelegate](/Java/ServiceDelegate/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ServiceDelegate.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
